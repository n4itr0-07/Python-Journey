# TODO: Write a program to find the greatest of 3 numbers entered by the user.

a = int(input("Enter first number ->"))
b = int(input("Enter second number ->"))
c = int(input("Enter third number ->"))

if(a >= b and a >= c):
    print("First number is largest", a)

elif(b >= c):
    print("Second number is Largest", b)

else:
    print("Third number is Largest", c)

   