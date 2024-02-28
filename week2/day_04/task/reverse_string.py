def reverse(string):
    string = string[::-1]
    return string


s = str(input("Enter a string: "))

print("The original string is : ", end="")
print(s)

print("The reversed string is : ", end="")
print(reverse(s))