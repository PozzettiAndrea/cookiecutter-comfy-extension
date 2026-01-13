"""
Install script for {{cookiecutter.project_name}} ComfyUI node.

Uses comfy-env for isolated environment management.
"""

import subprocess
import sys
from pathlib import Path


def ensure_comfy_env():
    """Ensure comfy-env package is installed."""
    try:
        import comfy_env
        return True
    except ImportError:
        print("[{{cookiecutter.project_slug}}] Installing comfy-env...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "comfy-env", "-q"
        ])
        return True


def main():
    """Main installation routine."""
    print(f"[{{cookiecutter.project_slug}}] Running install.py...")

    # Ensure comfy-env is available
    if not ensure_comfy_env():
        print("[{{cookiecutter.project_slug}}] Failed to install comfy-env")
        return False

    from comfy_env import IsolatedEnvManager

    # Load config from comfy-env.toml
    config_path = Path(__file__).parent / "comfy-env.toml"
    if not config_path.exists():
        print(f"[{{cookiecutter.project_slug}}] Warning: comfy-env.toml not found")
        return True

    # Create isolated environment
    manager = IsolatedEnvManager(config_path)

    try:
        manager.ensure_environment("{{cookiecutter.project_slug}}")
        print(f"[{{cookiecutter.project_slug}}] Environment ready")
        return True
    except Exception as e:
        print(f"[{{cookiecutter.project_slug}}] Environment setup failed: {e}")
        return False


if __name__ == "__main__":
    main()
