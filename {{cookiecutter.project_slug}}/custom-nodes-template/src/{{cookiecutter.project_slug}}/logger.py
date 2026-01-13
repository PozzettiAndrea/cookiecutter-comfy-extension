"""
Logging helper for {{cookiecutter.project_name}}.

Usage:
    from .logger import log, warn, error

    log("Model loaded successfully")
    warn("Using CPU fallback")
    error("Failed to load model")
"""

PROJECT_NAME = "{{cookiecutter.project_slug}}"


def log(msg):
    """Print info message with project prefix."""
    print(f"[{PROJECT_NAME}] {msg}")


def warn(msg):
    """Print warning message with project prefix."""
    print(f"[{PROJECT_NAME}] WARNING: {msg}")


def error(msg):
    """Print error message with project prefix."""
    print(f"[{PROJECT_NAME}] ERROR: {msg}")
