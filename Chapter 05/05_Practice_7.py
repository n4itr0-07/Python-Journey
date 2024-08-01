
#TODO: Search for a number x in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 100, 64, 81, 100]

X = 100
idx = 0

for element in nums:
    if(element == X):
        print("Number found at idx", idx )

    idx += 1