# Finding most frequent elements in a list. 
from collections import Counter
list = [1,2,2,2,4,4,3,3,3,5,6,4,3,5,6,3,7,8,9,7,6,5,7,8,8]

# Best method - Use counter for counting frequent elements in a list.
max_count = Counter(list)
print(max_count)