"""Lists: ordered, mutable collections."""

skills = ["Python", "Git", "APIs"]
print(skills)

# Indexing and slicing
print(skills[0])     # 'Python'
print(skills[-1])    # 'APIs' (last item)
print(skills[0:2])   # ['Python', 'Git']

# Modifying lists
skills.append("Pandas")        # add to the end
skills.insert(1, "VS Code")    # add at a specific position
skills.remove("Git")           # remove by value
last = skills.pop()            # remove and return the last item
print(skills, "| removed:", last)

# Looping through a list
for skill in skills:
    print(f"- {skill}")

# Checking membership
print("Python" in skills)

# Sorting
scores = [88, 42, 97, 61]
scores.sort()
print(scores)                     # ascending
print(sorted(scores, reverse=True))  # descending, returns a new list

# List comprehensions — a compact way to build a new list from another
squares = [n ** 2 for n in range(6)]
print(squares)

even_only = [n for n in range(20) if n % 2 == 0]
print(even_only)

# Length and useful built-ins
print(len(skills))
