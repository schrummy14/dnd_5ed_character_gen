import rolls
from random import randint
from Classes.GenClass import GenClass
class Barbarian(GenClass):
    def __init__(self, extra=None): # Extra sets the primal path
        super(Barbarian, self).__init__()
        self.hitDie = rolls.d12
        self.className = "Barbarian"
        self.primaryAbility = "Strength"
        self.savingThrowProficiencies = ["Strength", "Constitution"]
        self.armorWeaponProficiencies = ["Light Armor", "Medium Armor", "Shields", "Simple Weapons", "Martial Weapons"]
        if extra is None:
            self.primalPath = None
        else:
            self.primalPath = extra[0]
            self.primalPathExtra = extra[1]

        self.lvl = [9, 16, 22]
        self.rgd = [2,  3,  4]

    def getNumRages(self, level):
        if level < 3:
            return 2
        elif level < 6:
            return 3
        elif level < 12:
            return 4
        elif level < 17:
            return 5
        elif level < 20:
            return 6
        else:
            return 99
    
    def getRageDamage(self, level):
        if level < 37:
            for k in range(len(self.lvl)):
                if level < self.lvl[k]:
                    return self.rgd[k]
            else:
                self.lvl.append(2*self.lvl[-1] - self.lvl[-2])
                self.rgd.append(self.rgd[-1] + 1)
                return self.rgd[-1]
        elif level == 37:
            self.rgd = self.rgd[-1] + 1
        else:
            self.rgd += 1
        return self.rgd

    def getFeatures(self, level):
        if level == 1:
            self.classFeatures.append('Unarmored Defense')
            self.acMod = ['dexterity', 'constitution']
        elif level == 2:
            self.classFeatures.append('Reckless Attack')
            self.classFeatures.append('Danger Sense')
        elif level == 3:
            self.setPrimalPath()
        elif level == 5:
            self.classFeatures.append('Extra Attack')
            self.numAttacks += 1
            self.classFeatures.append('Fast Movement')
            self.speedMod += 10
        elif level in [6, 10, 14]:
            self.getPathFeature(level)
        elif level == 7:
            self.classFeatures.append('Feral Instinct')
        elif level in [9, 13, 17]:
            if level == 9:
                self.classFeatures.append('Brutal Critical')
            self.extraCritWeaponDice += 1
        elif level == 11:
            self.classFeatures.append('Relentless Rage')
        elif level == 15:
            self.classFeatures.append('Persistent Rage')
        elif level == 18:
            self.classFeatures.append('Indomitable Might')
        elif level == 20:
            self.classFeatures.append('Primal Champion')
            self.atributeValueMod["strength"] += 4
            self.atributeValueMod["constitution"] += 4
                

    def setPrimalPath(self):
        if self.primalPath is None:
            if randint(1,2) == 1:
                self.primalPath = 'Path of the Berserker'
            else:
                self.primalPath = 'Path of the Totem Warrior'
                totems = ['Bear', 'Eagle', 'Wolf']
                self.primalPathExtra = totems[randint(0,2)]

        self.getPathFeature(3)

    def getPathFeature(self, level):
        if self.primalPath == 'Path of the Berserker':
            self.getBerserker(level)
        else:
            self.getWarrior(level)

    def getWarrior(self, level):
        f = 'Path of the Totem Warrior (%s): ' % (self.primalPathExtra)
        if level == 3:
            self.classFeatures.append(f + 'Spirit Seeker')
            self.classFeatures.append(f + 'Totem Spirit')
        elif level == 6:
            self.classFeatures.append(f + 'Aspect of the Beast')
        elif level == 10:
            self.classFeatures.append(f + 'Spirit Walker')
        elif level == 14:
            self.classFeatures.append(f + 'Totemic Attunement')


    def getBerserker(self, level):
        f = 'Path of the Berserker: '
        if level == 3:
            self.classFeatures.append(f + 'Frenzy')
        elif level == 6:
            self.classFeatures.append(f + 'Mindless Rage')
        elif level == 10:
            self.classFeatures.append(f + 'Intimidating Presence')
        elif level == 14:
            self.classFeatures.append(f + 'Retaliation')

    def levelUp(self, level):
        self.getFeatures(level)
        pass
