import rolls
from random import randint

class Classes:
    def __init__(self):
        self.info = GenClass()

    def getRandom(self):
        randClassId = randint(1,1)
        if randClassId == 1:
            self.info = Barbarian()
        elif randClassId == 2:
            self.info = Bard()
        elif randClassId == 3:
            self.info = Cleric()
        elif randClassId == 4:
            self.info = Druid()
        elif randClassId == 5:
            self.info = Fighter()
        elif randClassId == 6:
            self.info = Monk()
        elif randClassId == 7:
            self.info = Paladin()
        elif randClassId == 8:
            self.info = Ranger()
        elif randClassId == 9:
            self.info = Rogue()
        elif randClassId == 10:
            self.info = Sorcerer()
        elif randClassId == 11:
            self.info = Warlock()
        elif randClassId == 12:
            self.info = Wizard()
        

    def setClass(self, className):
        self.info = _Classes[className]()

class GenClass:
    def __init__(self):
        self.hitDie = None
        self.className = None
        self.primaryAbility = None
        self.savingThrowProficiencies = None
        self.armorWeaponProficiencies = None

class Barbarian(GenClass):
    def __init__(self):
        self.hitDie = rolls.d12
        self.className = "Barbarian"
        self.primaryAbility = "Strength"
        self.savingThrowProficiencies = ["Strength", "Constitution"]
        self.armorWeaponProficiencies = ["Light Armor", "Medium Armor", "Shields", "Simple Weapons", "Martial Weapons"]
    
class Bard(GenClass):
    def __init__(self):
        self.hitDie = rolls.d8
        self.className = "Bard"
        self.primaryAbility = "Charisma"
        self.savingThrowProficiencies = ["Dexterity", "Charisma"]
        self.armorWeaponProficiencies = ["Light Armor", "Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers", "Shortswords"]

class Cleric(GenClass):
    def __init__(self):
        self.hitDie = rolls.d8
        self.className = "Cleric"
        self.primaryAbility = "Wisdom"
        self.savingThrowProficiencies = ["Wisdom", "Charisma"]
        self.armorWeaponProficiencies = ["Light Armor", "Medium Armor", "Shields", "Simple Weapons"]

class Druid(GenClass):
    def __init__(self):
        self.hitDie = rolls.d8
        self.className = "Druid"
        self.primaryAbility = "Wisdom"
        self.savingThrowProficiencies = ["Intelligence", "Wisdom"]
        self.armorWeaponProficiencies = [
            "Light Armor (nonmetal)", "Medium Armor (nonmetal)", "Shields (nonmetal)", "Clubs", "Daggers",
            "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears"]

class Fighter(GenClass):
    def __init__(self):
        self.hitDie = rolls.d10
        self.className = "Fighter"
        if randint(1,2) == 1:
            self.primaryAbility = "Strength"
        else:
            self.primaryAbility = "Dexterity"
        self.savingThrowProficiencies = ["Strength", "Constitution"]
        self.armorWeaponProficiencies = ["All Armor", "Shields", "Simple Weapons", "Martial Weapons"]

class Monk(GenClass):
    def __init__(self):
        pass

class Paladin(GenClass):
    def __init__(self):
        pass

class Ranger(GenClass):
    def __init__(self):
        pass

class Rogue(GenClass):
    def __init__(self):
        pass

class Sorcerer(GenClass):
    def __init__(self):
        pass

class Warlock(GenClass):
    def __init__(self):
        pass

class Wizard(GenClass):
    def __init__(self):
        pass

_Classes = {
    "Barbarian": Barbarian,
    "Bard": Bard,
    "Cleric": Cleric,
    "Druid": Druid,
    "Fighter": Fighter,
    "Monk": Monk,
    "Paladin": Paladin,
    "Ranger": Ranger,
    "Rogue": Rogue,
    "Sorcerer": Sorcerer,
    "Warlock": Warlock,
    "Wizard": Wizard
}

_HitDie = {
    "Barbarian": 12,
    "Bard": 8,
    "Cleric": 8,
    "Druid": 8,
    "Fighter": 10,
    "Monk": 8,
    "Paladin": 10,
    "Ranger": 10,
    "Rogue": 8,
    "Sorcerer": 6,
    "Warlock": 8,
    "Wizard": 6
}
