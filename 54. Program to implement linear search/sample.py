# Program to implement linear search 
linear = [10, 20, 80, 30, 60, 50, 110, 100]
key = int(input("Enter element to search: "))

for i in linear:
    if i == key: # Compares the current element i with the search element(key). 
        # and if they are equal, the element is found 
        print("Element found")
        break
else:
    print("Element not found")
    
# Linear Search means searching the element in the list one by one. If they found then it becomes true.