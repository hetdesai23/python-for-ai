"""Booleans: True/False and truthiness."""

is_ready = True
is_finished = False

# Comparison operators return booleans
print(5 > 3)      # True
print(5 == 5)     # True
print(5 != 3)     # True

# Boolean/logical operators
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# "Truthiness" — non-boolean values Python treats as True/False
print(bool(0))        # False
print(bool(1))         # True
print(bool(""))        # False (empty string)
print(bool("text"))    # True
print(bool([]))        # False (empty list)
print(bool([1, 2]))    # True
print(bool(None))      # False

# Common pattern: checking if a value exists before using it
user_input = ""
if user_input:
    print("Got input:", user_input)
else:
    print("No input provided")
