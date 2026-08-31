#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
EXPECTED_COUNT = 25
FORBIDDEN_PATTERNS = {
    "absolute user path": re.compile(r"/Users/|[A-Za-z]:\\\\Users\\\\"),
    "project-specific content": re.compile(r"雅江|CYJDRP|中国雅江集团|久其"),
    "book excerpt section": re.compile(r"原文（Reading）|PDF第|书页\d+"),
}


def frontmatter(text: str) -> str:
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        raise ValueError("missing YAML frontmatter")
    return match.group(1)


def scalar(field: str, yaml_text: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(field)}:\s*([^|>].*)$", yaml_text)
    return match.group(1).strip().strip('"\'') if match else None


def block_scalar(field: str, yaml_text: str) -> str | None:
    match = re.search(
        rf"(?ms)^{re.escape(field)}:\s*[|>]\s*\n((?:  .*\n?)*)",
        yaml_text,
    )
    if not match:
        return None
    return "\n".join(line[2:] for line in match.group(1).splitlines()).strip()


def validate_metadata(skill_name: str, yaml_text: str) -> list[str]:
    errors: list[str] = []
    match = re.search(r"(?ms)^metadata:\s*\n((?:  .*\n?)*)", yaml_text)
    if not match:
        return errors
    for line in match.group(1).splitlines():
        if not re.fullmatch(r'  [a-z0-9-]+:\s*"[^"]*"', line):
            errors.append(f"{skill_name}: metadata values must be quoted strings: {line.strip()}")
    return errors


def tracked_text_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    paths = []
    for raw in result.stdout.decode("utf-8").split("\0"):
        if not raw:
            continue
        path = ROOT / raw
        if path.is_file() and path.suffix not in {".png", ".jpg", ".jpeg", ".gif", ".zip"}:
            paths.append(path)
    return paths


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    required = [
        skill_dir / "SKILL.md",
        skill_dir / "agents" / "openai.yaml",
        skill_dir / "test-prompts.json",
        skill_dir / "test-results.md",
    ]
    for path in required:
        if not path.is_file():
            errors.append(f"{skill_dir.name}: missing {path.relative_to(skill_dir)}")

    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return errors

    text = skill_file.read_text(encoding="utf-8")
    try:
        yaml_text = frontmatter(text)
    except ValueError as exc:
        errors.append(f"{skill_dir.name}: {exc}")
        return errors

    name = scalar("name", yaml_text)
    if name != skill_dir.name:
        errors.append(f"{skill_dir.name}: frontmatter name is {name!r}")
    if not name or len(name) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append(f"{skill_dir.name}: name does not follow Agent Skills naming rules")

    description = scalar("description", yaml_text) or block_scalar("description", yaml_text)
    if not description:
        errors.append(f"{skill_dir.name}: missing description")
    elif len(description) > 1024:
        errors.append(f"{skill_dir.name}: description exceeds 1024 characters")

    errors.extend(validate_metadata(skill_dir.name, yaml_text))

    related_value = scalar("  related-skills", yaml_text) or ""
    for relation in filter(None, (item.strip() for item in related_value.split(","))):
        related_name = relation.split(":", 1)[0]
        if not (SKILLS_DIR / related_name / "SKILL.md").is_file():
            errors.append(f"{skill_dir.name}: unknown related skill {related_name}")

    if len(text.splitlines()) > 500:
        errors.append(f"{skill_dir.name}: SKILL.md exceeds 500 lines")

    for label, pattern in FORBIDDEN_PATTERNS.items():
        if pattern.search(text):
            errors.append(f"{skill_dir.name}: contains {label}")

    prompts_file = skill_dir / "test-prompts.json"
    if prompts_file.is_file():
        try:
            payload = json.loads(prompts_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{skill_dir.name}: invalid test-prompts.json: {exc}")
        else:
            if payload.get("skill") != skill_dir.name:
                errors.append(f"{skill_dir.name}: test skill name mismatch")
            cases = payload.get("test_cases")
            if not isinstance(cases, list) or len(cases) < 3:
                errors.append(f"{skill_dir.name}: expected at least 3 test cases")

    openai_file = skill_dir / "agents" / "openai.yaml"
    if openai_file.is_file():
        openai_text = openai_file.read_text(encoding="utf-8")
        for field in ("display_name", "short_description", "default_prompt"):
            if not re.search(rf"(?m)^\s+{field}:\s*.+$", openai_text):
                errors.append(f"{skill_dir.name}: missing agents/openai.yaml {field}")

    return errors


def main() -> int:
    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    errors: list[str] = []
    if len(skill_dirs) != EXPECTED_COUNT:
        errors.append(f"expected {EXPECTED_COUNT} skills, found {len(skill_dirs)}")

    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    repo_text = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for path in tracked_text_files()
        if path.resolve() != Path(__file__).resolve()
    )
    for label, pattern in FORBIDDEN_PATTERNS.items():
        if pattern.search(repo_text):
            errors.append(f"repository contains {label}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validation passed: {len(skill_dirs)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
