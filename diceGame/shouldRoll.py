"""Optimal PIG dice game solution."""
import pickle
from collections import Counter
"""Code made by rodri45z,
using data from http://cs.gettysburg.edu/projects/pig/piggame.html
and equations from http://cs.gettysburg.edu/~tneller/papers/pig.zip"""

GOAL = 100

with open('./DiceGame/probabilities_list', 'rb') as fp:
    p = pickle.load(fp)

for x1 in range(0, 100):
    for x2 in range(0, 100):
        for zero in range(1, 100):
            p[x1][x2].append(0)


def shouldRoll(i, j, k):
    """Return a boolean depending on if the player should roll or not."""
    '''i = Player score
       j = Oponents score
       k = PLayers total '''
    pRoll = 1 - pWin(j, i, 0)
    for dice in range(2, 7):
        pRoll += pWin(i, j, k + dice)
    pRoll /= 6
    pHold = 1 - pWin(j, i + k, 0)
    return pRoll > pHold


def countZeros(pList):
    """Count zeros in a list."""
    dic = Counter(pList)
    return GOAL-dic[0]


def pWin(i, j, k):
    """Calculate the probabilities of winning."""
    if i+k >= GOAL:
        return 1.0
    if j >= GOAL:
        return 0
    if k != 0 and (countZeros(p[i][j]) < GOAL - i):
        for dice2 in range(GOAL-1, 0, -1):
            if p[i][j][dice2] == 0:
                pRoll = 1 - p[j][i][0]
                for roll in range(2, 7):
                    pRoll += pWin(i, j, dice2 + roll)
                pRoll /= 6
                pHold = 1 - pWin(j, i + dice2, 0)
                if pHold > pRoll:
                    p[i][j][dice2] = pHold
                else:
                    p[i][j][dice2] = pRoll
            else:
                break
    return p[i][j][k]

pWin(1, 1, 86)