#Program to calculate the total marks and percentage by taking input from the user.

Physics = int(input("Enter marks of Physics: "))
Chemistry = int(input("Enter marks of Chemistry: "))
Maths = int(input("Enter marks of Maths: "))

print(f"Your total marks are: {Physics + Chemistry + Maths} out of 300")
print(f"Your percentage is: {(Physics + Chemistry + Maths)/300*100}")