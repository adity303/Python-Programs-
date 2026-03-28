# Program to find the second largest number in a list
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

max1 = float('-inf') # Negative integer number not allowed 
max2 = float('-inf')

for n in numbers:
    if n > max1:
        max2 = max1
        max1 = n
    elif n > max2 and n != max1:
        max2 = n

print("Second largest number is:", max2)
