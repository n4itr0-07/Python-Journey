def get_full_name(first_name = "Zahid", last_name = "Mujtaba"): # this is parameter if i stored some value directly in paramters then it will print if when calling function is empty.

    ''' This is a function for printing names'''
    name = f'{first_name} {last_name}'
    print(name)

get_full_name("Mr", "Robot") # If i not entered Mr Robot then it will print default value which is stored in function.
get_full_name() # If i not entered Mr Robot then it will print default value which is stored in function.