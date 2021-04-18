import spells
from random import randint
from skills import skill2atribute
class GenClass:
    def __init__(self, extra=None):
        self.hitDie = None
        self.className = None
        self.primaryAbility = None
        self.savingThrowProficiencies = None
        self.armorWeaponProficiencies = None
        self.classFeatures = list()
        self.numAttacks = 1
        self.speedMod = 0
        self.meleeAttackBonus = 0
        self.rangeAttackBonus = 0
        self.meleeDamageBonus = 0
        self.rangeDamageBonus = 0
        self.extraCritWeaponDice = 0
        self.acMod = ["dexterity"]
        self.atributeValueMod = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0
        }
        self.profSkills = list()
        self.expertSkills = list()
        self.spellSaveAtr = None
        self.spellAttackAtr = None
        self.skills = dict()
        for key in skill2atribute.keys():
            self.skills[key] = 0
        self.spells = dict()
        self.spellStructure = list()
        self.extraLanguages = 0
        self.needAbilityScoreImprovement = False

    def levelUp(self, level):
        pass
    
    def getFeatures(self, level):
        pass

    def getNewSpells(self, extraSpells, className):
        for lvl in range(len(extraSpells)):
            if lvl == 1:
                continue
            for k in range(extraSpells[lvl]):
                while True:
                    newSpell = spells.getRandomSpell(max(0, lvl-1), className)
                    spellName, spellContents = list(newSpell.items())[0]
                    if spellName in self.spells.keys():
                        continue
                    self.spells.update(newSpell)
                    break

    def pickSkills(self):
        pass

    def getProfBonus(self, level):
        return 2 + (level-1)//4

    def updateSkills(self, level):
        profBonus = self.getProfBonus(level)
        for key in self.skills.keys():
            if key in self.profSkills:
                self.skills[key] = profBonus
            else:
                self.skills[key] = 0
        for key in self.expertSkills:
            self.skills[key] += profBonus
    
    def pickExpertise(self, numExpert=2):
        stats = self.profSkills
        numProfs = len(stats)
        numPicked = 0
        while True:
            if numProfs == len(self.expertSkills):
                break
            curStat = stats[randint(1,numProfs)-1]
            if curStat in self.expertSkills:
                continue
            self.expertSkills.append(curStat)
            numPicked += 1
            if numPicked == numExpert:
                break