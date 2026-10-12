# Week 1 — if, elif, else, nested condition, ternary expression

try:
    marks = float(input("Enter marks from 0 to 100: "))
    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
    elif marks >= 80:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    else:
        print("Keep practising.")
    result = "Pass" if marks >= 50 else "Needs improvement"
    print("Result:", result)
except ValueError:
    print("Please enter a number.")
