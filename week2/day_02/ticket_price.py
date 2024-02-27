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