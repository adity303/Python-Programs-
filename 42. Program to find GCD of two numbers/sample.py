# Program to find GCD of two numbers 
import math # Importing module name math 

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd = math.gcd(num1, num2) # Calculating gcd value of the two numbers 
print("GCD of", num1, "and", num2, "is", gcd)