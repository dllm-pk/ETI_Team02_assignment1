from mainprog import *
from class1 import *
from random import *
#Faris: Manual test
#Test values
"""
Code below help with the creation of the values for the functions
"""
charstat = randint(30,50)
#charstat = character minimum damage
ratstat = randint(10,20)
#ratstat = rat minimum damage
rkstat = randint(30,50)
#rkstat = ratking minimum damage
char = characterinfo("The Hero",charstat,charstat+randint(5,10),randint(10,20),100,False,100)
#char = player
rat = enemyinfo("Rat",ratstat,ratstat+randint(5,10),randint(1,5),100,100)
#rat = generic enemy
ratking = enemyinfo("Rat King",rkstat,rkstat+randint(5,10),randint(10,20),100,100)
#ratking = boss
day = 1
#day = day in game

#Menu for testing rest (Faris)
testmenu = True
"""
Loop menu for testing (Faris)
"""
while testmenu == True:
    if (char.hp <= 0):
        testmenu = False
        break
    print("Today is Day " +str(day))
    print("Your stats.")
    char.toString()
    a = input("(1) rest (2) combat (3) Orb of Power (4) View Character (0) stop test: ")
    if a == "1":
        """
        Rest system call function (Faris)
        """
        restresult = rest(day,char)
        day = restresult[0]
        char.hp = restresult[1]
    elif a == "2":
        """
        Rat encounter test function (Faris)
        """
        result = enemy(char,rat)
        char.hp = result[0]
        if result[1] == True:
            testmenu = False
            break
    elif a == "3":
        """
        Orb encounter test function (Faris)
        """
        orb = orb(char)
        char.minDamage = orb[0]
        char.maxDamage = orb[1]
        char.defence = orb[2] 
        OOP = True
    elif a == "4":
        """
        View Character (Faris)
        """
        characterview(char)
   


    elif a == "5":
        """
        Ends menu (Faris), exits game
        """
        exit = input("Type \"Exit\" to confirm exit, anything else to return: ").upper()
        if exit == "EXIT":
            saveloop = True
            if saveloop == True:
                save = input("Do you want to save? (Y/N): ").upper()
                if save == "Y":
                    print("Saving...")
                    #Save Function
                    saveloop = False
                elif save.upper == "N":
                    saveloop = False
            if saveloop == False:
                print("Exiting Game.")
                break
        else:
            break

        

        testmenu = False
        break
    else:
        """
        Error Validation (Faris)
        """
        print("Invalid Choice")

