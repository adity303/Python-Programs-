# Checking for a string whether it is a palindrome or not. 
# Example - eye, malayalam, dad, mom, level, madam
str = input("Enter a string: ")

# Python slice format (start, end, step)
if str == str[::-1]: # (Start is 0, end is 0 but step goes from -1) means it will read from backwards
    print("Palindrome")
else:
    print("Not Palindrome")