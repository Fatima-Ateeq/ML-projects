# Week 2 — Functions, scope, lambda, map, filter, nested functions

def calculate_average(numbers):
    """Return the average of a non-empty list of numbers."""
    if not numbers:
        raise ValueError("Please provide at least one number.")
    return sum(numbers) / len(numbers)

marks = [75, 82, 91, 68]
print("Average:", calculate_average(marks))

course = "AI/ML"  # global variable

def show_course():
    local_message = "Welcome to"
    print(local_message, course)

show_course()

double = lambda number: number * 2
print("Double 5:", double(5))
print("Doubled marks:", list(map(double, marks)))
print("Marks >= 80:", list(filter(lambda mark: mark >= 80, marks)))

def make_greeting(greeting):
    def greet(person):
        return f"{greeting}, {person}!"
    return greet

say_hello = make_greeting("Hello")
print(say_hello("student"))
