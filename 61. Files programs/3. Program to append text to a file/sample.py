# Program to append text to a file.
file = open("file.txt", "a")

# Enter the text to append in the file
text = input("Enter the text to append:")
file.write(text, "\a")

# Close the file
file.close()

print("File appended successfully!!")