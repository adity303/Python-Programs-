# Count the number of digits of a number 
# For eg - 12345 count = 5 
# Using while loop 
num = int(input("Enter a number: "))
count = 0
while num != 0: # Condition1 - num always not equal to 0
    num = num // 10 # Last digit is removed 
    count = count + 1 # Move to next iteration for count 
print("Number of digits:", count)

# Method 2 - Using len keyword 
num = input("Enter a number: ")
print("Number of digits:", len(num))
# len keyword is used to count the number of character(digits) are present