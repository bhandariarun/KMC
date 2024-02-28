#write a python function that takes a number as a parameter and check the number is prime or not

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True

def main():
    number_to_check = int(input("Enter a number: "))
    if is_prime(number_to_check):
        print(f"{number_to_check} is a prime number")
    else:
        print(f"{number_to_check} is not a prime number")
main()