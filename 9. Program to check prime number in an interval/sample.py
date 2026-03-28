# Program to print all prime number in interval 
start = 11
end = 25
          
for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
