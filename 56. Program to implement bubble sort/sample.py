# Program to implement bubble sort 
numbers = [5, 3, 8, 6, 7, 2, 1, 4]
n = len(numbers) # Calculates total numbers of elements in a list  

for i in range(n): # This loops controls the number of passes. 
    for j in range(0, n-i-1): # this loop compares the adjacent elements 
        # n-i-1 is used because after every pass the last element is already sorted. 
        # Swap if the element found is greater than the next element
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp
    
    print("Sorted array is:")
    for i in numbers:
        print(i, end=" ")
        
    #BEST CASE - O(n) and Worst Case - O(n^2)