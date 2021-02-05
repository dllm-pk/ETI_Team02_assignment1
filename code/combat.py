import random
from class1 import *
"""
Combat functionalities (Faris)
"""
def attack(char, enemy):
    """
    Player Attack Function, returns hp lost
    """
    lose_hp = random.randint(char.minDamage,char.maxDamage) - enemy.defence
    if lose_hp <0:
        lose_hp = 0
    return lose_hp
def ratkingattack(char,enemy):
    """
    Ratking Attack Function, returns hp lost, default as 0 when player has no OOP
    """
    if char.oop == False:
        """
        Disabled if user has no orb of power
        """
        lose_hp = 0 
    else:
        lose_hp = random.randint(char.minDamage,char.maxDamage) - enemy.defence
        if lose_hp <0:
            lose_hp = 0
    return lose_hp
def enemy_attack(char, enemy):
    """
   Enemy Attack Function, returns hp lost
    """
    lose_hp = random.randint(enemy.maxDamage,enemy.minDamage) - char.defence
    if lose_hp <0:
            lose_hp = 0
    return lose_hp

