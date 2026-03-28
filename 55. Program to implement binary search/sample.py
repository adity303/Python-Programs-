# Program to implement binary search 
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

key = int(input("Enter element to search: "))

low = 0 # Set low to first index. 
high = len(arr) - 1 # Set high to last index.

while low <= high: 
    mid = (low + high) // 2 # Middle element found 

# Comparison of the element with middle element(mid).
# 1. If arr[mid] is equal then element is found
    if arr[mid] == key:
        print("Element found at index", mid)
        break
    # if key > arr[mid] then search in right half 
    elif arr[mid] < key:
        low = mid + 1
    else:
        # if key < arr[mid] then search in left half
        high = mid - 1
else:
    print("Element not found")
    
# Repeat the step until low > high 