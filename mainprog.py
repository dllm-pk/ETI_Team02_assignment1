import combat


def orb(min,max,user_defence):
    print("You found the Orb of Power!")
    min += 5
    max += 5
    print("Min = {0}, Max = {1}".format(min,max))
    print("Your attack has increased by 5")
    print("Min = {0}, Max = {1}".format(min,max))
    user_defence += 5
    print("Your defence has increased by 5")
    result = [min,max,user_defence]
    return result

#Orb of Power (Faris)


def enemy(min,max,defn,hp,user_hp,maxuserhp,user_defence):
    #Menu for combat
    combat_mode = True #Ensures loop functionality
    while combat_mode == True: #Loop for combat menu
        print("Encounter! - Rat \nDamage: {0} - {1} \nDefence: {2} \nHP: {3} \n\n1) Attack \n2) Run".format(min,max,defn,hp))
        choice = input("Enter Choice: ")#Menu choice
        print(" ")
        if choice == "1":#Attack
            hit = combat.attack(min,max,defn)#damage to rat
            print("You deal {} damage to the rat".format(hit))
            hp = hp - hit
            if hp <= 0:#rat hp below zero
                print("The Rat is dead! You are victorious!")
                break#End combat
                combat_mode = False
            else:
                tackle = combat.enemy_attack(user_defence)#damage to player
                print("Ouch! The Rat hit you for {} damage! \n".format(tackle))
                user_hp = user_hp - tackle
                if user_hp <= 0:
                    user_hp = 0#player's HP cant go below 0
                print("You have {} HP left.".format(user_hp))
                if user_hp <= 0:
                    print("Your HP is zero. You are dead")
                    break#End combat
                    combat_mode = False
        elif choice == "2":
            print("You run and hide.")
            break#End combat
            combat_mode = False
        else:
            print("Invalid Choice")#Reloads loop, no effect on both enemy and player
        while combat_mode == False:
            return user_hp
def rest(day,user_hp,maxuserhp):
    day = day + 1
    new_user_hp = 0
    new_user_hp = user_hp + 20
    if new_user_hp <= maxuserhp:
            print("You are fully healed.")
    elif new_user_hp >= maxuserhp: #Makes sure hp is fully healed
            new_user_hp = maxuserhp
            print("You are fully healed.")
    return [day,new_user_hp]





