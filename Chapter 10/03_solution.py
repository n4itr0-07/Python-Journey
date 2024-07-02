marks = int(input("Enter Your Marks ->"))

if(marks >= 90 and marks <= 100):
    grade = "A"
    print("A Grade Congratulations !")

elif(marks >= 80 and marks < 90):
    grade = "B"
    print("B Grade Congratulations !")

elif(marks >= 70 and marks < 80):
    grade = "C"
    print("C Grade Congratulations !")

elif(marks >= 60 and marks < 70):
    grade = "D"
    print("D Grade Congratulations !")

elif(marks >= 60 and marks <= 50):

    grade = "F"
    print("F Grade Congratulations !")

else:
    print("Invalid Marks")