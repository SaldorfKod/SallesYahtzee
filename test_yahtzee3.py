from yahtzee3 import rollIt
from yahtzee3 import checkYahtzee
from yahtzee3 import main
from die import Die



def test_is_yahtzee_when_all_dice_matches():
    dice = [Die(), Die(), Die(), Die(), Die()]
    #Set all dice to value of 6
    for die in dice:
        die.value = 6
    #Check if it now is yahtzee
    assert checkYahtzee(dice) == 6


def test_is_not_yahtzee_when_all_dice_not_matching_each_other():
    dice = [Die(), Die(), Die(), Die(), Die()]
    #Set all dice to same value
    for die in dice:
        die.value = 6
    #Change the value of one die
    dice[0].value = 2
    #Is it now NOT yahtzee?
    assert checkYahtzee(dice) == 0

