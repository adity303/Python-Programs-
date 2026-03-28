# Program to count lines in a file 
# First method - Using counter variable and loop 
counter = 0 
with open("myfile.txt", "r") as file:
    for line in file:
        counter = counter + 1
print("Number of lines in the file: ", counter)

# Second method - Using readlines()
with open("myfile.txt", "r") as file:
    lines = len(file.readlines)
print("Number of lines in the file: ", lines)