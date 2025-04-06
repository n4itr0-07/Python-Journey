#TODO Writing to a File
# ---------------------------

# Opening a file in write mode
file = open("C:\\Code Repos\\Learning Python\\Python-Journey\\Chapter 16\\write.txt", "w") # file name is sample.txt and mode is write


# Writing to the file
file.write("Hello World!") # write "Hello World!" to the file

print("File Created!") # print "File Created!" to the console

# Closing the file
file.close() # close the file

# The file is now closed and cannot be used until it is opened again.
# The file is now created and contains the text "Hello World!"

#To read the file again, we need to open it in read mode again.
file = open("C:\\Code Repos\\Learning Python\\Python-Journey\\Chapter 16\\write.txt", "r") # file name is sample.txt and mode is read

content = file.read() # read the contents of the file

print(content) # print the contents of the file