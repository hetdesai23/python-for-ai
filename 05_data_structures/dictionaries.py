"""Dictionaries: key-value pairs."""

student = {
    "name": "Ada",
    "age": 25,
    "track": "AI/ML",
}

# Accessing values
print(student["name"])
print(student.get("email"))            # None (key doesn't exist, no error)
print(student.get("email", "n/a"))     # default value if missing

# Adding / updating
student["email"] = "ada@example.com"
student["age"] = 26
print(student)

# Removing
del student["age"]
print(student)

# Looping through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

# Checking membership (checks keys by default)
print("name" in student)

# Nested dictionaries — common shape for API responses / JSON
api_response = {
    "status": "ok",
    "data": {
        "user": {"id": 1, "name": "Ada"},
        "items": [1, 2, 3],
    },
}
print(api_response["data"]["user"]["name"])

# Dict comprehension
squares_by_number = {n: n ** 2 for n in range(5)}
print(squares_by_number)
