#Write a python function to find factorial of a given negative numbers
def factorial(n):
    if (n == 1 or n == 0):
        return 1

    else:
        return n * factorial(n - 1)

def main():
    n = int(input("Enter a number: "))
    print("Factorial of", n, "is", factorial(n))
main()
