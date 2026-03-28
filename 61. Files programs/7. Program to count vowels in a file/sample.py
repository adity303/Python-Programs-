# Program to count vowels in a file
with open("Count_vowels.txt", "r"):
    content = file.read()
    
vowels = "aeiouAEIOU" # initializing vowels 
count = 0 # initializing count 

for char in content:
    if char in vowels:
        count += 1
        
print("Number of vowels in a file are: ", count)
print("End of program")