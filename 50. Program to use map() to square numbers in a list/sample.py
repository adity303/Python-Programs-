# Program to use map() to square numbers in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers) 

# Note - lambada function is used to calculate the square of a number 
# map function is used to apply to every elements of the list 
# list() function is used to converts the result of map() into a list