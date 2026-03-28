# Program to merge two lists 
# Method 1 - Using + operator(Concatenation)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Method 2 - Using extend() function 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# Method 3 - Using unpacking operator (*)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
final_list = [*list1, *list2]
print(final_list)