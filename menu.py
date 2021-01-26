from mainprog import *
#Faris: Manual test
#Test values
min = 1
max = 3
defn = 1
hp = 10
maxuserhp = 100
user_hp = 50
user_defence = 1
day = 1

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
