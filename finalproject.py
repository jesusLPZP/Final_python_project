import random
#imported time
import time
a = int(input("Enter a number to be the range of the questions: "))
score = 0
total = ""
start_time = time.time()
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
        elapsed_time = end_time - start_time
        print("Incorrect. The correct answer is", total)
        print("You got ", score , "questions correct in", round(elapsed_time,2), "seconds.") 
        #gotta work on this part, either to fix or remove it
        #try to focus on average score per second or if i cant change it to per minute
        average_score = score / (elapsed_time/60)
        print("you got an average of", average_score, "questions per second.")
