

class Student:
    college_name = "BGSBU"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome Student,", self.name)

s1 = Student("Salik", 100)
s1.welcome()
