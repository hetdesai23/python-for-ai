"""Loops: for and while, plus break/continue."""

# for loop over a range
for i in range(5):
    print(i)  # 0 1 2 3 4

# for loop over a list
topics = ["variables", "loops", "functions", "classes"]
for topic in topics:
    print(f"Learned: {topic}")

# enumerate — get index + value together
for index, topic in enumerate(topics):
    print(index, topic)

# while loop — repeats while a condition is True
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    print(f"Attempt {attempts + 1}")
    attempts += 1

# break — exit the loop early
for number in range(10):
    if number == 5:
        break
    print(number)  # prints 0-4, then stops

# continue — skip to the next iteration
for number in range(6):
    if number % 2 == 0:
        continue  # skip even numbers
    print(number)  # prints 1, 3, 5

# Nested loops
for row in range(3):
    for col in range(3):
        print(f"({row},{col})", end=" ")
    print()
