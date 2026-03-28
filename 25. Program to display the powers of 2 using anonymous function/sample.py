# Program to find the powers of 2 using anonymous function 
n_terms = int(input("Enter number of terms here: "))

# 2nd method 
result = []
# Lambada function is used to create anonymous function 
# Here lambada function taking x variable and produces 2 raised to the power x.
# Map function is used to return map of the object according to the user's choice of writing the code. The syntax is map(function, iterable)
# Actually map applies function to each element. 
# list - It converts results into lists. 
result = list(map(lambda x : 2 ** x, range(n_terms+1)))

# 2nd method 
for i in range(n_terms+ 1):
    result.append(2**i)

for i in range(n_terms+1):
    print("The value of 2 raised to the power of", i, "is", result[i])