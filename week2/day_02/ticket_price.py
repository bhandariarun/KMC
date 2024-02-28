# # Task 02: Ticket Price Calculator Exercise
#
# ## Objective
# Create a program that calculates the ticket price for a movie based on the age and whether the customer is a student.
#
# ## Requirements
#
# 1. Get the user's age and whether they are a student (True or False) as input.
# 2. Define the ticket prices:
#    - Children (age 0-12): \$10
#    - Teenagers (age 13-17): \$15
#    - Adults (age 18 and above): $20
#    - Students (regardless of age): \$18 (discounted price)
# 3. Calculate and print the ticket price based on the user's age and student status.
# 4. Handle cases where the entered age is not a valid numeric value.
# 5. Provide a message for cases where the age is negative or non-integer.

def calculate_ticket_price(age, is_student):
    if age < 0 or not isinstance(age, int):
        print("Invalid age entered.")
        return
    if is_student:
        return 18
    elif age <= 12:
        return 10
    elif age <= 17:
        return 15
    else:
        return 20

def main():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                print("Age cannot be negative.")
                continue
            is_student_str = input("Are you a student? (True/False): ")
            is_student = is_student_str.lower() == 'true'
            ticket_price = calculate_ticket_price(age, is_student)
            if ticket_price is not None:
                print("Ticket Price: ${}".format(ticket_price))
            break
        except ValueError:
            print("Invalid input. Please enter a valid age.")

main()