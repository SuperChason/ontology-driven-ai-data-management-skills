#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
EXPECTED_COUNT = 16


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def archive_names(path: Path) -> set[str]:
    with zipfile.ZipFile(path) as archive:
        bad = archive.testzip()
        if bad:
            raise ValueError(f"{path.name}: corrupt member {bad}")
        return set(archive.namelist())


def validate_agent_archive(path: Path, platform: str, errors: list[str]) -> None:
    try:
        names = archive_names(path)
    except (OSError, zipfile.BadZipFile, ValueError) as exc:
        errors.append(str(exc))
        return
    skill_files = [name for name in names if name.endswith("/SKILL.md")]
    if len(skill_files) != EXPECTED_COUNT:
        errors.append(f"{path.name}: expected {EXPECTED_COUNT} SKILL.md files, found {len(skill_files)}")
    openai_files = [name for name in names if name.endswith("/agents/openai.yaml")]
    expected_openai = EXPECTED_COUNT if platform == "codex" else 0
    if len(openai_files) != expected_openai:
        errors.append(f"{path.name}: expected {expected_openai} openai.yaml files, found {len(openai_files)}")
    if any(name.endswith("test-prompts.json") or name.endswith("test-results.md") for name in names):
        errors.append(f"{path.name}: contains test-only files")
    with zipfile.ZipFile(path) as archive:
        installers = [info for info in archive.infolist() if info.filename.endswith("/scripts/install.sh")]
        if len(installers) != 1:
            errors.append(f"{path.name}: expected one install.sh")
        elif not ((installers[0].external_attr >> 16) & 0o111):
            errors.append(f"{path.name}: install.sh is not executable")


def validate_workbuddy(path: Path, errors: list[str]) -> None:
    try:
        names = archive_names(path)
    except (OSError, zipfile.BadZipFile, ValueError) as exc:
        errors.append(str(exc))
        return
    if "SKILL.md" not in names:
        errors.append(f"{path.name}: SKILL.md is not at archive root")
    if any(name.startswith("agents/") or name.startswith("test-") for name in names):
        errors.append(f"{path.name}: contains platform-specific or test-only files")


def validate_workbuddy_bundle(path: Path, errors: list[str]) -> None:
    try:
        names = archive_names(path)
    except (OSError, zipfile.BadZipFile, ValueError) as exc:
        errors.append(str(exc))
        return
    nested = sorted(name for name in names if "/skills/" in name and name.endswith(".zip"))
    if len(nested) != EXPECTED_COUNT:
        errors.append(f"{path.name}: expected {EXPECTED_COUNT} nested skill archives, found {len(nested)}")
        return
    checksum_members = [name for name in names if name.endswith("/SHA256SUMS.txt")]
    if len(checksum_members) != 1:
        errors.append(f"{path.name}: expected one nested SHA256SUMS.txt")
        return
    checksum_member = checksum_members[0]
    prefix = checksum_member.removesuffix("SHA256SUMS.txt")
    with zipfile.ZipFile(path) as archive:
        lines = archive.read(checksum_member).decode("utf-8").splitlines()
        listed: set[str] = set()
        for line in lines:
            expected, relative = line.split("  ", 1)
            member = f"{prefix}{relative}"
            listed.add(member)
            if member not in names or hashlib.sha256(archive.read(member)).hexdigest() != expected:
                errors.append(f"{path.name}: nested checksum mismatch: {relative}")
        if listed != set(nested):
            errors.append(f"{path.name}: nested checksum list does not match bundled skills")


def main() -> int:
    errors: list[str] = []
    release_version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    codex = DIST / f"ontology-skills-codex-v{release_version}.zip"
    claude = DIST / f"ontology-skills-claude-code-v{release_version}.zip"
    workbuddy_bundle = DIST / f"ontology-skills-workbuddy-v{release_version}.zip"

    for path in (codex, claude, workbuddy_bundle):
        if not path.is_file():
            errors.append(f"missing {path.relative_to(ROOT)}")
    if codex.is_file():
        validate_agent_archive(codex, "codex", errors)
    if claude.is_file():
        validate_agent_archive(claude, "claude-code", errors)

    individual = sorted((DIST / "workbuddy" / "skills").glob("*.zip"))
    if len(individual) != EXPECTED_COUNT:
        errors.append(f"expected {EXPECTED_COUNT} WorkBuddy skill archives, found {len(individual)}")
    for path in individual:
        validate_workbuddy(path, errors)
    if workbuddy_bundle.is_file():
        validate_workbuddy_bundle(workbuddy_bundle, errors)

    checksum_file = DIST / "SHA256SUMS.txt"
    if not checksum_file.is_file():
        errors.append("missing dist/SHA256SUMS.txt")
    else:
        listed: set[str] = set()
        for line in checksum_file.read_text(encoding="utf-8").splitlines():
            expected, relative = line.split("  ", 1)
            listed.add(relative)
            path = DIST / relative
            if not path.is_file() or digest(path) != expected:
                errors.append(f"checksum mismatch: {relative}")
        expected_release_files = {path.name for path in (codex, claude, workbuddy_bundle)}
        if listed != expected_release_files:
            errors.append("SHA256SUMS.txt must list exactly the three release archives")

    if errors:
        print("Package validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Package validation passed: Codex, Claude Code, and {len(individual)} WorkBuddy skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
