import random
a = int(input("Enter a number to be the range of the questions: "))
score = 0
total = ""
while total == "":
    number1 = random.randint(1, a)
    number2 = random.randint(1, a)
    total = number1 * number2
    print ("What is", number1, "times", number2, "?")
    answer = int(input("Your answer: "))
    if answer == total:
        score += 1
        print("Correct! Next Quetsion")
        total = ""
        number1 = random.randint(1, a)
        number2 = random.randint(1, a)
        total = number1 * number2
        print ("What is", number1, "times", number2, "?")
        answer = int(input("Your answer: "))
        total = ""
    else:
        print("Incorrect. The correct answer is", total)
        print("You got ", score , "questions correct.")
        # Reset total to continue the loop
    