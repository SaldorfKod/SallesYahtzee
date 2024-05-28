from yahtzee3 import YahtzeeMainClass
from yahtzee3 import rollIt
from yahtzee3 import checkYahtzee
from yahtzee3 import main
from die import Die

import pytest


def test_is_yahtzee_when_all_dice_matches():
    dice = [Die(), Die(), Die(), Die(), Die()]
    
    for die in dice:
        die.value = 6
    
    # Assert something?
    assert checkYahtzee(dice) == 6


def test_is_not_yahtzee_when_all_dice_not_matching_each_other():
    dice = [Die(), Die(), Die(), Die(), Die()]
    
    for die in dice:
        die.value = 6
        
    dice[0].value = 2
    
    # Assert something?
    assert checkYahtzee(dice) == 0

if __name__ == '__main__':
    pytest.main()
