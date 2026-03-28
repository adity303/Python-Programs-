# Find missing number 
# The missing number can be found by numerous methods. The first method is: 
# 1. By using SUM formula (n)(n+1)/2, that is Missing Number = Expected Sum - Actual Sum 
nums = [1,2,3,5,6]

# len(sums) - counts the elements in the list 
n = len(nums)+1 # Calculation of total numbers 
expected_sum = n * (n+1) // 2 # Calculation of expected sum(if all numbers are there)
actual_sum = sum(nums) # calculates the actual_sum 

missing_number = expected_sum - actual_sum # Formula for missing number 
print(missing_number)

# Second method - Using SORT Method 
nums = [1,2,4,5,6]
nums.sort()

for i in range(len(nums)):
    if nums[i] != i+1:
        print(i+1)
        break