with open("C:\Code With Ssn\Learning Python\Python-Journey\Chapter 7\Practice1.txt", "r") as f:
    data = f.read()
    new_data = data.replace("Java", "Python")
    print(new_data)
    # f.write("I am studying Python check my github repo\n")
    # f.write("Thanks for checking my github repo")

with open("C:\Code With Ssn\Learning Python\Python-Journey\Chapter 7\Practice1.txt", "w") as f:
    f.write(new_data)