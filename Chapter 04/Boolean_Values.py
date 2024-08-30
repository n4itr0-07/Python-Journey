
#TODO: Booleans represent one of two values: True or False.

# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# When you run a condition in an if statement, Python returns True or False:

a = 200
b = 33

if(b > a):
    print("b is greater than a")

else:
    print("b is not greater than a")


#TODO: The bool() function allows you to evaluate any value, and give you True or False in return,

print(bool("Hello"))

print(bool(15))

print(bool(0))

#FIXME: Evaluate two variables :

x = "salik"
y = 15

print(bool(x))
print(bool(y))

#TODO: Print the type of the variables x and y.
print(type(x))
print(type(y))

#TODO: In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})