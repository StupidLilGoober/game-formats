"""
Version 1.0
Packages levels into a tidy format.
"""

import sys

args = sys.argv
usage_msg = f"USAGE: <level input dir> <level output dir>"

if len(args) < 3:
    print(usage_msg)
    sys.exit(1)

from pathlib import Path

import zipfile as zip

source_dir = Path(args[1])

import tests

tests.shallow_verification(source_dir)
tests.step_one_verification(source_dir)

output_file = Path(args[2]).with_suffix(".lvl")

print(f"PACKAGING {args[1]} TO {str(output_file)}")

with zip.ZipFile(output_file, "w", compression=zip.ZIP_STORED) as zipf:
    for file in source_dir.rglob("*"):
        if file.is_file():
            zipf.write(file, arcname=file.relative_to(source_dir))
