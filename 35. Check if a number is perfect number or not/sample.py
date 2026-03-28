# Checking number is perfect number or not
# Perfect Number are those number which determines if it is equal to the 
# sum of its proper positive divisors(excluding number itself)

num = int(input("Enter a number:"))
sum = 0 # Initialize sum = 0 
for i in range(1,num):  
    if (num%i == 0): # Condition1 - if number divided by (i=1,2,3,4,5) 
        sum = sum + i # whenever the factor is found it goes to the sum 

if (sum == num): # if sum of factors(excluding number itself) = number 
    print("Number is perfect")
else:
    print("Number is not perfect")