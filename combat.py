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

#Faris: combat manual test
#Test values
min = 1
max = 3
defn = 1
hp = 10
user_hp = 100
#Menu for combat
combat_mode = True #Ensures loop functionality
while combat_mode == True: #Loop for combat menu
    print("Encounter! - Rat \nDamage: {0} - {1} \nDefence: {2} \nHP: {3} \n1) Attack \n2) Run".format(min,max,defn,hp))
    choice = input("Enter Choice: ")#Menu choice
    print(" ")
    if choice == "1":#Attack
        hit = attack(min,max,defn)#damage to rat
        print("You deal {} damage to the rat".format(hit))
        hp = hp - hit
        if hp <= 0:#rat hp below zero
            print("The Rat is dead! You are victorious!")
            break#End combat
        else:
            tackle = enemy_attack()#damage to player
            print("Ouch! The Rat hit you for {} damage!".format(tackle))
            user_hp = user_hp - tackle
            if user_hp <= 0:
                user_hp = 0#player's HP cant go below 0
            print("You have {} HP left.".format(user_hp))
            if user_hp <= 0:
                print("Your HP is zero. You are dead")
                break#End combat
    elif choice == "2":
        print("You run and hide.")
        break#End combat
    else:
        print("Invalid Choice")#Reloads loop, no effect on both enemy and player
  combat_mode = False #Closes loop