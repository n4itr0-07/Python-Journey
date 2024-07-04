input_str = str(input("Enter Your String : "))

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Char is : ", char)
        break
       