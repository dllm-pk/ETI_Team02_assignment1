from class1 import *
import pytest
import random
from combat import *
def test_playerattack_notzero():
    char = characterinfo("The Hero",random.randint(30,50),char.minDamage+random.randint(5,10),random.randint(10,20),100,True,100)
    ratking = enemyinfo("Rat King",random.randint(30,50),rat.minDamage+random.randint(5,10),random.randint(10,20),100,100)
    value = attack(char,rat)
    assert value > 0 #Value never below 0
def test_playerattack_belowmax():
    char = characterinfo("The Hero",random.randint(30,50),char.minDamage+random.randint(5,10),random.randint(10,20),100,True,100)
    ratking = enemyinfo("Rat King",random.randint(30,50),rat.minDamage+random.randint(5,10),random.randint(10,20),100,100)
    value = attack(char,rat)
    assert value <= char.maxDamage #Value always lower than max
def test_attack_rat_king_noOOP():
    char = characterinfo("The Hero",random.randint(30,50),char.minDamage+random.randint(5,10),random.randint(10,20),100,True,100)
    ratking = enemyinfo("Rat King",random.randint(30,50),ratking.minDamage+random.randint(5,10),random.randint(10,20),100,100)
    value = ratkingattack(char,ratking)
    assert value == 0
def test_attack_rat_king_OOP():
    char = characterinfo("The Hero",random.randint(30,50),char.minDamage+random.randint(5,10),random.randint(10,20),100,True,100)
    ratking = enemyinfo("Rat King",random.randint(30,50),ratking.minDamage+random.randint(5,10),random.randint(10,20),100,100)
    value = ratkingattack(char,ratking)
    assert value != 0 


    
