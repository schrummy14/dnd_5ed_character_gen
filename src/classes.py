from random import randint
from Classes.GenClass import GenClass
from Classes.Barbarian import Barbarian
from Classes.Bard import Bard
from Classes.Cleric import Cleric
from Classes.Druid import Druid
from Classes.Fighter import Fighter
from Classes.Monk import Monk
from Classes.Paladin import Paladin
from Classes.Ranger import Ranger
from Classes.Rogue import Rogue
from Classes.Sorcerer import Sorcerer
from Classes.Warlock import Warlock
from Classes.Wizard import Wizard

class Classes:
    def __init__(self):
        self.info = GenClass()

    def getRandom(self):
        randClassId = randint(1,5)
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
