# Program to convert string to uppercase without using upper(). 
sentence = input("Enter a sentence: ")
result = " " # Declare a variable result to store the uppercase letters

for char in sentence:
    if char >= 'a' and char <= 'z': # Checking the condition if character is lowercase. 
        result += chr(ord(char) - 32)
    else:
        result = result + char
        
print("Uppercase String:",result)

# Note -- In ASCII Code, the difference between lowercase and uppercase is 32. 
# For uppercase = 32 - chr(ord(char) - 32)
# chr() converts the ASCII value back to the character. 