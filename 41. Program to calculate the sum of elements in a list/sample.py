# Program to calculate the sum of elements in a list 
# Method1 - Using normal method 
numbers = [10,20,30,40,50,60]
sum = 0 # Initialize sum = 0

for num in numbers:
    sum = sum + num # Calculates the sum with numbers present in the list
print(sum)

# Using built-in function 
numbers = [10, 20, 30, 40, 50]
print("Sum of elements:", sum(numbers))