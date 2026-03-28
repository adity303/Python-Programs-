# Program to read a file line by line 
with open("rohit.txt", "r") as file: 
    lines = file.readlines()
    
    for line in lines:
        print(line)
        
# 2nd method - Use read file line by line using with 
with open("rohit.txt", "r") as file:
    for line in file:
        print(line)
        
