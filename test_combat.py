from class1 import *
import pytest
import random
from combat import *
def test_playerattack_notzero():
    char = characterinfo("The Hero",random.randint(30,50),random.randint(40,60),random.randint(10,20),100,False,100)
    rat = enemyinfo("Rat",random.randint(10,20),random.randint(20,30),random.randint(1,5),100,100)
    value = attack(char,rat)
    assert value > 0 #Value never below 0
def test_playerattack_belowmax():
    char = characterinfo("The Hero",random.randint(30,50),random.randint(40,60),random.randint(10,20),100,False,100)
    rat = enemyinfo("Rat",random.randint(10,20),random.randint(20,30),random.randint(1,5),100,100)
    value = attack(char,rat)
    assert value <= char.maxDamage #Value always lower than max
def test_attack_rat_king_noOOP():
    char = characterinfo("The Hero",random.randint(30,50),random.randint(40,60),random.randint(10,20),100,False,100)
    ratking = enemyinfo("Rat King",random.randint(30,50),random.randint(40,60),random.randint(10,20),100,100)
    value = ratkingattack(char,ratking)
    assert value == 0
def test_attack_rat_king_OOP():
    char = characterinfo("The Hero",random.randint(30,50),random.randint(40,60),random.randint(10,20),100,True,100)
    ratking = enemyinfo("Rat King",random.randint(30,50),random.randint(40,60),random.randint(10,20),100,100)
    value = ratkingattack(char,ratking)
    assert value != 0


    
