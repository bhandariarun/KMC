import random


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("-------------------------------")

    # Get the range of numbers from the user
    while True:
        try:
            min_num = int(input("Enter the minimum number of the range: "))
            max_num = int(input("Enter the maximum number of the range: "))
            break
        except ValueError:
            print("Please enter valid integers for the range.")

    # Generate a random number within the specified range
    secret_number = random.randint(min_num, max_num)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess the number between {} and {}: ".format(min_num, max_num)))
            attempts += 1

            if guess < min_num or guess > max_num:
                print("Your guess is out of the range. Please guess between {} and {}.".format(min_num, max_num))
                continue

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print("Congratulations! You guessed the number {} correctly in {} attempts!".format(secret_number,
                                                                                                    attempts))
                break
        except ValueError:
            print("Please enter a valid number.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        number_guessing_game()
    else:
        print("Thank you for playing!")


# Start the game
number_guessing_game()
