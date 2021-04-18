import rolls
from random import sample
from Classes.GenClass import GenClass
class Fighter(GenClass):
    def __init__(self, extra = None):
        super(Fighter, self).__init__()
        self.hitDie = rolls.d10
        self.className = "Fighter"
        self.as_id = None
        self.cs_id = None
        self.indomitable_id = None
        self.allFightingStyles = ["Archery", "Defense", "Dueling", "Great Weapon Fighting", "Protection", "Two-Weapon Fighting"]
        if extra is None:
            self.fightingStyle = None
            self.martialArchetype = None
            self.primaryAbility = sample(["Strength", "Dexterity"],1)[0]
            # self.maneuver = None
        else:
            self.primaryAbility = extra["primaryAbility"]
            self.fightingStyle = extra["fightingStyle"]
            self.martialArchetype = extra["martialArchetype"]
            # self.maneuver = extra["maneuver"]
        
        self.savingThrowProficiencies = ["Strength", "Constitution"]
        self.armorWeaponProficiencies = ["All Armor", "Shields", "Simple Weapons", "Martial Weapons"]

    def getFightingStyleFeatures(self, fs=None):
        if fs is None:
            fs = self.fightingStyle
        if fs == "Archery":
            self.rangeAttackBonus += 2
        elif fs == "Defense":
            self.acMod.append(1)
        elif fs == "Dueling":
            self.meleeDamageBonus += 2

    def getMartialArchetype(self):
        if self.martialArchetype is None:
            self.martialArchetype = sample(["Champion", "Battle Master", "Eldritch Knight"],1)[0]

    def getMartialArchetypeFeature(self, level):
        if self.martialArchetype == "Champion":
            if level == 3:
                self.classFeatures.append(self.martialArchetype + ": " + "Improved Critical")
            elif level == 7:
                self.classFeatures.append(self.martialArchetype + ": " + "Remarkable Athlete")
            elif level == 10:
                curStr = self.martialArchetype + ": " + "Additional Fighting Style: "
                while True:
                    newStyle = sample(self.allFightingStyles,1)[0]
                    if newStyle == self.fightingStyle:
                        continue
                    break
                curStr += newStyle
                self.classFeatures.append(curStr)
                self.getFightingStyleFeatures(newStyle)
            elif level == 15:
                self.classFeatures.append(self.martialArchetype + ": " + "Superior Critical")
            elif level == 18:
                self.classFeatures.append(self.martialArchetype + ": " + "Survivor")
        elif self.martialArchetype == "Battle Master":
            if level == 3:
                self.cs_id = len(self.classFeatures)
                self.classFeatures.append(self.martialArchetype + ": " + "Combat Superiority (d8)")
                self.classFeatures.append(self.martialArchetype + ": " + "Student of War")
            elif level == 7:
                self.classFeatures.append(self.martialArchetype + ": " + "Know Your Enemy")
            elif level == 10:
                self.classFeatures[self.cs_id] = self.martialArchetype + ": " + "Combat Superiority (d10)"
            elif level == 15:
                self.classFeatures.append(self.martialArchetype + ": " + "Relentless")
            elif level == 18:
                self.classFeatures[self.cs_id] = self.martialArchetype + ": " + "Combat Superiority (d12)"

    def pickSkills(self):
        self.profSkills = sample(["acrobatics", "animal handling", "athletics", "history", "insight", "intimidation", "perception", "survival"], 2)

    def getFeatures(self, level):
        if level == 1:
            self.pickSkills()
            self.classFeatures.append("Second Wind")
            if self.fightingStyle is None:
                self.fightingStyle = sample(self.allFightingStyles,1)[0]
            self.getFightingStyleFeatures()
            self.classFeatures.append("Fighting Style: %s" % (self.fightingStyle))
        elif level == 2:
            self.as_id = len(self.classFeatures)
            self.classFeatures.append("Action Surge (1 Use)")
        elif level == 3:
            self.getMartialArchetype()
        elif level == 5:
            self.numAttacks += 1
        elif level == 6:
            self.needAbilityScoreImprovement = True
        elif level == 8:
            self.needAbilityScoreImprovement = True
        elif level == 9:
            self.indomitable_id = len(self.classFeatures)
            self.classFeatures.append("Indomitable (1 Use)")
        elif level == 11:
            self.numAttacks += 1
        elif level == 12:
            self.needAbilityScoreImprovement = True
        elif level == 13:
            self.classFeatures[self.indomitable_id] = "Indomitable (2 Uses)"
        elif level == 14:
            self.needAbilityScoreImprovement = True
        elif level == 16:
            self.needAbilityScoreImprovement = True
        elif level == 17:
            self.classFeatures[self.as_id] = "Action Surge (2 Uses)"
            self.classFeatures[self.indomitable_id] = "Indomitable (3 Uses)"
        elif level == 20:
            self.numAttacks += 1

        if level >= 3:
            self.getMartialArchetypeFeature(level)

    def levelUp(self, level):
        self.getFeatures(level)
        self.updateSkills(level)