# Program to use filter() to get even numbers from a list.  
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

# Just apply the filter function to find even numbers from the list. 