"""
{{cookiecutter.project_name}}: {{cookiecutter.project_short_description}}
"""
import os
import sys
import traceback

__author__ = """{{cookiecutter.full_name}}"""
__email__ = "{{cookiecutter.email}}"
__version__ = "{{cookiecutter.version}}"

# Track initialization status
INIT_SUCCESS = False
INIT_ERRORS = []

# Detect if running under pytest
# Only skip initialization when PYTEST_CURRENT_TEST env var is set.
# Note: Checking '_pytest.config' in sys.modules causes false positives
# when ComfyUI or dependencies import pytest.
# Allow override with {{cookiecutter.project_slug | upper}}_FORCE_INIT=1
force_init = os.environ.get('{{cookiecutter.project_slug | upper}}_FORCE_INIT') == '1'
is_pytest = 'PYTEST_CURRENT_TEST' in os.environ
skip_init = is_pytest and not force_init

if not skip_init:
    print(f"[{{cookiecutter.project_slug}}] v{__version__} initializing...")

    # Register model folder with ComfyUI
    try:
        import folder_paths
        model_dir = os.path.join(folder_paths.models_dir, "{{cookiecutter.project_slug}}")
        os.makedirs(model_dir, exist_ok=True)
        folder_paths.add_model_folder_path("{{cookiecutter.project_slug}}", model_dir)
        print(f"[{{cookiecutter.project_slug}}] Registered model folder: {model_dir}")
    except Exception as e:
        error_msg = f"Failed to register model folder: {str(e)}"
        INIT_ERRORS.append(error_msg)
        print(f"[{{cookiecutter.project_slug}}] WARNING: {error_msg}")

    # Import node classes
    try:
        from .src.{{cookiecutter.project_slug}}.nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
        print(f"[{{cookiecutter.project_slug}}] Node classes imported successfully")
        INIT_SUCCESS = True
    except Exception as e:
        error_msg = f"Failed to import node classes: {str(e)}"
        INIT_ERRORS.append(error_msg)
        print(f"[{{cookiecutter.project_slug}}] ERROR: {error_msg}")
        print(f"[{{cookiecutter.project_slug}}] Traceback:\n{traceback.format_exc()}")

        # Set empty mappings if import failed
        NODE_CLASS_MAPPINGS = {}
        NODE_DISPLAY_NAME_MAPPINGS = {}

    # Report final status
    if INIT_SUCCESS:
        print(f"[{{cookiecutter.project_slug}}] Loaded successfully!")
        if NODE_CLASS_MAPPINGS:
            print(f"[{{cookiecutter.project_slug}}] Available nodes: {', '.join(NODE_CLASS_MAPPINGS.keys())}")
    else:
        print(f"[{{cookiecutter.project_slug}}] Failed to load ({len(INIT_ERRORS)} error(s)):")
        for error in INIT_ERRORS:
            print(f"  - {error}")

else:
    # During testing, skip initialization
    print(f"[{{cookiecutter.project_slug}}] v{__version__} running in pytest mode - skipping initialization")
    print(f"[{{cookiecutter.project_slug}}] Set {{cookiecutter.project_slug | upper}}_FORCE_INIT=1 to override")

    NODE_CLASS_MAPPINGS = {}
    NODE_DISPLAY_NAME_MAPPINGS = {}

{% if cookiecutter.frontend_type == 'js' -%}
# Web directory for custom UI
WEB_DIRECTORY = "./web"
{%- endif %}

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    {% if cookiecutter.frontend_type == 'js' -%}
    "WEB_DIRECTORY",
    {%- endif %}
]
