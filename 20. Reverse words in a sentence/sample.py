# Reverse words in a sentence 
# Example - Python is great ---> great is Python 
s = input("Enter a string: ")

#.join function is used to join the sentence and .split function converts sentence into list of words. 
# [::-1] - Reverses the list 
reversed = " ".join(s.split()[::-1])
print(reversed)