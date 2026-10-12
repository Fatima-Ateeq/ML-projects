# Week 1 — Python data structures

# List: ordered and changeable
skills = ["Python", "Pandas", "Machine Learning"]
skills.append("NumPy")
print("List:", skills)
print("First skill:", skills[0])

# Tuple: ordered and not changeable
coordinates = (31.52, 74.35)
print("Tuple:", coordinates)

# Set: unique values
scores = {80, 90, 80, 75}
print("Set (duplicates removed):", scores)

# Dictionary: key-value pairs
student = {"name": "Ayesha", "course": "AI/ML", "week": 1}
student["week"] = 2
print("Dictionary:", student)
print("Student name:", student["name"])
