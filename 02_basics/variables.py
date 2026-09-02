"""
Variables, naming, and comments.

Python is dynamically typed: a variable's type is inferred from the value
you assign to it, and can change if you reassign it.
"""

# Assigning variables
course_name = "Python for AI"
lessons_completed = 12
is_finished = False

print(course_name, lessons_completed, is_finished)

# Reassigning changes the type — Python doesn't care
progress = 50          # int
progress = 50.5        # now a float
progress = "halfway"   # now a string
print(progress)

# Naming conventions (snake_case for variables/functions)
first_name = "Ada"
last_name = "Lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# Multiple assignment
x, y, z = 1, 2, 3
print(x, y, z)

# Constants — Python has no true constants, ALL_CAPS is just a convention
MAX_RETRIES = 3

# This is a single-line comment explaining the next block
# Docstrings (triple-quoted strings) are used for module/function/class docs
