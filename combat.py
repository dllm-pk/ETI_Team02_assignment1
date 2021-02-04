import random
import class1
"""
Combat functionalities (Faris)
"""
def attack(char, enemy):
    """
    User Attack Function
    """
    lose_hp = random.randint(char.minDamage,char.maxDamage) - enemy.defence
    if lose_hp <0:
        lose_hp = 0
    return lose_hp
def ratkingattack(char,enemy):
    """
    Ratking Attack Function 
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
#Faris: This is an attack test function as performed by the enemy
def enemy_attack(enemy, char):
    """
   Enemy Attack Function
    """
    lose_hp = random.randint(enemy.maxDamage,enemy.minDamage) - char.defence
    if lose_hp <0:
            lose_hp = 0
    return lose_hp

