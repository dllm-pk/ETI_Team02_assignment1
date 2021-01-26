import combat

#Faris: combat manual test
#Test values
min = 1
max = 3
defn = 1
hp = 10
maxuserhp = 100
user_hp = 50
user_defence = 1
day = 1
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

#Menu for testing rest (Faris)
testmenu = True
while testmenu == True:
    print("Today is Day " +str(day))
    print("Your stats. Damage: {0}-{1} HP:{2} Defence {3}".format(min,max,user_hp,user_defence))
    a = input("(1) rest (2) combat (3) Orb of Power (0) stop test: ")
    if a == "1":
        restresult = rest(day,user_hp,maxuserhp)
        day = restresult[0]
        user_hp = restresult[1]
    elif a == "2":
        user_hp = enemy(min,max,defn,hp,user_hp,maxuserhp,user_defence)
    elif a == "3":
        orb = orb(min,max,user_defence)
        min = orb[0]
        max = orb[1]
        user_defence = orb[2]
    elif a == "0":
        testmenu = False
        break
    else:
        print("Invalid Choice")



