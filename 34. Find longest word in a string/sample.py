# Finding longest word in a string. 
word = "Hello my name is Aditya."
res = " " # Initialising a new variable res to store the longest word.

words = word.split()  # Split the sentence into each word

for word in words: 
    if len(word) > len(res): # condition: if length of word is greater than longest word 
        res = word # longest word is equivalent to word 
print(res)