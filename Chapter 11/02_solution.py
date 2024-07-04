n = int(input("Enter Numbers Upto n →"))

sum_even = 0

for i in range(1, n+1):

    if(i % 2 == 0):
        sum_even += i

print("Sum of Even Numbers -> ", sum_even)