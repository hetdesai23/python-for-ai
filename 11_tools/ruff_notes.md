# Formatting & Linting with Ruff

Ruff is a fast Python linter + formatter (replaces older tools like
flake8/black/isort in one package).

## Install
```bash
pip install ruff
```

## Usage
```bash
ruff format .     # auto-format all files in the project
ruff check .       # lint — find unused imports, style issues, likely bugs
ruff check --fix .  # auto-fix what it safely can
```

## Why it matters
Consistent formatting makes code easier to read (for you and for teammates),
and a linter catches mistakes (like unused variables or imports) before they
become bugs. Set it to run on save in VS Code with the Ruff extension.
