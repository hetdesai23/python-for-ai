"""Error handling: try/except so one bad input doesn't crash everything."""

# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")

# Catching a specific error type vs a generic one
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' is not a valid number")
        return None


print(safe_int("42"))
print(safe_int("abc"))

# Handling multiple exception types
def get_item(items, index):
    try:
        return items[index]
    except IndexError:
        print("That index doesn't exist")
    except TypeError:
        print("Index must be an integer")


numbers = [1, 2, 3]
get_item(numbers, 10)
get_item(numbers, "a")

# else and finally
def read_config(value):
    try:
        number = int(value)
    except ValueError:
        print("Invalid config value")
    else:
        # runs only if no exception was raised
        print(f"Config loaded: {number}")
    finally:
        # always runs, error or not — good for cleanup
        print("Done checking config")


read_config("10")
read_config("bad")

# Raising your own errors
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount


try:
    withdraw(100, 150)
except ValueError as e:
    print(f"Transaction failed: {e}")
