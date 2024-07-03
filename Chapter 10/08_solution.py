password = input("Enter Your Password ->")

if len(password) < 6:
    strength = "Weak"
    print("Password is too short. It should have at least 6 characters.")

elif len(password) <= 10:
    strength = "Moderate"
    print("Password is moderately strong.")

else:
    strength = "Strong"
    print("Password is strong.")
    
print("Password Strength: ", strength)