import os
import subprocess

CORVUS_ASTROMETRY_DIR = os.path.dirname(os.path.abspath(__file__))

KEEP_FILES = {
    "CREDITS",
    "Changelog",
    "LICENSE",
    "Makefile",
    "README.md",
    "__init__.py",
    "astrometry",
    "configure",
    "setup-libkd.py",
    "setup.py",
    "clean_up.py",
    "requirements.txt"
}

def clean_up(dir_to_clean, keep_files):
    for filename in os.listdir(dir_to_clean):
        full_path = os.path.join(dir_to_clean, filename)

        # Skip directories
        if os.path.isdir(full_path):
            continue

        # Skip files in the keep list
        if filename in keep_files:
            continue

        # Delete file
        try:
            os.remove(full_path)
            print(f"Removed {full_path}")
        except Exception as e:
            print(f"Could not remove {full_path}: {e}")

if __name__ == '__main__':
    dir_to_clean = CORVUS_ASTROMETRY_DIR
    keep_files = KEEP_FILES

    clean_up(dir_to_clean, keep_files)