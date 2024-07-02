distance = int(input("Enter Your Distance Milage ->"))

if distance < 3:
    transport = "Walk"
    print("It's short distance you can walk easily !")

elif distance > 3 and distance <=15:
    transport = "Bike"
    print("It's a moderate distance, you can use bike for a comfortable journey.")

# elif distance > 15 and distance <=25:
#     transport = "Car"
#     print("It's a long distance, you can use car for a comfortable journey.")

# else:
#     print("Prefer as you wish")
#     import sys
#     sys.exit()

else:
    transport = "Car"
    print("It's a long distance, you can use car for a comfortable journey.")

print("You can use", transport, "to cover this distance.")