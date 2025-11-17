import random
#imported time
import time

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
        
    else:
        end_time = time.time()
        print("Incorrect. The correct answer is", total)
        print("You got ", score , "questions correct.") 
        #gotta work on this part, either to fix or remove it
        #try to focus on average score per second or if i cant change it to per minute
