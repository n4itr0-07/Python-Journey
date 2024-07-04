while True:
    number = int(input("Enter value b/w 1 to 10 : "))

    if number >= 1 and number <= 10:
        print("Valid input!")
        break
    else:
        print("Invalid input. Please enter a value b/w 1 to 10.")
