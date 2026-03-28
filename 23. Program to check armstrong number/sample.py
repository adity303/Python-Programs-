#Check armstrong number 
# Armstrong number - Any three digit number is said to this if its sum of cubes equal to its own value. 
# For eg - 153 = 1*1*1 + 5*5*5 + 3*3*3 = 153 itself 
num = int(input("Enter a number: "))  # Take a number from the user

sum = 0        # Variable to store the sum of cubes of digits
temp = num     # Copy the original number into temp so the original value remains unchanged

while temp > 0: 
    digit = temp % 10      # Extract the last digit of the number
    cube = digit ** 3      # Calculate the cube of the extracted digit
    sum = sum + cube       # Add the cube value to the sum
    temp //= 10            # Remove the last digit from the number using floor division

# After processing all digits, compare the calculated sum with the original number
if sum == num: 
    print("It is an Armstrong number")
else: 
    print("Not an Armstrong number")