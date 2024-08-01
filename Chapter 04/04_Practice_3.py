#FIXME:: Write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & ass one by one. Use subjects name as key & marks as value.

marks = {}

X = int(input("Enter Physics marks ->"))
marks.update({"physics" : X})

X = int(input("Enter Chemistry marks ->"))
marks.update({"Chemistry" : X})

X = int(input("Enter Math marks ->"))
marks.update({"Math" : X})

print(marks)

