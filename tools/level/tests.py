import sys
from pathlib import Path

def shallow_verification(source: Path):
    if source.exists() and not source.is_file():
        print("Shallow verification passed.")
    else:
        print(f"Shallow verification failed. {str(source)} does not exist or isn't directory.")

def step_one_verification(source: Path):
    meta = source / "data.json"

    if meta.exists() and meta.is_file():
        print("Step 1 verification passed.")
    else:
        print(f"Step 1 verification failed. {str(meta)} does not exist or is directory.")

def step_two_verification(source: Path):
    layout = source / "layout.txt"

    if layout.exists() and layout.is_file():
        print("Step 2 verification passed.")
    else:
        print(f"Step 2 verification failed. {str(layout)} does not exist or is directory.")
