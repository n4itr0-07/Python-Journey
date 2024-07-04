number = int(input("Enter Your Factorial →"))

factorial = 1
original_number = number

while number > 0:
    factorial *= number
    number -= 1

print(f"The Factorial of", original_number, "is", factorial)