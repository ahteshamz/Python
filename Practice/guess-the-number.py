import random

number = random.randint(1, 10)
number_of_guess = 0

while number_of_guess < 5:
    try:
        guess = int(input("Enter your guess (1-10): "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    number_of_guess += 1

    if guess < number:
        print("Your guess is too low")
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Congratulations! You guessed the number in " + str(number_of_guess) + " tries!")
        break
else:
    print("Sorry, you did not guess the number. The number was " + str(number))
