# def add (a, b):
#     return a + b

# add (3, 4)
# #TODO: Lambda function
# (lambda a, b : a + b) (3, 6)


# def larger (a, b):
#     if a < b:
#         return b
#     else:
#         return a
    
# larger (3, 4)
# print ("larger")

# def even(li):
#     for i in li:
#         if i % 2 == 0:
#             print(i)

# inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even(input)

print(dir(__builtins__))

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")

# What will be the output of this code?