"""Tuples: ordered, IMMUTABLE collections."""

point = (10, 20)
print(point[0], point[1])

# Tuples can't be modified after creation
# point[0] = 5  # this would raise a TypeError

# Unpacking — a very common and readable pattern
x, y = point
print(f"x={x}, y={y}")

# Tuples are often used for functions that return multiple values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 8, 15, 16, 23, 42])
print(low, high)

# Single-item tuple needs a trailing comma
single = (1,)
print(type(single))  # <class 'tuple'>

# When to use a tuple vs a list:
# - list: a collection that will change (add/remove/reorder items)
# - tuple: a fixed collection, e.g. coordinates, RGB values, a returned pair
