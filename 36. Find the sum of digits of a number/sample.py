# Program to find the sum of digit of a number 
n = int(input("Enter a number: "))
sum = 0 # Initialize sum = 0 

while n>0: # do while loop for number(n)
    digit = n%10 # doing modulo expression (64%10 = 4)
    n = n//10 # Removing last digit
    sum = sum + digit # whatever digit come, goes to sum  

print("Sum of digits:", sum)    