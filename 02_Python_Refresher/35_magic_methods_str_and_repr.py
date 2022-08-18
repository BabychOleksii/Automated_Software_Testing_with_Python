class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return f"This is the {self.name} object."

    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"

alex = Person("Alex", 40)

print(alex)