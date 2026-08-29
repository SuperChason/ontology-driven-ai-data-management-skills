#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
PLATFORM="codex"
TARGET_DIR=""
SKILL_NAME=""
FORCE=false

usage() {
  cat <<'EOF'
Usage: ./scripts/install.sh [codex|claude-code] [options]

Options:
  --force          Replace an existing skill with the repository version.
  --skill NAME     Install or update one skill only.
  --target DIR     Override the default installation directory.
  -h, --help       Show this help.

Default locations:
  Codex:       ~/.codex/skills
  Claude Code: ~/.claude/skills
EOF
}

if [[ "${1:-}" == "codex" || "${1:-}" == "claude-code" ]]; then
  PLATFORM="$1"
  shift
fi

while [[ $# -gt 0 ]]; do
  case "$1" in
    --force)
      FORCE=true
      shift
      ;;
    --skill)
      [[ $# -ge 2 ]] || { echo "--skill requires a skill name" >&2; exit 2; }
      SKILL_NAME="$2"
      shift 2
      ;;
    --target)
      [[ $# -ge 2 ]] || { echo "--target requires a directory" >&2; exit 2; }
      TARGET_DIR="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ -z "${TARGET_DIR}" ]]; then
  case "${PLATFORM}" in
    codex)
      TARGET_DIR="${CODEX_SKILLS_DIR:-${HOME}/.codex/skills}"
      ;;
    claude-code)
      TARGET_DIR="${CLAUDE_SKILLS_DIR:-${HOME}/.claude/skills}"
      ;;
  esac
fi

case "${TARGET_DIR}" in
  ""|"/"|"${HOME}")
    echo "Refusing unsafe target directory: ${TARGET_DIR:-<empty>}" >&2
    exit 2
    ;;
esac

if [[ -n "${SKILL_NAME}" && ! "${SKILL_NAME}" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "Invalid skill name: ${SKILL_NAME}" >&2
  exit 2
fi

mkdir -p "${TARGET_DIR}"

installed=0
skipped=0
for skill_dir in "${REPO_DIR}"/skills/*; do
  [[ -d "${skill_dir}" ]] || continue
  skill_name="$(basename "${skill_dir}")"
  if [[ -n "${SKILL_NAME}" && "${skill_name}" != "${SKILL_NAME}" ]]; then
    continue
  fi
  target_skill="${TARGET_DIR}/${skill_name}"
  if [[ -e "${target_skill}" && "${FORCE}" != true ]]; then
    echo "Skipped existing skill: ${skill_name}"
    skipped=$((skipped + 1))
    continue
  fi
  if [[ -e "${target_skill}" ]]; then
    rm -rf "${target_skill}"
  fi
  mkdir -p "${target_skill}"
  cp "${skill_dir}/SKILL.md" "${target_skill}/SKILL.md"
  for resource_dir in scripts references assets; do
    if [[ -d "${skill_dir}/${resource_dir}" ]]; then
      cp -R "${skill_dir}/${resource_dir}" "${target_skill}/${resource_dir}"
    fi
  done
  if [[ "${PLATFORM}" == "codex" && -d "${skill_dir}/agents" ]]; then
    cp -R "${skill_dir}/agents" "${target_skill}/agents"
  fi
  installed=$((installed + 1))
done

if [[ -n "${SKILL_NAME}" && ${installed} -eq 0 && ${skipped} -eq 0 ]]; then
  echo "Skill not found: ${SKILL_NAME}" >&2
  exit 1
fi

echo "Platform: ${PLATFORM}"
echo "Installed ${installed} skills to ${TARGET_DIR}; skipped ${skipped}"
