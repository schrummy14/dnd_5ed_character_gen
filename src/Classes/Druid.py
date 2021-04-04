import rolls
import spells
from random import sample
from Classes.GenClass import GenClass
class Druid(GenClass):
    def __init__(self, extra = None):
        super(Druid, self).__init__()
        self.hitDie = rolls.d8
        self.className = "Druid"
        self.primaryAbility = "Wisdom"
        self.savingThrowProficiencies = ["Intelligence", "Wisdom"]
        self.armorWeaponProficiencies = [
            "Light Armor (nonmetal)", "Medium Armor (nonmetal)", "Shields (nonmetal)", "Clubs", "Daggers",
            "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears"]
        
        if extra is None:
            self.circle = None
            self.homeLand = None
        else:
            self.circle = extra[0]
            self.homeLand = extra[1]

        self.ws_id = 0

    def levelUp(self, level):
        self.getFeatures(level)
        self.getSpells(level)
        self.updateSkills(level)
    
    def getSpells(self, level):
        if level == 1:
            self.getNewSpells(_druidSpells[1], 'druid')
            self.spellStructure = _druidSpells[1]
            return
        self.getNewSpells(_druidSpells[level], 'druid')
        newAddition = _druidSpells[level]
        for k in range(len(newAddition)):
            self.spellStructure[k] += newAddition[k]
    
    def getDruidCircle(self):
        if self.circle is None:
            self.circle = sample(["Land", "Moon"], 1)[0]
            if self.circle == "Land":
                self.homeLand = sample(["Arctic", "Coast", "Desert", "Forest", "Grassland", "Mountain", "Swamp", "Underdark"],1)[0]
        self.druidCircle(2)

    def druidCircle(self, level):
        if self.circle == "Land":
            f = "Circle of the Land: "
            if level == 2:
                self.getNewSpells([1,0,0,0,0,0,0,0,0,0,0], 'druid')
                self.classFeatures.append(f + "Natural Recovery")
            elif level == 6:
                self.classFeatures.append(f + "Land's Stride")
            elif level == 10:
                self.classFeatures.append(f + "Nature's Ward")
            elif level == 14:
                self.classFeatures.append(f + "Nature's Sanctuary")
            
            if level in [3, 5, 7, 9]:
                self.spells.update(spells.getSpell(_landNames[self.homeLand][level][0]))
                self.spells.update(spells.getSpell(_landNames[self.homeLand][level][1]))

        elif self.circle == "Moon":
            f = "Circle of the Moon: "
            if level == 2:
                self.classFeatures.append(f + "Combat Wild Shape")
                self.classFeatures[self.ws_id] = "Wild Shape [Max Cr: 1, No Flying/Swimming]"
            if level == 4:
                self.classFeatures[self.ws_id] = "Wild Shape [Max Cr: 1, No Flying]"
            elif level == 6:
                self.classFeatures.append(f + "Primal Strike")
            elif level == 10:
                self.classFeatures.append(f + "Elemental Wild Shape")
            elif level == 14:
                self.classFeatures.append(f + "Thousand Forms")
                self.spells.update(spells.getSpell("Alter Self"))
            if level >= 6:
                newCR = level//3
                self.classFeatures[self.ws_id] = "Wild Shape [Max Cr: %d]" % (newCR)
            

    def getFeatures(self, level):
        if level == 1:
            self.classFeatures.append("Language: Druidic")
        elif level == 2:
            self.ws_id = len(self.classFeatures)
            self.classFeatures.append("Wild Shape [Max Cr: 1/4, No Flying/Swimming]")
            self.getDruidCircle()
        elif level == 4:
            self.classFeatures[self.ws_id] = "Wild Shape [Max Cr: 1/2, No Flying]"
        elif level == 8:
            self.classFeatures[self.ws_id] = "Wild Shape [Max Cr: 1]"
        elif level == 18:
            self.classFeatures.append("Timeless Body")
            self.classFeatures.append("Beast Spells")
        elif level == 20:
            self.classFeatures.append("Archdruid")
        
        if level > 2:
            self.druidCircle(level)

_druidSpells = {
    # Each row is the increase in the number
    #l: [0  #  1  2  3  4  5  6  7  8  9]
     1: [3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
     2: [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     3: [0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0],
     4: [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     5: [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
     6: [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     7: [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     8: [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     9: [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    10: [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
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

_landArctic = {
    3: ["Hold Person", "Spike Growth"],
    5: ["Sleet Storm", "Slow"],
    7: ["Freedom of Movement", "Ice Storm"],
    9: ["Commune with Nature", "Cone of Cold"]
}

_landCoast = {
    3: ["Mirror Image", "Misty Step"],
    5: ["Water Breathing", "Water Walk"],
    7: ["Control Water", "Freedom of Movement"],
    9: ["Conjure Elemental", "Scrying"]
}

_landDesert = {
    3: ["Blur", "Silence"],
    5: ["Create Food and Water", "Protection from Energy"],
    7: ["Blight", "Hallucinatory Terrain"],
    9: ["Insect Plague", "Wall of Stone"]
}

_landForest = {
    3: ["Barkskin", "Spider Climb"],
    5: ["Call Lightning", "Plant Growth"],
    7: ["Divination", "Freedom of Movement"],
    9: ["Commune with Nature", "Tree Stride"]
}

_landGrassland = {
    3: ["Invisibility", "Pass without Trace"],
    5: ["Daylight", "Haste"],
    7: ["Divination", "Freedom of Movement"],
    9: ["Dream", "Insect Plague"]
}

_landMountain = {
    3: ["Spider Climb", "Spike Growth"],
    5: ["Lightning Bolt", "Meld into Stone"],
    7: ["Stone Shape", "Stoneskin"],
    9: ["Passwall", "Wall of Stone"]
}

_landSwamp = {
    3: ["Darkness", "Melf's Acid Arrow"],
    5: ["Water Walk", "Stinking Cloud"],
    7: ["Freedom of Movement", "Locate Creature"],
    9: ["Insect Plague", "Scrying"]
}

_landUnderdark = {
    3: ["Spider Climb", "Web"],
    5: ["Gaseous Form", "Stinking Cloud"],
    7: ["Greater Invisibility", "Stone Shape"],
    9: ["Cloudkill", "Insect Plague"]
}

_landNames = {
    "Arctic": _landArctic,
    "Coast": _landCoast,
    "Desert": _landDesert,
    "Forest": _landForest,
    "Grassland": _landGrassland,
    "Mountain": _landMountain,
    "Swamp": _landSwamp,
    "Underdark": _landUnderdark
}
