
import pytest
import random
#from full_program import *


#def test_attack(outdoor_attack):
    #add(1)
    #option = get_option(1)
    #COMBAT_OPTIONS[option-1](game)

#def test_enemyattack(outdoor_run):
    #add(2)
    #assert "You fled"

from combat import *
def test_playerattack():
    a = random.randint(1,10) #min dmg
    b = random.randint(a+1,a+4) #max dmg
    c = random.randint(1,a-1) #defence 
    value = attack(a,b,c)
    max = b-c
    min = a-c
    assert value <= max & value > 0 #Value always lower than max, value never below 0

    
