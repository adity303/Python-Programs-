with open("input.txt", "r") as source_file:
    with open("output.txt", "w") as output_file: 
        for line in source_file:
            if line.strip():  # checks if there is any blank space or not
                destination.write(line)
                
print("Blank lines removed successfully.!!")

# 2nd method 
with open("input.txt", "r") as source_file:
    lines =file.readlines()
    
with open("output.txt", "w") as output_file:
    for line in lines:
        if line.strip() != "": # check if line is not blank 
            file.write(line)
            
print("Blank lines removed successfully.!!") 