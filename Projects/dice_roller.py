#Loop
  #Ask: roll the dice?
    #   If user enter Yes
    #       Generate two random number.
    #       Print them.
    #   If the user enter No
    #       Print thank you message
    # Terminate the program
    #Invalid choice
import random

while True:
 choice = input("Do you want to roll the dice? (Yes/No): ").lower()
 if choice == "yes":
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f'({dice1}, {dice2})')
 elif choice == "no":
    print("Thank you for using the dice roller!")   
else:
    print("Invalid choice. Please enter Yes or No.")