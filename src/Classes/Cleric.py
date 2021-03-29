import rolls
from spells import getSpell
from random import randint, sample
from Classes.GenClass import GenClass
class Cleric(GenClass):
    def __init__(self, extra = None):
        super(Cleric, self).__init__()
        self.hitDie = rolls.d8
        self.className = "Cleric"
        self.primaryAbility = "Wisdom"
        self.savingThrowProficiencies = ["Wisdom", "Charisma"]
        self.armorWeaponProficiencies = ["Light Armor", "Medium Armor", "Shields", "Simple Weapons"]
        self.spellAttackAtr = "Wisdom"
        self.spellSaveAtr = "Wisdom"
    
        if extra is None:
            self.divineDomain = None
        else:
            self.divineDomain = extra

        self.cd_id = 0
        self.du_id = 0
        self.di_id = 0


    def getFeatures(self, level):
        if level == 1:
            self.pickSkills()
            self.classFeatures.append("Spellcasting")
            self.getDivineDomain()
        elif level == 2:
            self.cd_id = len(self.classFeatures)
            self.classFeatures.append("Channel Divinity (1/rest)")
            self.divineDomainFeature(level)
        elif level == 5:
            self.du_id = len(self.classFeatures)
            self.classFeatures.append("Destroy Undead (CR 1/2)")
        elif level == 6:
            self.classFeatures[self.cd_id] = "Channel Divinity (2/rest)"
            self.divineDomainFeature(level)
        elif level == 8:
            self.classFeatures[self.du_id] = "Destroy Undead (CR 1)"
            self.divineDomainFeature(level)
        elif level == 10:
            self.di_id = len(self.classFeatures)
            self.classFeatures.append("Divine Intervention")
        elif level == 11:
            self.classFeatures[self.du_id] = "Destroy Undead (CR 2)"
        elif level == 14:
            self.classFeatures[self.du_id] = "Destroy Undead (CR 3)"
        elif level == 17:
            self.classFeatures[self.du_id] = "Destroy Undead (CR 4)"
            self.divineDomainFeature(level)
        elif level == 18:
            self.classFeatures[self.cd_id] = "Channel Divinity (3/rest)"
        elif level == 20:

            self.classFeatures[self.di_id] = "Divine Intervention [Improvement]"

    def getDivineDomain(self):
        if self.divineDomain is None:
            self.divineDomain = "Light" # sample(["Knowledge", "Life", "Light", "Nature", "Tempest", "Trickery", "War"], 1)[0]
        self.divineDomainFeature(1)

    def divineDomainFeature(self, level):
        if self.divineDomain == "Knowledge":
            self.getKnowledgeDomainFeature(level)
        elif self.divineDomain == "Life":
            self.getLifeDomainFeature(level)
        elif self.divineDomain == "Light":
            self.getLightDomainFeature(level)
        elif self.divineDomain == "Nature":
            self.getNatureDomainFeature(level)
        elif self.divineDomain == "Tempest":
            self.getTempestDomainFeature(level)
        elif self.divineDomain == "Trickery":
            self.getTrickeryDomainFeature(level)
        elif self.divineDomain == "War":
            self.getWarDomainFeature(level)

    def getKnowledgeDomainFeature(self, level):
        if level == 1:
            self.classFeatures.append("Knowledge Domain: Blessings of Knowledge")
            self.addSkills()
            self.extraLanguages += 2
        elif level == 2:
            self.classFeatures.append("Knowledge Domain: Channel Divinity (Knowledge of the Ages)")
        elif level == 6:
            self.classFeatures.append("Knowledge Domain: Channel Divinity (Read Thoughts)")
        elif level == 8:
            self.classFeatures.append("Knowledge Domain: Potent Spellcasting")
        elif level == 17:
            self.classFeatures.append("Knowledge Domain: Visions of the Past")

    def getLifeDomainFeature(self, level):
        f = "Life Domain: "
        if level == 1:
            self.armorWeaponProficiencies.append("Heavy Armor")
            self.classFeatures.append(f + "Disciple of Life")
        elif level == 2:
            self.classFeatures.append(f + "Channel Divinity (Preserve Life)")
        elif level == 6:
            self.classFeatures.append(f + "Blessed Healer")
        elif level == 8:
            self.classFeatures.append(f + "Divine Strike")
        elif level == 17:
            self.classFeatures.append(f + "Supreme Healing")

    def getLightDomainFeature(self, level):
        f = "Light Domain: "
        if level == 1:
            curSpells = self.spells.keys()
            if not "light" in curSpells:
                self.spells.update(getSpell('Light'))

            self.classFeatures.append(f + "Warding Flare")
        elif level == 2:
            self.classFeatures.append(f + "Channel Divinity (Radiance of the Dawn)")
        elif level == 6:
            self.classFeatures.append(f + "Improved Flare")
        elif level == 8:
            self.classFeatures.append(f + "Potent Spellcasting")
        elif level == 17:
            self.classFeatures.append(f + "Corona of Light")

    def getNatureDomainFeature(self, level):
        pass

    def getTempestDomainFeature(self, level):
        pass

    def getTrickeryDomainFeature(self, level):
        pass

    def getWarDomainFeature(self, level):
        pass

    def addSkills(self):
        avalSkills = ["arcana", "history", "nature", "religion"]
        newSkills = sample(avalSkills, 2)
        for s in newSkills:
            self.expertSkills.append(s)
            if s in self.profSkills:
                continue
            self.profSkills.append(s)

    def pickSkills(self):
        self.profSkills = ["religion", sample(["history", "insight", "medicine", "persuasion"],1)[0]]
        

    def getSpells(self, level):
        pass

    def levelUp(self, level):
        self.getFeatures(level)
        self.getSpells(level)
        self.updateSkills(level)
    
    def getSpells(self, level):
        if level == 1:
            self.spellStructure = _clericSpells[1]
            return
        newAddition = _clericSpells[level]
        for k in range(len(newAddition)):
            self.spellStructure[k] += newAddition[k]

_clericSpells = {
    # Each row is the increase in the number
    #l: [0  #  1  2  3  4  5  6  7  8  9]
     1: [3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
     2: [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     3: [0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0],
     4: [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     5: [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
     6: [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     7: [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     8: [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     9: [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    10: [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    11: [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    12: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    13: [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    14: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    15: [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    16: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    17: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    18: [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    19: [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    20: [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
}