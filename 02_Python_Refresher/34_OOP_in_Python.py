class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (90, 90, 93, 78, 90)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student()

print(student.average_grade())

# ====================================================


class NewStudent:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


newstudent1 = NewStudent("Alex", (100, 100, 93, 78, 90))
newstudent2 = NewStudent("Max", (90, 90, 95, 78, 90))

print(newstudent1.average_grade())
print(newstudent2.average_grade())

