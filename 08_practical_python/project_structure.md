# Project Structure

A clean, real-world Python project layout (roughly what this repo follows):

```
my_project/
├── .venv/              # virtual environment (not committed — see .gitignore)
├── .env                # secrets, API keys (not committed)
├── .gitignore
├── requirements.txt    # or pyproject.toml with uv
├── README.md
├── src/
│   ├── main.py
│   └── utils.py
└── tests/
    └── test_utils.py
```

## Why structure matters
- Keeps code discoverable — anyone (including future you) can find things.
- Separates config/secrets from code.
- Makes a project runnable and installable, not just a folder of scripts.

## Python paths
Python looks for modules in: the current script's directory, installed
packages, and any directories listed in `PYTHONPATH`. This is why imports
between your own files can break if the project isn't structured/run
consistently — always run scripts from the project root when possible.
