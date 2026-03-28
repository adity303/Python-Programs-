# Calculation of each character in a string.
# Method 1 - Using Counter library, will count the each character in a string  
from collections import Counter
str = input("Enter a string:")
count = Counter(str)

print(count)
