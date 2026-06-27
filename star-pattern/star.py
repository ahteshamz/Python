'''
  *
 ***
*****

'''

# n = int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#     print(" "* (n-i), end="")
#     print("*"* (2*i-1), end="")
#     print("")


'''
***
**
*
'''
def pattern(n):
    if(n==1):
        return
    print("*" * n)
    pattern(n-1)
pattern(5)