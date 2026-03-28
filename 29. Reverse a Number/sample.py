# Program to reverse a number 
num = int(input("Enter a number"))

# 1. str(num) - First number is converted into string. 
# 2. Then slicing step starts. It's format is (start,stop,step). 
reversed = int(str(num) [::-1])
print(reversed)