import combat
from class1 import *
from menu import *

def orb(char):
    """
    Orb of Power, if found, a list is returned to override the user stats
    """
    print("You found the Orb of Power!")
    min = char.minDamage + 5
    max = char.maxDamage + 5
    print("Your attack has increased by 5")
    print("Min = {0}, Max = {1}".format(min,max))
    user_defence = char.defence + 5
    print("Your defence has increased by 5")
    result = [min,max,user_defence]
    return result

#Orb of Power (Faris)


def enemy(char, enemy):
    """
    Enemy Battle Menu, list is returned to minus off player's HP and show ratking defeated
    """
    defeat_ratking = False
    #Menu for combat
    combat_mode = True 
    
    while combat_mode == True: #Loop for combat menu
        user_hp = char.hp
        enemy.toString()
        print("(1) Attack (2) Run")
        choice = input("Enter Choice: ")#Menu choice
        print(" ")
        if choice == "1":
            """
            Attack
            """
            if enemy.name == "Rat King":
                """
                Attacking Ratking
                """
                hit = combat.ratkingattack(char, enemy)#damage to rat king
            else:
                """
                Attacking Rat
                """
                hit = combat.attack(char,enemy)#damage to rat
            print("You deal {0} damage to the {1}".format(hit,enemy.name))
            """
             Hit = hp lost, enemy hp is subtracted
             """
            enemy.hp = enemy.hp - hit
            if enemy.hp <= 0:#rat hp below zero
                """
                Rat dies, end
                """
                print("The {} is dead! You are victorious!".format(enemy.name))
                if enemy.name == "Rat King":
                    """
                    If Ratking defeated, override main menu with ending
                    """
                    defeat_ratking = True
                break#End combat
                combat_mode = False
            else:

                """
                Enemy/Ratking attacks player
                """
                hit = combat.enemy_attack(char.defence)#damage to player
                print("Ouch! The {0} hit you for {1} damage! \n".format(enemy.name,hit))
                user_hp = user_hp - hit
                if user_hp <0:
                    """
                    Sets hp to be zero
                    """
                    user_hp = 0#player's HP cant go below 0
                print("You have {} HP left.".format(user_hp))
                if user_hp <= 0:
                    """
                    Ends combat as player dies
                    """
                    print("Your HP is zero. You are dead")
                    break#End combat
                    combat_mode = False
        elif choice == "2":
            """
             Run, ends combat
             """
            print("You run and hide.")
            break#End combat
            combat_mode = False
        else:
            print("Invalid Choice")#Reloads loop, no effect on both enemy and player
        while combat_mode == False:
            return [user_hp,defeat_ratking]
def rest(day, char):
    """
    Rest function: A day passes and a list is returned to override day and user HP
    """
    day = day + 1
    new_user_hp = char.hp + 20
    if new_user_hp <= char.maxhp:
        """
        Show that user is healed
        """
        print("You are fully healed.")
    elif new_user_hp > char.maxhp: #Makes sure hp is fully healed
        """
        Sets the new user hp to max hp if difference between user hp and max hp is less than tw3nty
        """
        new_user_hp = char.maxhp
        print("You are fully healed.")
    return [day,new_user_hp]
def characterview(char):
    """
     Allows the player to view stats
    """
    char.toString()
    if char.oop == True:
                print("You are holding the Orb of Power.")





