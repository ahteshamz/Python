#Simple Interest 

p = float(input("Enter the principle amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Ente the time in years:"))

si = (p*r*t)/100
amount = p + si
print("The simple interest is:", si, "and the total amount is:", amount)