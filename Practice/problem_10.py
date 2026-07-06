# Write a Python program to reverse a string entered by the user.

text = input("Enter any string you want to reverse: ")

reverse = ""
for i in text:
    reverse = i + reverse

print("The reverse string is:", reverse)

