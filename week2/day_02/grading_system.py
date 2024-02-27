def student(score):
    if score >=90 and score <= 100:
        print("The marks secured by student is 90-100:A")
    elif score >=80 and score <= 89:
        print("The marks secured by student is 80-89:B")
    elif score >=70 and score <= 79:
        print("The marks secured by student is 70-79:C")
    elif score >= 60 and score <= 69:
        print("The marks secured by student is 60-69:D")
    else:
        print("The marks secured by student is below 60:F")

def main():
    score = int(input("Enter a mark that is secured by student: "))
    student(score)
main()