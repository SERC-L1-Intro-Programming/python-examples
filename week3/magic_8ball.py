# Magic 8-Ball program
# Program responds to questions with magic 8-ball answers

import random

def get_answer(answer_number):
    # function takes a given number and returns a response string
    if answer_number == 1:
        return "It is certain"
    elif answer_number == 2:
        return "It is decidedly so"
    elif answer_number == 3:
        return "Yes"
    elif answer_number == 4:
        return "Reply hazy try again"
    elif answer_number == 5:
        return "Ask again later"
    elif answer_number == 6:
        return "Concentrate and ask again"
    elif answer_number == 7:
        return "My reply is no"
    elif answer_number == 8:
        return "Outlook not so good"
    elif answer_number == 9:
        return "Very doubtful!"

print("Magic 8-Ball will respond to your question")
print("")

while True:
    print("Input your question and Magic 8-Ball will answer")
    question = input()

    r = random.randint(1,9) # generate a random number between 1 and 9.
    fortune = get_answer(r)

    print(fortune)
