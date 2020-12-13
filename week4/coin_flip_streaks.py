# Possible solution to coin flip streaks exercise.
# Program generates series of coin flips and checks for streaks of heads or tails
# in that series.

import random

FLIPS = 100
STREAK_LENGTH = 6
EXPERIMENTS = 10000

def coin_flip():
    ''' function returns a random "H" for heads or "T" for tails
    '''
    if random.randint(0,1): # 0 is False, 1 is True
        return "H"
    else:
        return "T"

print("** Coin Flip Probabilites **")
print("Calculate probability of streak of {0} heads or {0} tails in {1} coin flips".format(STREAK_LENGTH, FLIPS))
print("")

number_of_streaks = 0

for experiment_number in range(EXPERIMENTS):
    flip_series = ""

    # generate coin flips
    for _ in range(FLIPS):
        flip_series += coin_flip()

    # check if streak in series
    if ("H"*STREAK_LENGTH) in flip_series or ("T"*STREAK_LENGTH) in flip_series:
        number_of_streaks += 1

    # print running probability
    print(" {:.2f}%   ".format(number_of_streaks*100/(experiment_number+1)), end='\r')

print("Number of streaks in {} experiments: {}".format(EXPERIMENTS, number_of_streaks))
print("Chance of streak: {:.2f}%".format(number_of_streaks*100/EXPERIMENTS))
