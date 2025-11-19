import random
import time
#user inputs a number value of their choice ofor the range of questions they would like to have them be asked 
a = int(input("Enter a number to be the range of the questions: "))
#thinking about adding motivational quotes at the end of the quiz - working on it
motivational_quotes = []
#defining the function for the multiplication quiz
def multiplication_quiz():
    a = int(input("Enter a number to be the range of the questions: "))
    score = 0
    start_time = time.time()

    while True:
        number1 = random.randint(1, a)
        number2 = random.randint(1, a)
        total = number1 * number2

        print(f"What is {number1} times {number2}?")
        answer = int(input("Your answer: "))

        if answer == total:
            score += 1
            print("Correct! Next Question\n")
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time
            elapsed_minutes = elapsed_time / 60
            average_per_minute = score / elapsed_minutes if elapsed_minutes > 0 else 0

            print(f"Incorrect. The correct answer is {total}.")
            print(f"You got {score} questions correct.")
            print(f"Average correct answers per minute: {average_per_minute:.2f}")
            break
#when the user types in a number value grater than , the quiz will begin
while a >= 0:
    multiplication_quiz()
    #when the quiz ends, the user will be prompted to play again or not
    userinput = input("Do you want to play again? (yes/no)")
#if typed in yes it will 
    if userinput == "yes" or userinput =="Yes" or userinput =="y" or userinput ==("Y"):
        multiplication_quiz()
    else:
        print(motivational_quotes)
