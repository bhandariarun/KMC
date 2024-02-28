# # Task 03: Word Frequency Counter
#
# ## Objective
# Create a program that analyzes a given text and counts the frequency of each unique word.
#
# ## Requirements
#
# 1. Ask the user to input a paragraph or sentence.
# 2. Tokenize the input into words (ignoring punctuation and case sensitivity).
# 3. Count the frequency of each unique word.
# 4. Display the word frequencies in alphabetical order.
# 5. Handle cases where the input is empty.

import string
def word_frequency_counter(text):
    # Convert the text to lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text into words
    words = text.split()

    # Count the frequency of each unique word
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq


def display_word_frequencies(word_freq):
    # Display the word frequencies in alphabetical order
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[0])
    for word, frequency in sorted_word_freq:
        print(f"{word}: {frequency}")


def main():
    # Ask the user to input a paragraph or sentence
    text = input("Enter a paragraph or sentence: ").strip()

    if not text:
        print("Input is empty.")
    else:
        # Count word frequencies
        word_freq = word_frequency_counter(text)

        # Display word frequencies
        print("Word Frequencies:")
        display_word_frequencies(word_freq)


if __name__ == "__main__":
    main()