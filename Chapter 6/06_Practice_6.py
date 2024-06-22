
#TODO: Write a recursive function to print all the elements in a list (Hint : use list & index as parameters.)

def print_list(list, index=0):
    if (index == len(list)):
        return
    print(list[index])
    print_list(list, index + 1)

fruits = ["apple", "banana", "Orange"]
print_list(fruits)