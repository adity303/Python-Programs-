# Count vowels and consonants in an string
var = input("Enter a string: ")

vowels = 0
consonants = 0

var = var.lower()

for i in var:
    if i in "aeiou":
        vowels += 1
    else:
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)