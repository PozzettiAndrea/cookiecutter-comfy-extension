"""
Pre-startup script for {{cookiecutter.project_name}} ComfyUI node.

Copies example assets to ComfyUI input directory.
"""

import shutil
from pathlib import Path


def copy_assets():
    """Copy example assets to ComfyUI input directory."""
    # Find ComfyUI root (go up from custom_nodes)
    this_dir = Path(__file__).parent
    comfy_root = this_dir.parent.parent  # custom_nodes/../..

    input_dir = comfy_root / "input"
    if not input_dir.exists():
        print(f"[{{cookiecutter.project_slug}}] ComfyUI input dir not found: {input_dir}")
        return

    assets_dir = this_dir / "assets"
    if not assets_dir.exists():
        return  # No assets to copy

    # Copy each asset file if it doesn't exist
    for asset_file in assets_dir.iterdir():
        if asset_file.name.startswith("."):
            continue  # Skip hidden files like .gitkeep

        dest = input_dir / asset_file.name
        if not dest.exists():
            print(f"[{{cookiecutter.project_slug}}] Copying {asset_file.name} to input/")
            if asset_file.is_dir():
                shutil.copytree(asset_file, dest)
            else:
                shutil.copy2(asset_file, dest)


if __name__ == "__main__":
    copy_assets()
else:
    # Run on import (ComfyUI prestartup)
    copy_assets()
