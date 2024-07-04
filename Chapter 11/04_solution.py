input_str = str(input("Enter Your String : "))

reverse_str = ""

for char in input_str:
    reverse_str = char + reverse_str

print("Reversed String : ", reverse_str)