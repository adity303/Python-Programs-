# Code for compress the string 
# For example - if (aaabb --> a3b2)
text = input("Enter the string")

count = 1 # Assuming that the first character has appeared at least one time. 
result = "" # Empty string to store answer 

for i in range(len(text) -1): # len(text) = This gives length of the string.
    # range(len(text - 1) - calculating range, means if length is 5 then its range is 4 
    if text[i] == text[i+1]: # Looping current character with next iterable character 
        count +=1 
    else:
        result = result + text[i] + str(count)
        count = 1 
result = result + text[-1] + str(count)

print("Compressed String:", result)