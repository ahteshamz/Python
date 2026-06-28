#Write a program to accept marks of 6 students and display them in a sorted manner.


marks = []

m1 = int(input("Enter marks here:"))
marks.append(m1)

m2 = int(input("Enter marks here:"))
marks.append(m2)

m3 = int(input("Enter marks here:"))
marks.append(m3)

m4 = int(input("Enter marks here:"))
marks.append(m4)

m4 = int(input("Enter marks here:"))
marks.append(m4)

f6 = int(input("Enter marks here:"))
marks.append(f6)

marks.sort()
print(marks)