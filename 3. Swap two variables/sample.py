NUM1 = float(input("Enter the value of x: "))
NUM2 = float(input("Enter the value of y: "))
# Using 3rd variable (temp)
temp = NUM1
NUM1 = NUM2
NUM2 = temp
print("After swapping:")
print("x =", NUM1)
print("y =", NUM2)

# 2nd method
NUM1, NUM2 = NUM2, NUM1

# Alternative question = Swapping two numbers without using third variable 