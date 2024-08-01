s = {1, 5, 32, "Salik"}

# e = s() # TODO: Don't use s ={} it will create empty dictionary. This method is used to create empty set

# d = {} # TODO: This will create a empty dictionary
# print(type(d))

# print(type(s))

s.add(143)
print(s)

# # TODO: Remove an element from set

# s.remove(5)
# print(s)

# # TODO: Clear all elements from set

# # s.clear()
# # print(s)

# TODO: Check if an element exists in set

print(1 in s) # True
print(10 in s) # False

# TODO: Get the length of set

print(len(s)) # 5

# TODO: Iterate over set

for element in s:
    print(element)

# TODO: Convert set to list

list_s = list(s)
print(list_s)

# TODO: Convert list to set

set_s = set(list_s)
print(set_s)

# TODO: Union of two sets

s1 = {1, 2, 3}
s2 = {3, 4, 5}

union_s = s1.union(s2)
print(union_s)

# TODO: Intersection of two sets

intersection_s = s1.intersection(s2)
print(intersection_s)

# TODO: Difference of two sets

difference_s = s1.difference(s2)
print(difference_s)

# TODO: Symmetric difference of two sets

symmetric_difference_s = s1.symmetric_difference(s2)
print(symmetric_difference_s)

# TODO: Copy a set

copied_s = s1.copy()
print(copied_s)

# TODO: Remove duplicates from set

s.discard(3)
print(s)

s.discard(10) # It will not raise any error if the element is not present in set
print(s)

# s.remove(10) # It will raise an error if the element is not present in set

# TODO: Convert set to tuple

tuple_s = tuple(s)
print(tuple_s)

# TODO: Convert tuple to set

set_tuple = set(tuple_s)
print(set_tuple)

# TODO: Convert set to frozenset

frozenset_s = frozenset(s)
print(frozenset_s)

# TODO: Convert frozenset to set

set_frozenset = set(frozenset_s)
print(set_frozenset)

# TODO: Convert set to dictionary

dict_s = {1: "One", 2: "Two", 3: "Three"}
print(dict_s)

# TODO: Convert dictionary to set

set_dict = set(dict_s.items())
print(set_dict)

# TODO: Convert set to string

string_s = "".join(str(element) for element in s)
print(string_s)