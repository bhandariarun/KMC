# # Task 01: Grading System Exercise
#
# ## Objective
# Create a simple grading system where a student's score is entered, and the program determines the corresponding grade.
#
# ## Requirements
#
# 1. Get the student's score as input.
# 2. Use the following grading scale:
#    - 90-100: A
#    - 80-89: B
#    - 70-79: C
#    - 60-69: D
#    - Below 60: F
# 3. Print the grade based on the input score.
# 4. Handle cases where the entered score is not within the valid range (0-100).

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