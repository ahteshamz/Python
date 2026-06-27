#Write a program using function to find greaterst of three numbers.

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>b):
        return c
    
a = 4
b = 8
c = 12

print(greatest(a, b, c))