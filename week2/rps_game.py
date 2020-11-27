# Program that plays Rock, Paper, Scissors with the user.

import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print("{0} Wins, {1} Losses, {2} Ties".format(wins, losses, ties))
    while True: # The player input loop.
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        player_move = input()
        if player_move == 'q':
            sys.exit() # Quit the program.
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    rand_number = random.randint(1, 3)
    if rand_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif rand_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif rand_number == 3:
        computer_move = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1
    elif (player_move == 'r' and computer_move == 's') or (player_move == 'p' and computer_move == 'r') or (player_move == 's' and computer_move == 'p'):
        print('You win!')
        wins = wins + 1
    elif (player_move == 'r' and computer_move == 'p') or (player_move == 'p' and computer_move == 's') or (player_move == 's' and computer_move == 'r'):
        print('You lose!')
        losses = losses + 1
