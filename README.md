# Python for AI — Course Notes & Code

Personal notes and practice code from the **Complete Python for AI** course
(free beginner course by Datalumina).

- Course handbook: https://python.datalumina.com
- YouTube video: https://youtu.be/ygXn5nV5qFc

This repo is my own working-through of the course — every folder is a module,
and every module has runnable `.py` files with example code plus short notes
on what I learned. I'm keeping this as a permanent reference and as proof of
practical Python fundamentals for my AI/ML learning path.

## How this is organized

| Folder | Topic |
|---|---|
| `01_getting_started` | Environment setup, virtual environments, pip, interactive Python |
| `02_basics` | Syntax, variables, comments, errors |
| `03_data_types` | Numbers, strings, booleans, operators |
| `04_control_flow` | If statements, loops |
| `05_data_structures` | Lists, dictionaries, tuples, sets |
| `06_functions` | Defining functions, parameters, return values |
| `07_libraries_apis` | Importing packages, calling APIs, working with data |
| `08_practical_python` | Project structure, working with files, organizing code |
| `09_error_handling` | try/except, common errors |
| `10_classes` | Classes, attributes, methods, inheritance |
| `11_tools` | Git & GitHub, environment variables/.env, Ruff, uv |

## Running the code

Each `.py` file is standalone and runnable on its own:

```bash
python 03_data_types/strings.py
```

Some files in `07_libraries_apis` need packages from `07_libraries_apis/requirements.txt`:

```bash
pip install -r 07_libraries_apis/requirements.txt
```

## Status

Working through the course module by module. See each folder's notes for
what's covered and what I still want to practice more.
