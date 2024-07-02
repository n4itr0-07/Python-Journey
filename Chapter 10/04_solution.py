furits = str(input("Enter Fruits Name ->"))
color = str(input("Enter Your Color ->"))


if furits == "Bannana":
    if color == "green":
        print("unripe")

    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverripeRipe")

else:
    print("Not a Bannana")
    exit()