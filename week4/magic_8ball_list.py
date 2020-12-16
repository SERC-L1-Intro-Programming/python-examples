# Magic 8-Ball program using list to store response
# Program responds to questions with magic 8-ball answers

import random

messages = [
    'It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful'
]

print("Magic 8-Ball will respond to your question")
print("")

while True:
    print("Input your question and Magic 8-Ball will answer")
    question = input()

    fortune = random.choice(messages)
    print(fortune)