"""If statements: making decisions in code."""

temperature = 28

if temperature > 30:
    print("It's hot")
elif temperature > 20:
    print("It's warm")
else:
    print("It's cold")

# Nested conditions
user_role = "admin"
is_logged_in = True

if is_logged_in:
    if user_role == "admin":
        print("Welcome, admin — full access")
    else:
        print("Welcome — limited access")
else:
    print("Please log in")

# Ternary (conditional) expression — a compact if/else for simple cases
age = 17
status = "adult" if age >= 18 else "minor"
print(status)

# Combining conditions with and/or
score = 78
attendance = 90
if score >= 70 and attendance >= 80:
    print("Pass")
else:
    print("Needs improvement")
