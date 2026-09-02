"""Strings: creation, formatting, and common methods."""

# Creating strings
single = 'hello'
double = "hello"
multiline = """This spans
multiple lines."""

# f-strings (preferred way to build strings with variables)
name = "Trainee"
score = 95
print(f"{name} scored {score}%")

# String methods
text = "  Python for AI  "
print(text.strip())        # remove leading/trailing whitespace
print(text.lower())
print(text.upper())
print(text.strip().replace("AI", "Machine Learning"))

# Splitting and joining
csv_line = "name,age,city"
fields = csv_line.split(",")
print(fields)                      # ['name', 'age', 'city']
print("-".join(fields))            # 'name-age-city'

# Slicing
message = "Hello, World!"
print(message[0:5])    # 'Hello'
print(message[7:])     # 'World!'
print(message[::-1])   # reversed string

# Checking content
email = "trainee@example.com"
print(email.endswith(".com"))
print("@" in email)

# Length
print(len(message))
