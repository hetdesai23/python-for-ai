# Python Syntax & Errors

## Syntax basics
- Indentation defines code blocks (no `{}` like other languages) — 4 spaces
  is the standard.
- Statements don't need semicolons.
- `#` starts a comment.

## Common error types
- **SyntaxError** — code doesn't follow Python's grammar (e.g. missing colon).
- **NameError** — using a variable that doesn't exist yet.
- **TypeError** — using a value in a way its type doesn't support
  (e.g. `"5" + 5`).
- **IndexError** — accessing a list index that doesn't exist.
- **KeyError** — accessing a dictionary key that doesn't exist.
- **ZeroDivisionError** — dividing by zero.

## Reading a traceback
Python tracebacks read bottom-to-top: the last line is the actual error and
error message; the lines above show the call path that led there. Always
read the last line first.

## Formatting
Consistent formatting (spacing, line length, quote style) matters for
readability — this is what tools like **Ruff** automate (see
`11_tools/ruff_notes.md`).
