def is_palindromic_anagram(input_str):
    # Remove spaces and convert to lowercase
    input_str = input_str.replace(" ", "").lower()

    # Count the frequency of each character
    char_count = {}
    for char in input_str:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1

    # Count the number of characters with odd frequency
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)

    # If there is at most one character with odd frequency, it can form a palindrome
    return odd_count <= 1


def main():
    # Ask the user to input a string
    input_str = input("Enter a string: ").strip()

    # Check if the given string can be rearranged to form a palindromic string
    if not input_str:
        print("Input string is empty.")
    elif is_palindromic_anagram(input_str):
        print("The given string can be rearranged to form a palindromic string.")
    else:
        print("The given string cannot be rearranged to form a palindromic string.")


if __name__ == "__main__":
    main()