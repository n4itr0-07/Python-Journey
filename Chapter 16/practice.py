with open("C:\\Code Repos\\Learning Python\\Python-Journey\\Chapter 16\\practice.md", "w") as file:
    
    # taking content of file as a input
    content = input("Enter the content of the file: ")
    # writing the content to file
    file.write(content)

# reading the content of file
file = open("C:\\Code Repos\\Learning Python\\Python-Journey\\Chapter 16\\practice.md", "r")
# reading the file line by line
for line in file:
    print(line)
    