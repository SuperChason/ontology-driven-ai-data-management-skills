#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import shutil
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
DEFAULT_OUTPUT = ROOT / "dist"
RESOURCE_DIRS = ("scripts", "references", "assets")
FIXED_ZIP_TIME = (2026, 1, 1, 0, 0, 0)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build Codex, Claude Code, and WorkBuddy packages.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def version() -> str:
    value = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not value:
        raise ValueError("VERSION is empty")
    return value


def runtime_files(skill_dir: Path, platform: str) -> list[Path]:
    files = [skill_dir / "SKILL.md"]
    if platform == "codex":
        files.extend(sorted((skill_dir / "agents").rglob("*")))
    for directory in RESOURCE_DIRS:
        resource = skill_dir / directory
        if resource.is_dir():
            files.extend(sorted(resource.rglob("*")))
    return [path for path in files if path.is_file()]


def copy_skill(skill_dir: Path, target: Path, platform: str) -> None:
    for source in runtime_files(skill_dir, platform):
        relative = source.relative_to(skill_dir)
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def write_zip(zip_path: Path, source_dir: Path, prefix: str = "") -> None:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for source in sorted(path for path in source_dir.rglob("*") if path.is_file()):
            relative = source.relative_to(source_dir).as_posix()
            archive_name = f"{prefix.rstrip('/')}/{relative}" if prefix else relative
            info = zipfile.ZipInfo(archive_name, date_time=FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            permissions = 0o100755 if source.stat().st_mode & 0o111 else 0o100644
            info.external_attr = permissions << 16
            archive.writestr(info, source.read_bytes())


def copy_distribution_files(target: Path) -> None:
    for name in ("README.md", "LICENSE", "NOTICE", "VERSION"):
        shutil.copy2(ROOT / name, target / name)
    scripts_dir = target / "scripts"
    scripts_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "scripts" / "install.sh", scripts_dir / "install.sh")


def build_agent_package(output: Path, platform: str, release_version: str) -> Path:
    archive_name = f"ontology-skills-{platform}-v{release_version}.zip"
    with tempfile.TemporaryDirectory(prefix=f"ontology-{platform}-") as temp_name:
        stage = Path(temp_name) / f"ontology-skills-{platform}-v{release_version}"
        stage.mkdir(parents=True)
        copy_distribution_files(stage)
        for skill_dir in sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir()):
            copy_skill(skill_dir, stage / "skills" / skill_dir.name, platform)
        write_zip(output / archive_name, stage, prefix=stage.name)
    return output / archive_name


def build_workbuddy_package(output: Path, release_version: str) -> tuple[Path, list[Path]]:
    individual_dir = output / "workbuddy" / "skills"
    individual_dir.mkdir(parents=True, exist_ok=True)
    individual_archives: list[Path] = []

    for skill_dir in sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir()):
        with tempfile.TemporaryDirectory(prefix="ontology-workbuddy-skill-") as temp_name:
            stage = Path(temp_name)
            copy_skill(skill_dir, stage, "workbuddy")
            for name in ("LICENSE", "NOTICE", "VERSION"):
                shutil.copy2(ROOT / name, stage / name)
            archive_path = individual_dir / f"{skill_dir.name}-v{release_version}.zip"
            write_zip(archive_path, stage)
            individual_archives.append(archive_path)

    with tempfile.TemporaryDirectory(prefix="ontology-workbuddy-") as temp_name:
        stage = Path(temp_name) / f"ontology-skills-workbuddy-v{release_version}"
        stage.mkdir(parents=True)
        for name in ("README.md", "LICENSE", "NOTICE", "VERSION"):
            shutil.copy2(ROOT / name, stage / name)
        target_skills = stage / "skills"
        target_skills.mkdir()
        for archive_path in individual_archives:
            shutil.copy2(archive_path, target_skills / archive_path.name)
        (stage / "SHA256SUMS.txt").write_text(
            "".join(
                f"{sha256(archive_path)}  skills/{archive_path.name}\n"
                for archive_path in individual_archives
            ),
            encoding="utf-8",
        )
        bundle = output / f"ontology-skills-workbuddy-v{release_version}.zip"
        write_zip(bundle, stage, prefix=stage.name)

    return bundle, individual_archives


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    args = parse_args()
    output = args.output.resolve()
    if output in (Path("/"), ROOT):
        raise ValueError(f"unsafe output directory: {output}")
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    release_version = version()
    artifacts = [
        build_agent_package(output, "codex", release_version),
        build_agent_package(output, "claude-code", release_version),
    ]
    workbuddy_bundle, individual = build_workbuddy_package(output, release_version)
    artifacts.append(workbuddy_bundle)

    checksum_file = output / "SHA256SUMS.txt"
    checksum_file.write_text(
        "".join(f"{sha256(path)}  {path.relative_to(output).as_posix()}\n" for path in sorted(artifacts)),
        encoding="utf-8",
    )
    print(
        f"Built {len(artifacts)} release archives and "
        f"{len(individual)} WorkBuddy skill archives in {output}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
