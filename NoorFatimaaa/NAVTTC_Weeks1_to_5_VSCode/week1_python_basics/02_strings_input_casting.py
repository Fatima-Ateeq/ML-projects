# Week 1 — Strings, input, and type casting

first_name = input("Enter your first name: ").strip()
age_text = input("Enter your age: ").strip()

try:
    age = int(age_text)
    print(f"Hello, {first_name.title()}!")
    print(f"Next year you will be {age + 1}.")
except ValueError:
    print("Please enter your age as a whole number, such as 25.")
