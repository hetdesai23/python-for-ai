# Getting Started

## What is Python
A high-level, interpreted programming language — good first language and the
dominant language for AI/ML because of its huge ecosystem of libraries.

## Editor: VS Code
Used as the main editor throughout the course. Key extensions: Python,
Pylance, Ruff.

## Virtual environments
A virtual environment is an isolated Python install per-project, so
dependencies for one project don't clash with another.

```bash
# create
python -m venv .venv

# activate (macOS/Linux)
source .venv/bin/activate

# activate (Windows)
.venv\Scripts\activate

# deactivate
deactivate
```

## Packages & pip
`pip` is Python's package installer. Packages are published on PyPI.

```bash
pip install requests
pip install -r requirements.txt
pip freeze > requirements.txt
```

## Interactive Python
Two main ways to run Python interactively while learning/exploring:
- The Python REPL (`python` in a terminal)
- Jupyter-style interactive cells in VS Code using `# %%` cell markers

Interactive mode is great for testing small pieces of code (like API calls
or data exploration) without re-running a whole script.
