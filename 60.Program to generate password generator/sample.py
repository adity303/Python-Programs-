import random # same random function will be used. 

number = "1234567890"
string = "qwertyuiopasdfghjklzxcvbnm"
characters = number + string   # initialize characters to combine digits and letters

pg = ""

for i in range(10):  # generate a 10-character password
    pg += random.choice(characters) # formula for generating 10 digit password 

print("Your password is:", pg)