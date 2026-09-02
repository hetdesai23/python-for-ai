"""Operators: arithmetic, comparison, logical, assignment."""

# Comparison operators
print(7 > 5, 7 < 5, 7 == 5, 7 != 5, 7 >= 7, 7 <= 6)

# Logical operators combine conditions
age = 22
has_id = True
print(age >= 18 and has_id)   # both must be True
print(age < 18 or has_id)     # at least one True

# Augmented assignment operators
count = 0
count += 1   # same as count = count + 1
count *= 3
print(count)  # 3

# Chained comparisons
score = 85
print(60 <= score <= 100)  # True — reads naturally like math

# Operator precedence: * and / before + and -
result = 2 + 3 * 4   # 14, not 20
print(result)
