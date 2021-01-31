import random
import class1
#Faris: The attack is performed by the user. When the function is executed, the following happens
#A random integer between minimum and maximum will be subtracted by the defence
#This value will be the HP lost by the enemy rat
def attack(char, enemy):
    if char.minDamage>char.maxDamage:
        lose_hp = random.randint(char.maxDamage,char.minDamage) - enemy.defence
    else:
        lose_hp = random.randint(char.minDamage,char.maxDamage) - enemy.defence
    if lose_hp <0:
        lose_hp = 0
    return lose_hp
def ratkingattack(char,enemy):
    if char.oop == False:
        lose_hp = 0
    elif char.minDamage>char.maxDamage:
        lose_hp = random.randint(char.maxDamage,char.minDamage) - enemy.defence
    else:
        lose_hp = random.randint(char.minDamage,char.maxDamage) - enemy.defence
        if lose_hp <0:
            lose_hp = 0
    return lose_hp
#Faris: This is an attack test function as performed by the enemy
def enemy_attack(enemy, char):
    if enemy.minDamage>enemy.maxDamage:
        lose_hp = random.randint(enemy.maxDamage,enemy.minDamage) - char.defence
    else:
        lose_hp = random.randint(enemy.minDamage,enemy.maxDamage) - char.defence
    if lose_hp <0:
            lose_hp = 0
    return lose_hp

