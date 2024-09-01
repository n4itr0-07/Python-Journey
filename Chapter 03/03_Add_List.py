
"""                                                             Append Method
To add an item to the end of the list, use the append() method:"""

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

"""                                                             Insert Method
To add an item at a specific index in the list, use the insert() method:"""

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

"""                                                             Extend Method
To add multiple items to the end of the list, use the extend() method:"""

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

"""                                                             Copy Method
To make a copy of a list, use the copy() method:"""

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

"""                                                             Clear Method
To remove all items from the list, use the clear() method:"""

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#TODO: Add a new item to the beginning of the list using the insert() method.

thislist = ["apple", "banana", "cherry"]

# Your code here

print(thislist)

#TODO: Add a new item to the end of the list using the append() method.

thislist = ["apple", "banana", "cherry"]

# Your code here

print(thislist)

#TODO: Add multiple new items to the end of the list using the extend() method.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

# Your code here

print(thislist)

#TODO: Make a copy of the list using the copy() method and print the copied list.

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()

print(mylist)

#TODO: Remove all items from the list using the clear() method and print the modified list.

thislist = ["apple", "banana", "cherry"]
thislist.clear()

print(thislist)