# Write a program to find the sum of the digits of a number.

num = int(input("Enter any number.:"))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print("The sum of the digits is:", sum)