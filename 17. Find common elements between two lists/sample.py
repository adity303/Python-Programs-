# Find common elements between two lists 
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
# Method1 = using list(set) and & operator. list(set) will converts list to set. 
# & - performs intersection 
# list() - converts back to list
common = list(set(list1) & set(list2))
print(common)

# method2 = Using set.intersection(), list(set) will converts list to set 
common = list(set(list1).intersection(set(list2)))