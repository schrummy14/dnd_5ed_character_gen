import rolls
from Classes.GenClass import GenClass
class Bard(GenClass):
    def __init__(self):
        self.hitDie = rolls.d8
        self.className = "Bard"
        self.primaryAbility = "Charisma"
        self.savingThrowProficiencies = ["Dexterity", "Charisma"]
        self.armorWeaponProficiencies = ["Light Armor", "Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers", "Shortswords"]
