# Week 2 — File handling and exception handling
from pathlib import Path

file_path = Path(__file__).with_name("practice_notes.txt")

try:
    file_path.write_text("Week 2 practice\nPython files are useful.\n", encoding="utf-8")
    contents = file_path.read_text(encoding="utf-8")
    print(contents)
except OSError as error:
    print("File operation failed:", error)

try:
    value = float(input("Enter a number to divide 100 by: "))
    print("Answer:", 100 / value)
except ValueError:
    print("That was not a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
