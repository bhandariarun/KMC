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

def is_valid_word(word):
    return word.isalpha() and len(word) > 0

def generate_pyramid(word, direction):
    if not is_valid_word(word):
        print("Invalid word.")
        return

    if direction.lower() == "up":
        for i in range(1, len(word) + 1):
            print(" " * (len(word) - i) + " ".join(word[:i]))
    elif direction.lower() == "down":
        for i in range(len(word), 0, -1):
            print(" " * (len(word) - i) + " ".join(word[:i]))

def main():
    word = input("Enter a word: ").strip()
    direction = input("Enter direction (up or down): ").strip()

    generate_pyramid(word, direction)

if __name__ == "__main__":
    main()