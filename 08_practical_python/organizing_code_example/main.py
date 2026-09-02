"""
Demonstrates organizing code into separate files/modules instead of one
giant script. Run from this folder with: python main.py
"""

from utils import clean_text, summarize

raw_notes = [
    "  Learned about VARIABLES today  ",
    "Practiced LOOPS and functions",
    "  Built my first API call ",
]

cleaned = [clean_text(note) for note in raw_notes]
print(cleaned)

stats = summarize(cleaned)
print(stats)

if __name__ == "__main__":
    print("This block only runs when the file is executed directly,")
    print("not when it's imported by another file.")
