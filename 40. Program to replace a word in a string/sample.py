# Program to replace a word in a string
# For example - String = chocolate, replace word o with p 
# Result - chpcplate, o is replaced with p
str = input("Enter string: ")
old_word = input("Enter the word you want to replace: ")
new_word = input("Enter the new word")

result = str.replace(old_word, new_word)
print("Updated sentence is: ", result)