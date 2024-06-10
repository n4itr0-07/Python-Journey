#TODO: Dictionary Methods.

student = {
    "name" : "Salik",
    "score" : {
        "chem" : 99,
        "phy" : 99.9,
        "math" : 100
    }
    
}

# #print(len(student.keys))

print(student.keys())   # --> Keys Method

print(student.values()) # --> Values Method

print(student.items())  # --> Items Method

print(student.get("name"))  #--> get Method

student.update({"city" : "Jammu & kashmir"})  # --> update Method