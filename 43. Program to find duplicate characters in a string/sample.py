# Program to find duplicate characters in a string
# To do this we have to first create empty list, then compare of the characters 
string = input("Enter a string: ")

duplicate = [] # Creating an empty lis

for i in string:
    # if string.count(i) > 1 = If character appears more than once 
    # and not in duplicate list = same repetition of the word is not allowed. 
    if string.count(i) > 1 and i not in duplicate:
        # .append = Adds the character to the duplicate list 
        duplicate.append(i)

print("Duplicate characters are:", duplicate)