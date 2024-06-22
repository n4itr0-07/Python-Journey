
#TODO: Write a program to the factorial of n. (n is the parameter)

n = 5
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(5)