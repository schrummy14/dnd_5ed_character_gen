from random import randint


## Function that simulates dice rolls to calculate attribute scores
#
#  @param min_val Min value the dice can take (reroll 1s)
#  @param max_val Max value the dice can take (roll d10)
#  @param numDice Number of dice to roll
def rollAtribute(min_val, max_val, numDice):
    minRoll = max_val
    curSum = 0
    for k in range(numDice):
        curRoll = randint(min_val, max_val)
        curSum += curRoll
        if curRoll < minRoll:
            minRoll = curRoll
    curSum -= minRoll
    return curSum


def d100():
    return randint(1,100)

def d20():
    return randint(1,20)

def d12():
    return randint(1,12)

def d10():
    return randint(1,10)

def d8():
    return randint(1,8)

def d6():
    return randint(1,6)

def d4():
    return randint(1,4)
