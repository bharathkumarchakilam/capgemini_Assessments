#importing the random module
import random

#displays the result
def display(result):
    print(result)
        
#input from the user
def get_input():
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

#checking the number guessed by the user
def number_guessing_game(guess, random_number):
    if guess > random_number:
        return "Too High"
    elif guess < random_number:
        return "Too Low"
    else:
        return "You guessed it right!"

#main function
def main():
    random_number = random.randint(1, 100)
    print("Guess the number (between 1 and 100).")
    while True:
        guess = get_input()
        result = number_guessing_game(guess, random_number)
        display(result)
        if result == "You guessed it right!":
            break

main()
