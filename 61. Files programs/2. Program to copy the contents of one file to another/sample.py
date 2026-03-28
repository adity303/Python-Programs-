# Program to copy contents of one file to another 
# Make source file for read mode
source = open("source.txt", "r")

# Make destination file for write mode
destination = open("destination.txt", "w")

# Copy contents of source to destination
content = source.read() 
#  Write contents from source file
destination.write(content)

# Close both files
source.close()
destination.close()

print("Files copied successfully!!")


# 2nd method is doing with statement 
with open("source.txt", "r") as source:
    content = source.read()
    with open("destination.txt", "w") as destination:
        destination.write(content)

print("Files copied successfully!!")