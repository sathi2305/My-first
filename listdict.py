# Program: Demonstrating List, Tuple, and Dictionary in Python

# ---------- LIST ----------
print("=== LIST EXAMPLE ===")
students = ["Alice", "Bob", "Charlie"]

print("Original list:", students)

# Add elements
students.append("David")
print("After append:", students)

# Access elements
print("First student:", students[0])

# Modify elements
students[1] = "Bobby"
print("After modification:", students)

# Remove elements
students.remove("Charlie")
print("After removal:", students)


# ---------- TUPLE ----------
print("\n=== TUPLE EXAMPLE ===")
marks = (85, 90, 75, 92)

print("Marks tuple:", marks)
print("First mark:", marks[0])
print("Total subjects:", len(marks))
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))

# Tuples are immutable — the line below would cause an error if uncommented
# marks[0] = 100


# ---------- DICTIONARY ----------
print("\n=== DICTIONARY EXAMPLE ===")
student_info = {
    "name": "Alice",
    "age": 20,
    "marks": [85, 90, 75],
    "course": "BCA"
}

print("Student info:", student_info)

# Access value
print("Name:", student_info["name"])

# Add new key-value pair
student_info["city"] = "New York"
print("After adding city:", student_info)

# Modify value
student_info["marks"].append(95)
print("After adding new mark:", student_info)

# Loop through dictionary
for key, value in student_info.items():
    print(f"{key}: {value}")
