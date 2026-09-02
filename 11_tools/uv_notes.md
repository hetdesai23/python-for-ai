# Modern Python with uv

`uv` is a fast, modern replacement for `pip` + `venv`, written in Rust.
It manages virtual environments, dependencies, and even Python versions
themselves.

## Why uv over pip + venv
- Much faster installs.
- One tool instead of juggling `venv`, `pip`, and `pip-tools`.
- Locks dependencies automatically for reproducible environments.

## Basic workflow
```bash
# install uv (see https://docs.astral.sh/uv for the current install command)

uv init my-project        # create a new project with pyproject.toml
cd my-project

uv add requests            # add a dependency (creates/updates .venv)
uv add --dev ruff          # add a dev-only dependency

uv run main.py              # run a script inside the project's environment

uv sync                     # install everything from the lockfile
```

## Complete setup (start to finish)
```bash
uv init ai-project
cd ai-project
uv add requests python-dotenv
uv run main.py
```

This replaces the older `python -m venv .venv` + `pip install -r
requirements.txt` workflow with a single tool and a lockfile
(`uv.lock`) that guarantees everyone gets the exact same dependency
versions.
