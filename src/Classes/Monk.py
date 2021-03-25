import rolls
from Classes.GenClass import GenClass
class Monk(GenClass):
    def __init__(self):
        super(Monk, self).__init__()
        self.hitDie = rolls.d8
        self.className = "Monk"
        self.primaryAbility = ["Dexterity", "Wisdom"]
        self.savingThrowProficiencies = ["Strength", "Dexterity"]
        self.armorWeaponProficiencies = ["Simple Weapons", "Shortswords"]
