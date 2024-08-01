class Student:
    college_name = "BGSBU"
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("Adding new student")

s1 = Student("Salik", 97)
print(s1.name, s1.marks)

s2 = Student("Atif", 98)
print(s2.name, s2.marks)
print(s2.college_name)