import rolls
from random import randint, sample
from Classes.GenClass import GenClass
class Bard(GenClass):
    def __init__(self, extra=None):
        super(Bard, self).__init__()
        self.hitDie = rolls.d8
        self.className = "Bard"
        self.primaryAbility = "Charisma"
        self.savingThrowProficiencies = ["Dexterity", "Charisma"]
        self.armorWeaponProficiencies = ["Light Armor", "Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers", "Shortswords"]
        self.spellAttackAtr = "Charisma"
        self.spellSaveAtr = "Charisma"

        if extra is None:
            self.collegePath = None
        else:
            self.collegePath = extra

    def getSpells(self, level):
        pass

    def getFeatures(self, level):
        if level == 1:
            self.classFeatures.append('Spellcasting')
            self.classFeatures.append("Bardic Inspiration (d6)")
            self.pickSkills()
        elif level == 2:
            self.classFeatures.append("Jack of All Trades")
            self.classFeatures.append("Song of Rest (d6)")
        elif level == 3:
            self.setBardCollege()
            self.classFeatures.append("Expertise")
            self.pickExpertise(2)
        elif level == 5:
            self.classFeatures[1] = "Bardic Inspiration (d8)"
            self.classFeatures.append("Font of Inspiration")
        elif level == 6:
            self.classFeatures.append("Countercharm")
            self.bardCollege(level)
        elif level == 9:
            self.classFeatures[3] = "Song of Rest (d8)"
        elif level == 10:
            self.classFeatures[1] = "Bardic Inspiration (d10)"
            self.pickExpertise(2)
            self.classFeatures.append("Magical Secrets")
            self.gainSpells(2, 'any')
        elif level == 13:
            self.classFeatures[3] = "Song of Rest (d10)"
        elif level == 14:
            self.gainSpells(2, 'any')
            self.bardCollege(level)
        elif level == 15:
            self.classFeatures[1] = "Bardic Inspiration (d12)"
        elif level == 17:
            self.classFeatures[3] = "Song of Rest (d12)"
        elif level == 18:
            self.gainSpells(2, 'any')
        elif level == 20:
            self.classFeatures.append("Superior Inspiration")
        
    def setBardCollege(self):
        if self.collegePath is None:
            collegeId = randint(1,2)
            if collegeId == 1:
                self.collegePath = "College of Lore"
            elif collegeId == 2:
                self.collegePath = "College of Valor"
        self.bardCollege(3)

    def bardCollege(self, level):
        if self.collegePath == "College of Lore":
            if level == 3:
                self.gainSkills(3)
                self.classFeatures.append("College of Lore: Cutting Words")
            elif level == 6:
                self.gainSpells(2,'any')
                self.classFeatures.append("College of Lore: Additional Magical Secrets")
            elif level == 14:
                self.classFeatures.append("College of Lore: Peerless Skill")
        elif self.collegePath == "College of Valor":
            if level == 3:
                self.armorWeaponProficiencies.append("Medium Armor")
                self.armorWeaponProficiencies.append("Shields")
                self.armorWeaponProficiencies.append("Martial Weapons")
                self.classFeatures.append("College of Valor: Combat Inspiration")
            elif level == 6:
                self.classFeatures.append("College of Valor: Extra Attack")
                self.numAttacks += 1
            elif level == 14:
                self.classFeatures.append("College of Valor: Battle Magic")

    def gainSpells(self, numSpells, spellType):
        pass

    def gainSkills(self, numSkills):
        foundSkills = 0
        skills = self.skills.keys()
        while True:
            randSkill = sample(skills,1)[0]
            print(randSkill)
            if randSkill in self.profSkills:
                continue
            self.profSkills.append(randSkill)
            foundSkills += 1
            if foundSkills == numSkills:
                break
            if len(skills) == len(self.profSkills):
                break

    def pickSkills(self):
        stats = self.skills.keys()
        self.profSkills = sample(stats,3)

    def updateJAT(self, level):
        if level == 1:
            return
        halfProf = self.getProfBonus(level)//2
        for key in self.skills.keys():
            if key in self.profSkills:
                continue
            if key in self.expertSkills:
                continue
            self.skills[key] = halfProf

    def levelUp(self, level):
        self.getFeatures(level)
        self.getSpells(level)
        self.updateSkills(level)
        self.updateJAT(level)

