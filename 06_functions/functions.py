"""Functions: defining, parameters, return values."""


# Basic function
def greet():
    print("Hello!")


greet()


# Parameters
def greet_person(name):
    print(f"Hello, {name}!")


greet_person("Ada")


# Default parameter values
def greet_with_title(name, title="Trainee"):
    print(f"Hello, {title} {name}!")


greet_with_title("Ada")
greet_with_title("Ada", title="Dr.")


# Return values — functions can send data back to the caller
def add(a, b):
    return a + b


total = add(3, 4)
print(total)


# Multiple return values (returned as a tuple)
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


lowest, highest, average = get_stats([4, 8, 15, 16, 23, 42])
print(lowest, highest, average)


# *args and **kwargs — flexible number of arguments
def describe(*skills, **details):
    print("Skills:", skills)
    print("Details:", details)


describe("python", "git", role="AI/ML trainee", months=3)


# Type hints — not enforced by Python, but make intent clear and help
# tools/editors catch mistakes
def calculate_average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)


print(calculate_average([1.0, 2.0, 3.0]))


# Docstrings — document what a function does
def is_even(number: int) -> bool:
    """Return True if number is even, False otherwise."""
    return number % 2 == 0


print(is_even(4), is_even(5))
