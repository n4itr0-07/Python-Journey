#TODO: with keyword: is used to open a file in a context manager. If we forget to close the file, it will be closed automatically. Also it will be closed even if an error occurs.


# Opening a file in read mode using with keyword
file = open("C:\\Code Repos\\Learning Python\\Python-Journey\\Chapter 16\\write.txt", "r") # file name is sample.txt and mode is read

content = file.read() # read the contents of the file

print(content) # print the contents of the file
# The file is now closed and cannot be used until it is opened again.