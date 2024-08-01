
#TODO: Write  a Recursive function to print the sum of first n natural numbers.

def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(20)
print(sum)