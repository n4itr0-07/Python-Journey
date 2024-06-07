# marks = int(input("Enter students marks :"))


# if(marks >= 90):
#     grade = "A"
#     #print("A Grade Congratulations !")

# elif(marks >=80 and marks < 90):
#     grade = "B"
#     #print("B Grade Congratulations !")

# elif(marks >=70 and marks <80):
#     grade = "C"
#     #print("C Grade Congratulations !")

# else:
#     grade = "D"
#     print("Grade of the student ->", grade)   

marks = int(input("Enter student's marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

print("Grade of the student ->", grade)

