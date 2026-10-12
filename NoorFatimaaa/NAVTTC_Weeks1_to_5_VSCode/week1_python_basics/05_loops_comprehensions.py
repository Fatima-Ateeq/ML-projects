# Week 1 — for, while, enumerate, break, continue, and list comprehension

print("for loop:")
for number in range(1, 6):
    print(number)

print("\nenumerate:")
subjects = ["Python", "Statistics", "NumPy"]
for index, subject in enumerate(subjects, start=1):
    print(index, subject)

print("\ncontinue skips 3; break stops at 5:")
for number in range(1, 10):
    if number == 3:
        continue
    if number == 5:
        break
    print(number)

print("\nwhile loop:")
count = 1
while count <= 3:
    print("Count:", count)
    count += 1

squares = [number ** 2 for number in range(1, 6)]
print("List comprehension:", squares)
