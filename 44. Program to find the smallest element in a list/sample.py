# Program to find the smallest element in a list
# Method 1 - Using for loop  
numbers = [23,24,1,65,35,13,16,76]

smallest = numbers[0] # Assume first element is smallest 

for num in numbers: # This loop will check each element in a list 
    if num < smallest: #  If the current number is smaller than the stored value, then it becomes the new smallest value. 
        smallest = num

print("Smallest number from the list is:", smallest)

# Method 2 - Using min() built-in function 
numbers = [23,24,1,65,35,13,16,76]

# min() function directly runs the smallest value in the list. 
print("Smallest number from the list is:", min(numbers))