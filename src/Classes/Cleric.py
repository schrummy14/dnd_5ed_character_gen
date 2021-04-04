import rolls
from spells import getSpell, getRandomSpell
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
            
        elif level == 5:
            self.du_id = len(self.classFeatures)
            self.classFeatures.append("Destroy Undead (CR 1/2)")
        elif level == 6:
            self.classFeatures[self.cd_id] = "Channel Divinity (2/rest)"
            
        elif level == 8:
            self.classFeatures[self.du_id] = "Destroy Undead (CR 1)"
            
        elif level == 10:
            self.di_id = len(self.classFeatures)
            self.classFeatures.append("Divine Intervention")
        elif level == 11:
            self.classFeatures[self.du_id] = "Destroy Undead (CR 2)"
        elif level == 14:
            self.classFeatures[self.du_id] = "Destroy Undead (CR 3)"
        elif level == 17:
            self.classFeatures[self.du_id] = "Destroy Undead (CR 4)"
        elif level == 18:
            self.classFeatures[self.cd_id] = "Channel Divinity (3/rest)"
        elif level == 20:
            self.classFeatures[self.di_id] = "Divine Intervention [Improvement]"
        if level > 1:
            self.divineDomainFeature(level)

    def getDivineDomain(self):
        if self.divineDomain is None:
            self.divineDomain = sample(["Knowledge", "Life", "Light", "Nature", "Tempest", "Trickery", "War"], 1)[0]
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
            self.addSkills("Knowledge")
            self.extraLanguages += 2
            self.spells.update(getSpell("Command"))
            self.spells.update(getSpell("Identify"))
        elif level == 2:
            self.classFeatures.append("Knowledge Domain: Channel Divinity (Knowledge of the Ages)")
        elif level == 3:
            self.spells.update(getSpell("Augury"))
            self.spells.update(getSpell("Suggestion"))
        elif level == 5:
            self.spells.update(getSpell("Nondetection"))
            self.spells.update(getSpell("Speak with Dead"))
        elif level == 6:
            self.classFeatures.append("Knowledge Domain: Channel Divinity (Read Thoughts)")
        elif level == 7:
            self.spells.update(getSpell("Arcane Eye"))
            self.spells.update(getSpell("Confusion"))
        elif level == 8:
            self.classFeatures.append("Knowledge Domain: Potent Spellcasting")
        elif level == 9:
            self.spells.update(getSpell("Command"))
            self.spells.update(getSpell("Identify"))
        elif level == 17:
            self.classFeatures.append("Knowledge Domain: Visions of the Past")

    def getLifeDomainFeature(self, level):
        f = "Life Domain: "
        if level == 1:
            self.armorWeaponProficiencies.append("Heavy Armor")
            self.classFeatures.append(f + "Disciple of Life")
            self.spells.update(getSpell("Bless"))
            self.spells.update(getSpell("Cure Wounds"))
        elif level == 2:
            self.classFeatures.append(f + "Channel Divinity (Preserve Life)")
        elif level == 3:
            self.spells.update(getSpell("Lesser Restoration"))
            self.spells.update(getSpell("Spiritual Weapon"))
        elif level == 5:
            self.spells.update(getSpell("Beacon of Hope"))
            self.spells.update(getSpell("Revivify"))
        elif level == 6:
            self.classFeatures.append(f + "Blessed Healer")
        elif level == 7:
            self.spells.update(getSpell("Death Ward"))
            self.spells.update(getSpell("Guardian of Faith"))
        elif level == 8:
            self.classFeatures.append(f + "Divine Strike")
        elif level == 9:
            self.spells.update(getSpell("Mass Cure Wounds"))
            self.spells.update(getSpell("Raise Dead"))
        elif level == 17:
            self.classFeatures.append(f + "Supreme Healing")

    def getLightDomainFeature(self, level):
        f = "Light Domain: "
        if level == 1:
            curSpells = self.spells.keys()
            if not "light" in curSpells:
                self.spells.update(getSpell('Light'))
            self.classFeatures.append(f + "Warding Flare")
            self.spells.update(getSpell("Burning Hands"))
            self.spells.update(getSpell("Faerie Fire"))
        elif level == 2:
            self.classFeatures.append(f + "Channel Divinity (Radiance of the Dawn)")
        elif level == 3:
            self.spells.update(getSpell("Flaming Sphere"))
            self.spells.update(getSpell("Scorching Ray"))
        elif level == 5:
            self.spells.update(getSpell("Daylight"))
            self.spells.update(getSpell("Fireball"))
        elif level == 6:
            self.classFeatures.append(f + "Improved Flare")
        elif level == 7:
            self.spells.update(getSpell("Guardian of Faith"))
            self.spells.update(getSpell("Wall of Fire"))
        elif level == 8:
            self.classFeatures.append(f + "Potent Spellcasting")
        elif level == 9:
            self.spells.update(getSpell("Flame Strike"))
            self.spells.update(getSpell("Scrying"))
        elif level == 17:
            self.classFeatures.append(f + "Corona of Light")

    def getNatureDomainFeature(self, level):
        f = "Nature Domain: "
        if level == 1:
            self.armorWeaponProficiencies.append("Heavy Armor")
            self.addSkills("Nature")
            self.spells.update(getRandomSpell(0,'druid'))
            self.spells.update(getSpell("Animal Friendship"))
            self.spells.update(getSpell("Speak with Animals"))
        elif level == 2:
            self.classFeatures.append(f + "Channel Divinity (Charm Animals and Plants)")
        elif level == 3:
            self.spells.update(getSpell("Barkskin"))
            self.spells.update(getSpell("Spike Growth"))
        elif level == 5:
            self.spells.update(getSpell("Plant Growth"))
            self.spells.update(getSpell("Wind Wall"))
        elif level == 6:
            self.classFeatures.append(f + "Damben Elements")
        elif level == 7:
            self.spells.update(getSpell("Dominate Beast"))
            self.spells.update(getSpell("Grasping Vine"))
        elif level == 8:
            self.classFeatures.append(f + "Divine Strike")
        elif level == 9:
            self.spells.update(getSpell("Insect Plague"))
            self.spells.update(getSpell("Tree Stride"))
        elif level == 17:
            self.classFeatures.append(f + "Master of Nature")

    def getTempestDomainFeature(self, level):
        f = "Tempest Domain: "
        if level == 1:
            self.armorWeaponProficiencies.append("Martial Weapons")
            self.armorWeaponProficiencies.append("Heavy Armor")
            self.spells.update(getSpell("Fog Cloud"))
            self.spells.update(getSpell("Thunderwave"))
        elif level == 2:
            self.classFeatures.append(f + "Channel Divinity (Destructive Wrath)")
        elif level == 3:
            self.spells.update(getSpell("Gust of Wind"))
            self.spells.update(getSpell("Shatter"))
        elif level == 5:
            self.spells.update(getSpell("Call Lightning"))
            self.spells.update(getSpell("Sleet Storm"))
        elif level == 6:
            self.classFeatures.append(f + "Thunderbolt Strike")
        elif level == 7:
            self.spells.update(getSpell("Control Water"))
            self.spells.update(getSpell("Ice Storm"))
        elif level == 8:
            self.classFeatures.append(f + "Divine Strike")
        elif level == 9:
            self.spells.update(getSpell("Destructive Wave"))
            self.spells.update(getSpell("Insect Plague"))
        elif level == 17:
            self.classFeatures.append(f + "Stormborn")


    def getTrickeryDomainFeature(self, level):
        f = "Trickery Domain: "
        if level == 1:
            self.classFeatures.append(f + 'Blessing of the Trickster')
            self.spells.update(getSpell("Charm Person"))
            self.spells.update(getSpell("Disguise Self"))
        elif level == 2:
            self.classFeatures.append(f + "Channel Divinity (Invoke Buplicity)")
        elif level == 3:
            self.spells.update(getSpell("Mirror Image"))
            self.spells.update(getSpell("Pass without Trace"))
        elif level == 5:
            self.spells.update(getSpell("Blink"))
            self.spells.update(getSpell("Dispel Magic"))
        elif level == 6:
            self.classFeatures.append(f + "Channel Divinity (Cloak of Shadows)")
        elif level == 7:
            self.spells.update(getSpell("Dimension Door"))
            self.spells.update(getSpell("Polymorph"))
        elif level == 8:
            self.classFeatures.append(f + "Divine Strike")
        elif level == 9:
            self.spells.update(getSpell("Dominate Person"))
            self.spells.update(getSpell("Modify Memory"))
        elif level == 17:
            self.classFeatures.append(f + "Improved Duplicity")

    def getWarDomainFeature(self, level):
        f = "War Domain: "
        if level == 1:
            self.armorWeaponProficiencies.append("Martial Weapons")
            self.armorWeaponProficiencies.append("Heavy Armor")
            self.spells.update(getSpell("Divine Favor"))
            self.spells.update(getSpell("Shield of Faith"))
            self.classFeatures.append(f + 'War Priest')
        elif level == 2:
            self.classFeatures.append('Channel Divinity (Guided Strike)')
        elif level == 3:
            self.spells.update(getSpell("Magic Weapon"))
            self.spells.update(getSpell("Spiritual Weapon"))
        elif level == 5:
            self.spells.update(getSpell("Crusader's Mantle"))
            self.spells.update(getSpell("Spirit Guardians"))
        elif level == 6:
            self.classFeatures.append("Channel Divinity (War God's Blessing)")
        elif level == 7:
            self.spells.update(getSpell("Freedom of Movement"))
            self.spells.update(getSpell("Stoneskin"))
        elif level == 8:
            self.classFeatures.append(f + "divine Strike")
        elif level == 9:
            self.spells.update(getSpell("Flame Strike"))
            self.spells.update(getSpell("Hold Monster"))
        elif level == 17:
            self.classFeatures.append(f + "Avatar of Battle")


    def addSkills(self, domain):
        if domain == "Knowledge":
            avalSkills = ["arcana", "history", "nature", "religion"]
            newSkills = sample(avalSkills, 2)
            for s in newSkills:
                self.expertSkills.append(s)
                if s in self.profSkills:
                    continue
                self.profSkills.append(s)
        elif domain == "Nature":
            avalSkills = ["animal handling", "nature", "survival"]
            while True:
                newSkills = sample(avalSkills, 1)[0]
                if newSkills in self.profSkills:
                    continue
                self.profSkills.append(newSkills)
                break
        

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