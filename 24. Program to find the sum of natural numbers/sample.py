# Program to find the sum of the natural numbers 
num = int(input("Enter the number here"))

if num < 0: # Logic1 = If number is already less than 0 then it will not accept 
    print("Please enter positive number")
else: 
    sum = 0 # Initialize the sum to 0 for storing the sum of the natural numbers after calculations. 
    while num>0:
        sum += num
        num -= 1 # Number will decrement (for eg - 3 = for 3 it will be 3+2+1 = 6)
    print(sum) # Printing sum 