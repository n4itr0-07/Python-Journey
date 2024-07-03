# Take user input for pet type and age
pet_type = input("Enter the type of pet (dog/cat): ").lower()
pet_age = float(input("Enter the age of the pet: "))

# Determine the recommended food based on the pet type and age
if pet_type == 'dog':
    if pet_age < 2:
        recommended_food = "Puppy food"
    else:
        recommended_food = "Adult dog food"
elif pet_type == 'cat':
    if pet_age < 1:
        recommended_food = "Kitten food"
    elif pet_age > 5:
        recommended_food = "Senior cat food"
    else:
        recommended_food = "Adult cat food"
else:
    recommended_food = "Unknown pet type"

# Print the recommended food
print(f"Recommended food: {recommended_food}")
