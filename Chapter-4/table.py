# Write a program to print multiplication table of a given number using for loop.
# num = int(input("Enter the number for multiplication table:"))

# for i in range (1, 11):
#     print(f"{num} x {i} = {num * i}")
#     print(num,"x", i, "=", num*i)

#Write a program to greet all the person names stored in a list l and which start with A

# l = ["Ahtesham", "Aroosha", "Zehra", "Ruqaiyya", "Aliza", "Humdan"]

# for name in l:
#     if name.startswith("R"):
#         print("Hello,", name)

#Write a program to check whether the number entered by the user is prime or not.

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prine Number")
else:
    for i in range (2, num):
        if num % i == 0:
            print("Not a Prime Number")
            break
        else:
            print("Prime Number")
