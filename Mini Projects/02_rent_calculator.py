
#TODO: Input we need from the user

# Total rent
# Total foos ordered for snacking
# Electricity units spend
# Charge per Unit 
# Persons living in room/flat

#TODO: Output

# TOtal amount you've to pay is

rent = int(input("Enter your hostel/flat rent :--> "))

food = int(input("Enter the amount of food ordered :--> "))

electricity = int(input("Enter the electricity units used :--> "))

charge_per_unit = int(input("Enter the charge per unit :--> "))

people = int(input("Enter the number of people living in the room/flat :--> "))

total_amount = (electricity * charge_per_unit)

output = (food + rent + total_amount) // people 

print("Total amount you've to pay is :--> ", output)