class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method.")


# Creating an object, the example of ClassTest
test = ClassTest()

# Calling the instance_method (var.1).  @instance_method get the object as an argument.
test.instance_method()
#  or Calling the instance_method (var.2)
ClassTest.instance_method(test)

# Calling the class_method. @classmethod get the class as an argument.
ClassTest.class_method()

# Calling the static_method. @staticmethod doesn't need any argument.
ClassTest.static_method()


# ==================== Example ================================================
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


book = Book("Harry Potter", "hardcover", 1500)
book2 = Book.hardcover("Lord of the Rings", 1600)
book3 = Book.paperback("Ready player 1", 900)

print(book.name)
print(book)
print(book2)
print(book3)
