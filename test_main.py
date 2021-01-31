import pytest
from mainprog import *
from class1 import *
import random

def test_orb():
    char = characterinfo("The Hero",random.randint(30,50),random.randint(40,60),random.randint(10,20),100,False,100)
    test = [char.minDamage,char.maxDamage,char.defence]
    result = orb(char)
    original = [i-5 for i in result]
    assert test == original

def test_rest_day_passed():#Checks if the day actually passes
    char = characterinfo("The Hero",random.randint(30,50),random.randint(40,60),random.randint(10,20),100,False,100)
    day = random.randint(1,10) #Day passing
    result = rest(day,char)
    assert result[0] == day + 1

def test_rest_hpgap_lessthan20():#HP will be fully healed
    char = characterinfo("The Hero",random.randint(30,50),random.randint(40,60),random.randint(10,20),random.randint(80,100),False,100)
    result = rest(1,char)
    assert result[1] == char.maxhp

def test_rest_hpgap_morethan20():#HP will be fully healed
    char = characterinfo("The Hero",random.randint(30,50),random.randint(40,60),random.randint(10,20),random.randint(1,79),False,100)
    result = rest(1,char)
    assert char.hp + 20 == result[1]


      
       

        
