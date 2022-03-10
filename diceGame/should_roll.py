"""Optimal PIG dice game solution."""
import pickle
from collections import Counter

# Code made by rodri45z,
# using data from http://cs.gettysburg.edu/projects/pig/piggame.html
# and equations from http://cs.gettysburg.edu/~tneller/papers/pig.zip

GOAL = 100

with open("./diceGame/probabilities_list.pickle", "rb") as fp:
    p = pickle.load(fp)

for x1 in range(0, 100):
    for x2 in range(0, 100):
        for zero in range(1, 100):
            p[x1][x2].append(0)


def should_roll(i, j, k):
    """Return a boolean depending on if the player should roll or not."""
    # i = Player score
    # j = Oponents score
    # k = PLayers turn total
    p_roll = 1 - p_win(j, i, 0)
    for dice in range(2, 7):
        p_roll += p_win(i, j, k + dice)
    p_roll /= 6
    p_hold = 1 - p_win(j, i + k, 0)
    return p_roll > p_hold


def count_zeros(p_list):
    """Count zeros in a list."""
    dic = Counter(p_list)
    return GOAL - dic[0]


def p_win(i, j, k):
    """Calculate the probabilities of winning."""
    if i + k >= GOAL:
        return 1.0
    if j >= GOAL:
        return 0
    if k != 0 and (count_zeros(p[i][j]) < GOAL - i):
        for dice2 in range(GOAL - 1, 0, -1):
            if p[i][j][dice2] == 0:
                p_roll = 1 - p[j][i][0]
                for roll in range(2, 7):
                    p_roll += p_win(i, j, dice2 + roll)
                p_roll /= 6
                p_hold = 1 - p_win(j, i + dice2, 0)
                if p_hold > p_roll:
                    p[i][j][dice2] = p_hold
                else:
                    p[i][j][dice2] = p_roll
            else:
                break
    return p[i][j][k]
