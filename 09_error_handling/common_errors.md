# Common Python Errors — Quick Reference

| Error | Typical cause |
|---|---|
| `SyntaxError` | Invalid Python grammar (missing `:`, unmatched bracket) |
| `IndentationError` | Inconsistent spacing/indentation |
| `NameError` | Using a variable/function before it's defined |
| `TypeError` | Wrong type for an operation (e.g. `"5" + 5`) |
| `ValueError` | Right type, wrong value (e.g. `int("abc")`) |
| `IndexError` | List index out of range |
| `KeyError` | Dictionary key doesn't exist |
| `AttributeError` | Calling a method/attribute that doesn't exist on that object |
| `ZeroDivisionError` | Dividing by zero |
| `ImportError` / `ModuleNotFoundError` | Package not installed, or typo in import |
| `FileNotFoundError` | File path doesn't exist |

## My rule of thumb
Catch the *specific* exception you expect, not a bare `except:` — a bare
except hides bugs you actually want to see.
