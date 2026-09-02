"""Numbers: int, float, and basic math."""

# Integers and floats
whole = 10
decimal = 3.14

print(type(whole))    # <class 'int'>
print(type(decimal))  # <class 'float'>

# Arithmetic operators
print(10 + 3)   # addition -> 13
print(10 - 3)   # subtraction -> 7
print(10 * 3)   # multiplication -> 30
print(10 / 3)   # true division -> 3.333...
print(10 // 3)  # floor division -> 3
print(10 % 3)   # modulo (remainder) -> 1
print(10 ** 2)  # exponent -> 100

# Type conversion
age_str = "25"
age_int = int(age_str)
price_float = float("19.99")
print(age_int + 1, price_float * 2)

# Rounding
print(round(3.14159, 2))  # 3.14

# Useful built-ins
numbers = [4, 8, 15, 16, 23, 42]
print(sum(numbers), min(numbers), max(numbers))
