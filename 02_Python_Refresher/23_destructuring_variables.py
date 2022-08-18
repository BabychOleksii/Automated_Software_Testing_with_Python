t = 5, 11
x, y = t

print(f"x = {x}, y = {y}")

# ============================

student_attendance = {"Rolf": 96, "Adam": 80, "Ann": 100}

list(student_attendance.items())

for elem in student_attendance.items():
    print(elem)

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# ============================

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]
for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")

# ============================

person = ("Bob", 42, "Mechanic")
name, _, profession = person
print((f"Name: {name}, Profession: {profession}"))

# ============================

list = [1, 2, 3, 4, 5]

head, *tail = list
print(f"head: {head}, tail: {tail}")

*head2, tail2 = list
print(f"head: {head2}, tail: {tail2}")

