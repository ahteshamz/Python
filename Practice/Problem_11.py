#Create a list of five fruits. Ask the user to enter a fruit name and check whether it exists in the list.
fruit = input("Enter the name of the fruit: ")
list =["apple", "banana", "pear", "grapes"]

for i in list:
    if fruit == i:
        print("The fruit is in the list.")
        break
else:
    print("The fruit is not in the list.")