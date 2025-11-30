import random
import time
#user inputs a number value of their choice ofor the range of questions they would like to have them be asked 
a = int(input("Enter a number to be the range of the questions: "))
#thinking about adding motivational quotes at the end of the quiz - working on it
motivational_quotes = ["Great job! Keep practicing to improve your skills!",
                       "Well done! Every mistake is a step towards mastery.",
                       "Fantastic effort! You're getting better with each question.",
                       "Keep it up! Practice makes perfect.",
                       "You're doing amazing! Stay focused and keep learning."]
#defining the function for the multiplication quiz, being able to replay if the user decides to 
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
            #the else statement was important to end the function of the quiz to be able to rerun it whne typed a wrong question
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time
            elapsed_minutes = elapsed_time / 60
            average_per_minute = score / elapsed_minutes if elapsed_minutes > 0 else 0

            print(f"Incorrect. The correct answer is {total}.")
            print(f"You got {score} questions correct.")
            print(f"Average correct answers per minute: {average_per_minute:.2f}")
            break
# this loop will continue the program until the user decides to type anything other than yes or y
while True:
    multiplication_quiz()
    userinput = input("Do you want to play again? (yes/no): ")
    #will print a motivbational quote if the user decides not to play again
    if userinput not in ["yes", "y"]:
        print(random.choice(motivational_quotes))
        print("Thanks for playing!")
        break
