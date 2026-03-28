# program to generate an OTP 
import random # for making an otp, we should use random function 

length = 3 # Decide length on their own 
number = "013456246789" # decide on their own 
otp = "" # initialize an otp variable to store length of the digits 

for i in range(length):
    otp += random.choice(number) # It means any otp that it will take, will add with random number with choice. 

print("Your OTP is:", otp) # Print that otp. 