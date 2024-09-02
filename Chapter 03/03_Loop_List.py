
#TODO: Loop Through a List
# You can loop through the items by using a for loop:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#TODO: Loop through the Index Numbers:
# You can loop through the list items by referring to their index number.Using the range() and len() functions to create a suitable iterable:

thisList = ["Pumpkin", "Gingerbread", "Cucumber"]

for i in range(len(thislist)):
    print(thisList[i])


#FIXME Using a While loop

#TODO: Use the len() function to determine the length if the list, then start at 0 and loop your way through the list items by referring to their index number. Remember to increment the index number by 1 after each iteration.

List = ["Pumpkin", "Gingerbread", "Cucumber"]
i = 0
while i < len(List):
    print(List[i])
    i += 1



#TODO: Looping Using List Comprehension
# A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]