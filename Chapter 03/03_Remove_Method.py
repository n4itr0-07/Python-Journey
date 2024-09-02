
#TODO: The remove() method removes the specified item.

# Remove Banana

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


#TODO: If there are more than one item with the specified value, the remove() method removes the first occurrence:

thislists = ["apple", "banana", "cherry","banana"]

# Remove Banana at index 1
thislists.remove("banana")
print(thislists)


#TODO: The pop() method removes the specified index.

thislist1 = ["apple", "banana", "cherry"]
thislist1.pop(1)
print(thislist1)

# If you do not specify the index, the pop() method removes the last item.
thislist1 = ["apple", "banana", "cherry"]
thislist1.pop()
print(thislist1)


#TODO: The del keyword also removes the specified index

thislist3 = ["apple", "banana", "cherry"]
del thislist3[1]
print(thislist3)

# The del keyword can also delete the entire list

thislist4 = ["apple", "banana", "cherry"]
del thislist4
print(thislist4) # This will raise an error because "thislist4" no longer exists.


#TODO: The clear() method empites the list. The list still remains, but it has no content.

thislist5 = ["apple", "banana", "cherry"]
thislist5.clear()
print(thislist5)