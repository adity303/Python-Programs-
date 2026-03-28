# Remove duplicates from the list 
tup = ("MISSISSIPPI")
myList = [1,3,4,5,6,7,7,5,3,2,1,5,7,8,8,3,1,4,6,7,8,5,7,8]
# using dict.fromkeys function is used to remove duplicates from the list. 
duplicate1 = list(dict.fromkeys(tup))
duplicate2 = list(dict.fromkeys(myList))
print(duplicate1)
print(duplicate2)