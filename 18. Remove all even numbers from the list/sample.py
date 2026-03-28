# Remove all even numbers from the list 
numbers = [1,2,3,4,5,6,7,8,9]

for n in numbers:
    if(n%2==0): # List for removing all even numbers from the list. 
        print(n, "is an even number")
    else:
        print(n, "is an odd number")