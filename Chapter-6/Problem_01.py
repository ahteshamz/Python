#Create a class "Programmer" for storing information about few programmers working at Microsoft.

class  Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = Programmer("Ahtesham", 1500000, 110025)
print(p.name, p.salary, p.pincode, p.company)
s = Programmer("Saif", 1500000, 110026)
print(s.name, s.salary, s.pincode, s.company)