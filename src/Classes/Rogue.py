import rolls
from Classes.GenClass import GenClass
class Rogue(GenClass):
    def __init__(self):
        super(Rogue, self).__init__()
        self.hitDie = rolls.d8
        self.className = "Rogue"
        self.primaryAbility = "Dexterity"
        self.savingThrowProficiencies = ["Dexterity", "Inteligence"]
        self.armorWeaponProficiencies = ["Light Armor", "Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers", "Shortswords"]
