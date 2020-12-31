import random
#Faris: The attack is performed by the user. When the function is executed, the following happens
#A random integer between minimum and maximum will be subtracted by the defence
#This value will be the HP lost by the enemy rat
def attack(min_damage,max_damage, defence):
    lose_hp = random.randint(min_damage,max_damage) - defence
    return lose_hp
#Faris: This is an attack test function as performed by the enemy
def enemy_attack():
    lose_hp = random.randint(1,5)
    return lose_hp
