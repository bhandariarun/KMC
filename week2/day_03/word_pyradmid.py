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