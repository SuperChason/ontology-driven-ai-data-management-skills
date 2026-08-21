#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
TARGET_DIR="${CODEX_SKILLS_DIR:-${HOME}/.agents/skills}"
FORCE=false

if [[ "${1:-}" == "--force" ]]; then
  FORCE=true
elif [[ $# -gt 0 ]]; then
  echo "Usage: $0 [--force]" >&2
  exit 2
fi

mkdir -p "${TARGET_DIR}"

installed=0
skipped=0
for skill_dir in "${REPO_DIR}"/skills/*; do
  [[ -d "${skill_dir}" ]] || continue
  skill_name="$(basename "${skill_dir}")"
  target_skill="${TARGET_DIR}/${skill_name}"
  if [[ -e "${target_skill}" && "${FORCE}" != true ]]; then
    echo "Skipped existing skill: ${skill_name}"
    skipped=$((skipped + 1))
    continue
  fi
  if [[ -e "${target_skill}" ]]; then
    rm -rf "${target_skill}"
  fi
  cp -R "${skill_dir}" "${TARGET_DIR}/${skill_name}"
  installed=$((installed + 1))
done

echo "Installed ${installed} skills to ${TARGET_DIR}; skipped ${skipped}"
