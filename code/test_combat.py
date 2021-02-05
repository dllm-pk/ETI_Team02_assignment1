from class1 import *
import pytest
import random
from combat import *
charstat = randint(30,50)
#charstat = character minimum damage
ratstat = randint(10,20)
#ratstat = rat minimum damage
rkstat = randint(30,50)
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
    char = characterinfo("The Hero",charstat,charstat+random.randint(5,10),random.randint(10,20),100,True,100)
    ratking = enemyinfo("Rat King",rkstat,rkstat+random.randint(5,10),random.randint(10,20),100,100)
    value = ratkingattack(char,ratking)
    assert value == 0
def test_attack_rat_king_OOP():
    char = characterinfo("The Hero",charstat,charstat+random.randint(5,10),random.randint(10,20),100,True,100)
    ratking = enemyinfo("Rat King",rkstat,rkstat+random.randint(5,10),random.randint(10,20),100,100)
    value = ratkingattack(char,ratking)
    assert value != 0 


    
