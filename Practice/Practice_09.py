# Write a program to count the number of vowels (a, e, i, o, u) in a string entered by the user.
str = input("Enter any word:")
vowels = "aeiouAEIOU"

count = 0
for i in str:
    if i in vowels:
        count += 1
print("The number of vowels in the word is:", count)