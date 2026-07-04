# Write a program to input three numbers and print the largest among them.

num = int(input("Enter a number: "))
num2 = int(input("Enter a another number: "))
num3 = int(input("Enter a another number: "))

if num > num2 and num > num3:
    print("The largest number is:", num)
elif num2 > num and num2 > num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)
