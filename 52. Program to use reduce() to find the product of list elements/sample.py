# Program to use reduce to find the product of list elements 
from functools import reduce # For this we have to use reduce module 
numbers = [1,2,3,4,5] 

product = reduce(lambda x, y: x * y, numbers)
print("Product of two numbers is:", product)
