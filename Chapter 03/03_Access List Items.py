
#TODO: List items are indexed and you can access them by referring to the index number:

# Print the second item of the below List.

list = ["apple", "banana", "cherry"]
print(list[1])

#TODO: Lists can contain different types of data, such as numbers, strings, and even other lists:

# Create a List containing mixed data types.

mixed_list = ["apple", 123, "banana", [456, 789]]
print(mixed_list[3])

#TODO: Lists are mutable, meaning you can change their elements after they are created:

# Modify the second item of the List.

list[1] = "orange"
print(list)

#FIXME: Note: The first item has index 0.

"""                                                 Negative index
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.
"""

print(list[-1])  # Output: orange
print(list[-2])  # Output: banana


"""                       Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items."""

print(list[0:2])  # Output: ['apple', 'banana']
print(list[1:])  # Output: ['banana', 'cherry']
print(list[:2])  # Output: ['apple', 'banana']

#FIXME: Part 2 of question below

"""
Create a list containing 10 elements. Write a program to print the last three elements of the list.
"""

list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

print(list[-3:])  # Output: ['kiwi', 'lemon', 'grape']

#TODO: To determine if a specified item is present in a list use the in keyword:

thislist = ["Bat", "Ball", "Kit", "Kitchen"]

if "Ball" in thislist:

    print("Yes, 'Ball' is present in the list")

else:
    print("No, 'Ball' is not present in the list")

#FIXME: Part 3 of question below

"""
 Write a program to create a list containing 10 elements. Write a program to print the first three elements of the list.
"""
list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
print(list[:3])  # Output: ['apple', 'banana', 'cherry']