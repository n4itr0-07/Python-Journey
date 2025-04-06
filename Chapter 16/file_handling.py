"""
File - is the collection of data
# File Handling - is the process of opening, reading, writing and closing a file.
# File Handling is important because it allows us to store and retrieve data in a persistent way.
"""

#TODO File Handling in Python
# ---------------------------
# Python provides built-in functions to handle files.
# The most common functions are:
# open() - to open a file
# read() - to read a file
# write() - to write to a file
# close() - to close a file
# The open() function takes two arguments:
# the file name and the mode in which to open the file.
# The mode can be:
# 'r' - read (default mode)
# 'w' - write (overwrites the file if it exists, creates a new file if it doesn't exist)
# 'a' - append (adds to the end of the file)
# 'b' - binary (used for binary files)
# 't' - text (default mode, used for text files)
# 'x' - exclusive creation (fails if the file already exists)


#TODO File Handling Example
# ---------------------------
# Opening a file in read mode
file = open("C:\\Code Repos\\Learning Python\\Python-Journey\\Chapter 16\\file_handling.md", "r") # file name is sample.txt and mode is read

# Reading the contents of the file
content = file.read() # read the contents of the file
# content = file.read(10) # read the first 10 characters of the file
# content = file.readline() # read the first line of the file

# Printing the contents of the file
print(content) # print the contents of the file

# Closing the file
file.close() # close the file
# The file is now closed and cannot be used until it is opened again.


