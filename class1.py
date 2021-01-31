class enemyinfo():
    def __init__(self, name, minDamage, maxDamage, defence,hp,maxhp):
        self.name = name
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.defence = defence
        self.hp = hp
        self.maxhp = maxhp
    def toString(self):
            print("Encounter - {}".format(self.name))
            print("Damage: {0} - {1}".format(self.minDamage,self.maxDamage))
            print("Defence: {}".format(self.defence))
            print("HP: {0}/{1}".format(self.hp,self.maxhp))
class characterinfo():
    def __init__(self, name, minDamage, maxDamage, defence,hp,oop,maxhp):
        self.name = name
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.defence = defence
        self.hp = hp
        self.oop = oop
        self.maxhp = maxhp
    def toString(self):
            print(string(self.name))
            print("Damage: {0} - {1}".format(self.minDamage,self.maxDamage))
            print("Defence: {}".format(self.defence))
            print("HP: {0}/{1}".format(self.hp,self.maxhp))