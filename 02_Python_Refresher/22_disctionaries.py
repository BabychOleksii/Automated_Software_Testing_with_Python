friend_ages = {"Rolf": 24, "Adam": 30, "Ann": 27}

print(friend_ages["Rolf"])

friend_ages["Bob"] = 25

friend_ages["Ann"] = 26

print(friend_ages)

# ====================================

friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Ann", "age": 27},
]

print(friends[1]["name"])

# ====================================

student_attendance = {"Rolf": 96, "Adam": 80, "Ann": 100}

for student in student_attendance:
    print(student)

for student in student_attendance.items():
    print(student)

for student, attendance in student_attendance.items():
    print(attendance)

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

# ====================================

for student in student_attendance:
    print(student)

for student in student_attendance.items():
    print(student)

for student, attendance in student_attendance.items():
    print(attendance)

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")


if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
elif "Rolf" in student_attendance:
    print(f"Rolf: {student_attendance['Rolf']}")
else:
    print("Bod is not a student")


attendance_values = student_attendance.values()
print(attendance_values)
print(sum(attendance_values) / len(attendance_values))

