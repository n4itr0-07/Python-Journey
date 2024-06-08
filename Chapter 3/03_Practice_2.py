#TODO: Write a program to check if a list contains a palindrome of elements (Hint: use copy() method).

# [1, 2, 3, 2, 1]        [2, "abc", "abc", 1]

list1 = [1, 2, 1]
list2 = [1, 2, 3]



copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")

else:
    print("NOT Palindrome")
