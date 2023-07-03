#! /usr/bin/python3
# GuessingGame by Zach Karr

import random

# we need global variables for previous category and previous distance
previous_category = 0
previous_difference = 0


def main():
    print("Welcome to the Guessing Game!")
    game_type = get_choice()
    while game_type != 0:
        random_number = random.randint(1, 100)
        print("I'm thinking of a number between 1 and 100...")
        if game_type == 1:
            play_hot_cold(random_number)
        elif game_type == 2:
            play_high_low(random_number)
        else:
            print("Unknown game type.")
        game_type = get_choice()
    print("Thanks for playing the Guessing Game!")


def get_choice():
    # final version must have robust menu: validate for 0-2, don't crash
    choice = -1
    while choice == -1:
        try:
            choice = int(input("Game type: 1 = Hot/Cold, 2 = High/Low, 0 = Quit: "))
        except ValueError:
            print("Unknown game selection, try again!")
            choice = -1
    return choice


def get_guess():
    # obtains user input and returns only numbers 0-100
    guess = -1
    while guess == -1:
        try:
            guess = int(input("Your guess? (1-100, 0 = Quit): "))
        except ValueError:
            guess = -1
        return guess


def play_hot_cold(random_number):
    guess_count = 0
    playing = True
    while playing:
        guess = get_guess()
        guess_count += 1
        if guess == random_number:
            print("You guessed my number in " + str(guess_count) + " guesses!")
            playing = False
        elif guess == 0:
            print(
                "Sorry, you did not guess my number "
                + str(random_number)
                + " in "
                + str(guess_count - 1)
                + " guesses."
            )
            playing = False
        elif guess == -1:
            print("Bad guess, try picking a number next time.")
        else:
            show_hot_cold(random_number, guess)
            # end of play_hot_cold


def show_hot_cold(random_number, guess):
    global previous_category, previous_difference
    current_difference = abs(random_number - guess)
    current_category = 0
    message = "Your guess is: "
    if current_difference >= 60:
        current_category = 1
        if current_category != previous_category:
            print(message + "cold")
        else:
            if current_difference < previous_difference:
                print(message + "cold (getting warmer)")
            elif current_difference > previous_difference:
                print(message + "cold (getting colder)")
            else:
                print(message + "cold ...but same degree")
    elif 60 > current_difference >= 30:
        current_category = 2
        if current_category != previous_category:
            print(message + "warm")
        else:
            if current_difference < previous_difference:
                print(message + "warm (getting warmer)")
            elif current_difference > previous_difference:
                print(message + "warm (getting colder)")
            else:
                print(message + "warm ...but same degree")
    elif 30 > current_difference >= 16:
        current_category = 3
        if current_category != previous_category:
            print(message + "very warm")
        else:
            if current_difference < previous_difference:
                print(message + "very warm (getting warmer!)")
            elif current_difference > previous_difference:
                print(message + "very warm (getting colder!)")
            else:
                print(message + "very warm ...but same degree")
    elif current_difference <= 15:
        current_category = 4
        if current_category != previous_category:
            print(message + "HOT")
        else:
            if current_difference < previous_difference:
                print(message + "HOT (GETTING HOTTER)")
            elif current_difference > previous_difference:
                print(message + "HOT (GETTING COLDER)")
            else:
                print(message + "HOT ...but same degree")
    else:
        print("Bad guess, try picking a number next time.")
    previous_difference = current_difference
    previous_category = current_category


def play_high_low(random_number):
    guess_count = 0
    playing = True
    while playing:
        guess = get_guess()
        guess_count += 1
        if guess == random_number:
            print("Correct! You guessed my number in " + str(guess_count) + " trys!")
            playing = False
        elif guess == 0:
            print(
                "Sorry, you did not guess my number "
                + str(random_number)
                + " in "
                + str(guess_count - 1)
                + " guesses."
            )
            playing = False
        elif guess > random_number:
            print("Sorry, that guess is too high")
        elif random_number > guess > 0:
            print("Sorry, that guess is too low")
        else:
            print("Bad input option")


if __name__ == "__main__":
    main()
