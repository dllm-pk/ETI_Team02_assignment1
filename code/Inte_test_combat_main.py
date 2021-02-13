from class1 import *
import pytest
import random
from combat import *
import pytest
from mainprog import *
import random

charstat = random.randint(30,50)
#charstat = character minimum damage
ratstat = random.randint(10,20)
#ratstat = rat minimum damage
rkstat = random.randint(30,50)
#rkstat = ratking minimum damage
def test_playerattack_notzero():
    char = characterinfo("The Hero",charstat,charstat+random.randint(5,10),random.randint(10,20),100,True,100)
    rat = enemyinfo("Rat",ratstat,ratstat+random.randint(5,10),random.randint(10,20),100,100)
    value = attack(char,rat)
    assert value > 0 #Value never below 0
def test_playerattack_belowmax():
    char = characterinfo("The Hero",charstat,charstat+random.randint(5,10),random.randint(10,20),100,True,100)
    rat = enemyinfo("Rat",ratstat,ratstat+random.randint(5,10),random.randint(10,20),100,100)
    value = attack(char,rat)
    assert value <= char.maxDamage #Value always lower than max
def test_attack_rat_king_noOOP():
    char = characterinfo("The Hero",charstat,charstat+random.randint(5,10),random.randint(10,20),100,False,100)
    ratking = enemyinfo("Rat King",rkstat,rkstat+random.randint(5,10),random.randint(10,20),100,100)
    value = ratkingattack(char,ratking)
    assert value == 0
def test_attack_rat_king_OOP():
    char = characterinfo("The Hero",charstat,charstat+random.randint(5,10),random.randint(10,20),100,True,100)
    ratking = enemyinfo("Rat King",rkstat,rkstat+random.randint(5,10),random.randint(10,20),100,100)
    value = ratkingattack(char,ratking)
    assert value != 0 



def test_orb():
    char = characterinfo("The Hero",charstat,charstat+random.randint(5,10),random.randint(10,20),100,False,100)
    test = [char.minDamage,char.maxDamage,char.defence]
    result = orb(char)
    original = [i-5 for i in result]
    assert test == original

def test_rest_day_passed():#Checks if the day actually passes
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

