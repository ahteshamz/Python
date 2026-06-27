#Write a python program using python to convert Celsius to Fahrenheit.

def c_to_f(f):
    return 5*(f-32)/9
f = int(input("Enter temperature in F: "))
c = c_to_f(f)
print(f"{round(c, 2)}C")



#Write a program using python to convert meters to centimeters.
def m_to_cm(m):
    return m*100
f = int(input("Enter length in meters: "))
l = m_to_cm(f)
print(f"{l}cm")


#Write a program in python which converts inces to cms.
def inches_to_cms(inches):
    return inches*2.54
f = int(input("Enter length in inches: "))
c = inches_to_cms(f)
print(f"{c}cms")