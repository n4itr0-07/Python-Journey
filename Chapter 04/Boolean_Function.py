
# TODO: You can create functions that returns a Boolean Value:
class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()

  
print(bool(myobj))

#TODO: You can execute code based on the Boolean answer of a function:
def myFunction():
    return True

if myFunction():
    print("YES!")

else:
    print("NO!")

#TODO: Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

x = 200

print(isinstance(x, int))