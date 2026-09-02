"""Advanced string manipulation — beyond the basics."""

prompt = "  Summarize This ARTICLE about AI Ethics  "

# Chaining methods
cleaned = prompt.strip().lower()
print(cleaned)  # "summarize this article about ai ethics"

# Counting occurrences
sentence = "the quick brown fox jumps over the lazy dog"
print(sentence.count("the"))  # 2

# Finding a substring's position
print(sentence.find("fox"))   # index where "fox" starts

# Padding / alignment (useful for printing tables)
print("id".ljust(6) + "name".ljust(10))
print(str(1).ljust(6) + "Ada".ljust(10))

# Multiline / templated text with f-strings
template = f"""
Report
------
Rows: {120}
Errors: {0}
"""
print(template)

# startswith / endswith for validation
filenames = ["notes.md", "data.csv", "script.py", "image.png"]
python_files = [f for f in filenames if f.endswith(".py")]
print(python_files)

# Building strings from a list — common when formatting output for a user
items = ["variables", "loops", "functions"]
summary = ", ".join(items[:-1]) + f", and {items[-1]}"
print(f"Today I learned: {summary}")
