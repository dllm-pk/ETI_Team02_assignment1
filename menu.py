from mainprog import *
from class1 import *
import random
#Faris: Manual test
#Test values
char = characterinfo("The Hero",random.randint(30,50),random.randint(40,60),random.randint(10,20),100,False,100)
rat = enemyinfo("Rat",random.randint(10,20),random.randint(20,30),random.randint(1,5),100,100)
ratking = enemyinfo("Rat King",random.randint(30,50),random.randint(40,60),random.randint(10,20),100,100)
day = 1

#Menu for testing rest (Faris)
testmenu = True
while testmenu == True:
    print("Today is Day " +str(day))
    print("Your stats.")
    char.toString
    a = input("(1) rest (2) combat (3) Orb of Power (4) View Character (0) stop test: ")
    if a == "1":
        restresult = rest(day,char)
        day = restresult[0]
        char.hp = restresult[1]
    elif a == "2":
        char.hp = enemy(char,rat)
    elif a == "3":
        orb = orb(char)
        char.minDamage = orb[0]
        char.maxDamage = orb[1]
        char.defence = orb[2] 
        OOP = True
    elif a == "4":
        char.toString
    elif a == "0":
        testmenu = False
        break
    else:
        print("Invalid Choice")

