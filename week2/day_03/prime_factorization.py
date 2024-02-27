def sort_numbers(input_list, ascending=True):
    odd_numbers = []
    even_numbers = []
    for item in input_list:
        if isinstance(item, int) or isinstance(item, float):
            if item % 2 == 0:
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
    if ascending:
        odd_numbers.sort()
        even_numbers.sort()
    else:
        odd_numbers.sort(reverse=True)
        even_numbers.sort(reverse=True)
    return odd_numbers, even_numbers


def main():
    input_values = input("Enter a list of numbers or values (comma-separated): ").split(',')
    input_list = []
    for value in input_values:
        try:
            input_list.append(float(value))
        except ValueError:
            input_list.append(value.strip())

    ascending = input("Sort in ascending order? (yes/no): ").strip().lower() == "yes"

    odd_numbers, even_numbers = sort_numbers(input_list, ascending)

    print("Odd Numbers:", odd_numbers)
    print("Even Numbers:", even_numbers)


if __name__ == "__main__":
    main()
