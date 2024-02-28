# # Task 01: Word Pyramid Generator
#
# ## Task
#
# Create a program that generates a word pyramid pattern based on user input.
#
# ## Objective
#
# The objective is to generate and print a pyramid pattern using the letters of the word provided by the user. Each level of the pyramid should display the letters of the word up to that level, and the word should be centered on each level of the pyramid.
#
# ## Requirements
#
# 1. Ask the user to input a word.
# 2. Generate and print a pyramid pattern using the letters of the word.
# 3. Each level of the pyramid should display the letters of the word up to that level.
# 4. The word should be centered on each level of the pyramid.
#
# ## Additional Challenges
#
# 1. Implement a function to validate the input and ensure it's a valid word.
# 2. Allow the user to choose the direction of the pyramid (upwards or downwards).
# 3. Enhance the program to handle phrases or sentences instead of single words.
#
# Expected Output:
# if word level is up:
# ```
#             S
#            S u
#           S u n
#          S u n i
#         S u n i l
# ```
#
# if word level is Down:
# ```
#             S u n i l
#              S u n i
#               S u n
#                S u
#                 S
# ```

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
