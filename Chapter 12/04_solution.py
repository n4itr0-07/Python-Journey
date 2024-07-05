import math

def circle_stats(radius):
    print("hi") #TODO: but this will be printed .

    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

    print("hi")  #TODO: this print statement will never be printed because we use return value in upper line this is when we use return value in upper line 

a, c = circle_stats(3)

print("Area:", a, "circumference:", c)