a = b = c = 0
for i in range(1, 11):
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number :"))
    if b == 0 :
        print("Division by zero error")
        continue
    else :
        c = a // b
        print("Quotient", c)
        print("End of program")