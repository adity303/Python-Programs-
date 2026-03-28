# Program to check prime number 
num = int(input("Enter a number: "))
if num == 1: 
    print("Number is not a prime number")

for i in range(2, num):
    if num % i == 0:
        print(num, "is not a prime number")
        break
else:
    print(num,"is a prime number")