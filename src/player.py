
import races
import rolls
import skills
import classes
import atributes
import features

class Player:
    def __init__(self):
        self.health = 0
        self.maxHealth = 0
        self.tempHealth = 0
        self.atributes = atributes.Atributes()
        self.skills = dict()
        self.races = races.Races()
        self.classes = classes.Classes()
        self.level = 0
        self.exp = 0
        self.ac = 0
        self.proficiencyBonus = 0
        self.alignment = None
        self.initiative = 0
        self.features = list()
        self.spells = dict()

    def create(self, race, className, level=1, subrace=None, atributes=None):
        self.level = 0
        self.races.setRace(race, subrace)
        self.classes.setClass(className)
        if atributes is None:
            self.atributes.rollAtributes()
        else:
            self.atributes.setAtributes(atributes)
        self.addAtributeModifiers()
        self.levelUp(level)

    def createRandom(self,level=1):
        self.level = 0
        self.races.getRandom()
        self.classes.getRandom()
        self.atributes.rollAtributes()
        self.addAtributeModifiers()
        self.levelUp(level)

    def rollInitiative(self):
        val = rolls.d20() + self.atributes.modifiers['dexterity']
        return val
    
    def addAtributeModifiers(self):
        # Add atribute modifiers from race
        raceModifiers = self.races.info.modstats
        keys = raceModifiers.keys()
        for key in keys:
            self.atributes.values[key] += raceModifiers[key]

        # Add atribute modifiers from background or other...
        
        self.atributes.setModifiers()
        return
    
    def levelUp(self, newLevel):
        if self.level > 1:
            self.health -= self.level*self.atributes.modifiers["constitution"]
            self.maxHealth -= self.level*self.atributes.modifiers["constitution"]
        while self.level < newLevel:
            self.level += 1
            if self.level == 1:
                self.health = classes._HitDie[self.classes.info.className]
                self.maxHealth = classes._HitDie[self.classes.info.className]
            else:
                dieRoll = self.classes.info.hitDie()
                self.health += dieRoll
                self.maxHealth += dieRoll

            # Call class specific level ups
            self.classes.info.levelUp(self.level)
            self.atributes.addClassMods(self.classes.info.atributeValueMod)
            if ((self.level % 4 == 0 or self.level == 19) and self.level != 20) or self.classes.info.needAbilityScoreImprovement:
                self.classes.info.needAbilityScoreImprovement = False
                for k in range(2):
                    atribute_name = self.chooseAtributeToIncrease()
                    if atribute_name is None:
                        break
                    print("increasing", atribute_name)
                    self.atributes.values[atribute_name] += 1
        self.atributes.setModifiers()
        self.health += self.level*self.atributes.modifiers["constitution"]
        self.maxHealth += self.level*self.atributes.modifiers["constitution"]
        self.proficiencyBonus = self.classes.info.getProfBonus(self.level)
        self.updateAC()
        self.initiative = self.atributes.modifiers['dexterity']
        self.updateFeatures()
        self.updateSpells()
        # Update skills
        for key in self.classes.info.skills.keys():
            self.skills[key] = self.classes.info.skills[key] + self.atributes.modifiers[skills.skill2atribute[key]]
    
    def updateAC(self):
        self.ac = 10
        for k in self.classes.info.acMod:
            try:
                self.ac += self.atributes.modifiers[k]
            except:
                self.ac += k

    def updateFeatures(self):
        vals = list()
        # Get Race Features
        for key in self.races.info.features["features"].keys():
            curStr = self.races.info.features["features"][key]
            curStr_split = curStr.split(':')
            curStr_strip = curStr_split[0].strip()
            vals.append(curStr_strip)
        # Get Class Features
        for key in self.classes.info.classFeatures:
            vals.append(key)
        self.features = vals
    
    def updateSpells(self):
        # Get Class Spells
        for key in self.classes.info.spells.keys():
            self.spells[key] = self.classes.info.spells[key]
        
        # Update spell structure
        self.spellStructure = self.classes.info.spellStructure # Plus others


    def chooseAtributeToIncrease(self):
        # Here is where we can add logic to better choose how and when an atribute increases.
        # Right now it prioritizes con, after that it goes in atribute order (str->dex->...).
        # How to choose should be class specific and we will probably want to write a function
        # for each class on how to choose the atribute.
        vals2increase = list()
        for key in self.atributes.modifiers.keys():
            if self.atributes.values[key] < self.atributes.maxValue[key]:
                vals2increase.append(key)
        if "constitution" in vals2increase:
            return "constitution"
        else:
            if len(vals2increase) > 0:
                return vals2increase[0]
            else:
                return None
