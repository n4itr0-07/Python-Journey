"""
Exception rises when code is in run time

Exception Handling?
---------------------------

#TODO: try-except

try - code that you think will throw error
except - if error occured in try what you have to do know
finally - This will always run 
"""
"""
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result : {result}")

except ZeroDivisionError: # Name for that error which is gonna occur
    print("You cannot divide with 0!")

except ValueError:
    print("You cannot divide with string!")

"""

#TODO: Example for finally;

try:
    file = open("C:\Code Repos\Learning Python\Python-Journey\Chapter 16\word.txt", "r") # lets change file name to wrong name (from sample.txt to word.txt)

    content = file.read()
    print(content)

except FileNotFoundError:
    print("File Not Found!!")

finally:
    file.close()
    print("File Operation Completed!")