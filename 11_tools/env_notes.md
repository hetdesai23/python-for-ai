# Environment Variables & Secrets

## Why
API keys and other secrets should never be hard-coded in your source files
(and never committed to Git) — otherwise anyone with the code can read them.

## Environment variables
Values set outside your code, in the operating system/shell, that your
program can read at runtime.

```bash
export OPENAI_API_KEY="sk-..."   # macOS/Linux
```

```python
import os
key = os.environ.get("OPENAI_API_KEY")
```

## .env files — the easy way
A `.env` file stores key=value pairs locally, loaded with `python-dotenv`.

`.env` (never committed — see `.gitignore`):
```
OPENAI_API_KEY=sk-your-key-here
DEBUG=True
```

```python
from dotenv import load_dotenv
import os

load_dotenv()  # reads .env into the environment
api_key = os.environ.get("OPENAI_API_KEY")
```

## Rule
`.env` goes in `.gitignore`. Commit a `.env.example` instead, with the
variable names but no real values, so others know what's needed.
