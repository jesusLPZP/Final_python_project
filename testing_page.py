import random
import time
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

