# Sets ---> Mutable

# sets elements --> Immutable

collection = set()

collection.add(10)

collection.add(20)          # --> Add Methods.

collection.add(30)

collection.add("Modi 🤡")  # --> String value

collection.add((1, 2, 3, 4))  # --> Tuple value

#TODO: collection.add([1, 2, 3, 4]) # --> List value but in set we can not add list value it will show error.

collection.remove(10)  # --> Remove Method.

collection.clear() # --> Clear Method.

print(collection)

print(len(collection))

#TODO: For POP Method Check Below Code :-

set = {"Delhi", "world", "Coding", "Python"}

print(set.pop()) # POP Method.

#TODO: For Union Method Check Below Code :-

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2)) # Union Method.

#TODO: For Intersection Method Check Below Code :-

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.intersection(set2)) # Intersection Method.