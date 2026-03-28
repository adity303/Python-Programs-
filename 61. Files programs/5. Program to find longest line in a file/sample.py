# Program to find longest line in a File
with open("example.txt", "r") as file:
    # initialize longest line that will calculate the longest line in a file
    longest_line = "" 
    
    for line in file:
        # Applying the condition - if length of line is greater than length of longest line then
        # the value of longest line will be equivalent to its line value. 
        if len(line) > len(longest_line):
            longest_line = line
            
print("longest line is:")
print(longest_line)
print("length:", len(longest_line))

# For example 
# 1. Programming - 11 
# 2. Length of programming - 19
# 19 > 11 so the longest line would be - length of programming 