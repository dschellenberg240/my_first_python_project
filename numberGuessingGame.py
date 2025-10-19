"""
      My First program 10/19/2025
Guess my number!
Basic guessing game using .random, function, and a while loop
Guess number between 1 - 100 inclusive
"""
import random

def rando_num():
    return random.randint(1, 100)

print("Welcome to the number guessing game!\n")

play_again = "Y"

while play_again == "Y":
    print("I'm thinking of a number between 1 - 100. Can you guess my number?\n")
    my_random_num = rando_num()
    number_guess = -1

    while number_guess != my_random_num:
        number_guess = int(input("Your guess: "))
        if number_guess == my_random_num:
            print(f"Awesome! You guessed it! My number was is fact {my_random_num}.\n")
        elif number_guess > my_random_num:
            print("Nope! Try guessing lower.\n")
        elif number_guess < my_random_num:
            print("Sorry, too low.\n")

    play_again  = input("You did great, want to go another round?(Y, N): ").upper()

print("Thanks for playing, see you soon.")