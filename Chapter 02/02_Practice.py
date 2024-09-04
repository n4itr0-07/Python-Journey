
#TODO: Quiz Question 

number = 5

if (number == 5):
    number += 1
    print("1")

if (number == 6):
    print("2")

else:
    print("3")


score = 0

# Question 1
print("1. What will be the output of the following code?")
print("""
for i in range(1, 5):
    print(i * '*')
""")
answer = input("a) *\n   **\n   ***\n   ****\nb) *\n   **\n   ***\n   ****\n   *****\nc) Error\nd) None of the above\n")
if answer.lower() == 'a':
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is a).\n")




# Question 2
print("2. What will be the value of 'sum' after the following code runs?")
print("""
sum = 0
for i in range(1, 4):
    sum += i
""")
answer = input("a) 3\nb) 6\nc) 10\nd) 1\n")
if answer.lower() == 'b':
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is b).\n")
