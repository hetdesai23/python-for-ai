"""
Working with data returned from an API — filtering, transforming,
and summarizing it with plain Python (no pandas needed for basics).
"""

# Pretend this came from an API's JSON response
repos = [
    {"name": "ai-agent", "language": "Python", "stars": 120},
    {"name": "web-app", "language": "JavaScript", "stars": 45},
    {"name": "ml-pipeline", "language": "Python", "stars": 300},
    {"name": "cli-tool", "language": "Go", "stars": 12},
]

# Filtering — list comprehension with a condition
python_repos = [r for r in repos if r["language"] == "Python"]
print(python_repos)

# Transforming — pull out just what you need
names_and_stars = [(r["name"], r["stars"]) for r in repos]
print(names_and_stars)

# Sorting by a field
most_popular = sorted(repos, key=lambda r: r["stars"], reverse=True)
print(most_popular[0]["name"])

# Aggregating
total_stars = sum(r["stars"] for r in repos)
average_stars = total_stars / len(repos)
print(f"Total: {total_stars}, Average: {average_stars:.1f}")

# Grouping by a key (without pandas)
by_language = {}
for repo in repos:
    by_language.setdefault(repo["language"], []).append(repo["name"])
print(by_language)
