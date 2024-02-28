#Write a python function to multiply all the members in a list

def multiply(listed):
    result = 1
    for x in listed:
        result= result * x
    return result

def main():
    list1 = [1, 2, 3, 4, 5]
    print(multiply(list1))
main()