#write a python function that takes a list and return a new list with unique elements of the first list

def unique_elements_traversal(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

# Example usage:
def main():
    input_list1 = [1,2,2,3,4,5,5,10, 20, 10, 30, 40, 40]
    print("Unique values from the first list:")
    print(unique_elements_traversal(input_list1))

main()