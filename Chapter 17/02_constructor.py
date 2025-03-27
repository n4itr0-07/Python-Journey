class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

# Creating objects
student1 = Student("Mr Robot", 28, "A++")
student2 = Student("Elliot", 25, "B++")

print(f"Student Name: {student1.name}, age {student1.age}, and Grades: {student1.grades}")
print(student2.name, student1.age, student1.grades)


"""
        Constructor is a special method in Python that is used to initialize the object.
        The constructor is called when the object is created.
        The constructor method is always called __init__.
        The constructor method is optional.
        The constructor method is used to initialize the object.
        The constructor method is called with the class name.

        Types of constructors:
        1. Default Constructor: The constructor with no arguments.
        2. Parameterized Constructor: The constructor with arguments.
        3. Copy Constructor: The constructor that initializes an object with another object.
        4. Private Constructor: The constructor that is private.
        5. Constructor With Default Arguments: The constructor with default arguments.
"""