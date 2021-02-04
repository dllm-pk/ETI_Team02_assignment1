from mainprog import *
from class1 import *
import random
#Faris: Manual test
#Test values
"""
Code below help with the creation of the values for the functions
"""
char = characterinfo("The Hero",random.randint(30,50),char.minDamage+random.randint(5,10),random.randint(10,20),100,False,100)
rat = enemyinfo("Rat",random.randint(10,20),rat.minDamage+random.randint(5,10),random.randint(1,5),100,100)
ratking = enemyinfo("Rat King",random.randint(30,50),ratking.minDamage+random.randint(5,10),random.randint(10,20),100,100)
day = 1

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
    char.toString
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
        char.toString
    elif a == "0":
        """
        Ends menu (Faris)
        """
        testmenu = False
        break
    else:
        """
        Error Validation (Faris)
        """
        print("Invalid Choice")

