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

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
squared_evens = list(map(lambda x: x * x, even_numbers))
sum_squares = sum(squared_evens)
print("Even Numbers:", even_numbers)
print("Sum of Squared Evens:", sum_squares)
