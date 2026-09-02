"""Sets: unordered collections of unique items."""

skills_a = {"python", "git", "sql"}
skills_b = {"python", "docker", "sql"}

# Duplicates are automatically removed
tags = {"ai", "ml", "ai", "python"}
print(tags)  # {'ai', 'ml', 'python'}

# Set operations — very useful for comparing two collections
print(skills_a | skills_b)   # union — all items from both
print(skills_a & skills_b)   # intersection — items in both
print(skills_a - skills_b)   # difference — in a, not in b

# Adding/removing
skills_a.add("apis")
skills_a.discard("sql")
print(skills_a)

# Fast membership checks (this is what sets are great for)
print("python" in skills_a)

# Common real use: deduplicate a list while keeping it simple
raw = [1, 2, 2, 3, 3, 3, 4]
unique_values = list(set(raw))
print(unique_values)
