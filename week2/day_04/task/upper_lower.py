#write a python function that accepts a string and calculate the number of upper case letters and lower case letters

def count_upper_lower(s):
    upper_count = 0
    lower_count = 0

    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Example usage:
def main():
    input_string = str(input("Enter a string: "))
    upper_count, lower_count = count_upper_lower(input_string)
    print("Number of uppercase letters:", upper_count)
    print("Number of lowercase letters:", lower_count)
main()
