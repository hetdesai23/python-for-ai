"""Reading, writing, and processing files."""

import json
from pathlib import Path

# Writing a text file
notes_path = Path("notes_output.txt")
notes_path.write_text("Line 1\nLine 2\nLine 3\n")

# Reading a text file — 'with' automatically closes the file when done
with open(notes_path, "r") as f:
    for line in f:
        print(line.strip())

# Appending to a file
with open(notes_path, "a") as f:
    f.write("Line 4\n")

# Working with JSON — the format most APIs and configs use
data = {"course": "Python for AI", "completed": True, "modules": 11}

with open("progress.json", "w") as f:
    json.dump(data, f, indent=2)

with open("progress.json", "r") as f:
    loaded = json.load(f)
print(loaded["modules"])

# Working with CSV (no external library needed for basics)
import csv

rows = [["name", "score"], ["Ada", 95], ["Grace", 88]]
with open("scores.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

with open("scores.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# pathlib for checking/manipulating paths
print(notes_path.exists())
print(notes_path.suffix)     # '.txt'
print(notes_path.stem)       # 'notes_output'

# Clean up the demo files this script created
for f in ["notes_output.txt", "progress.json", "scores.csv"]:
    Path(f).unlink(missing_ok=True)
