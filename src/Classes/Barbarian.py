import rolls
from Classes.GenClass import GenClass
class Barbarian(GenClass):
    def __init__(self):
        self.hitDie = rolls.d12
        self.className = "Barbarian"
        self.primaryAbility = "Strength"
        self.savingThrowProficiencies = ["Strength", "Constitution"]
        self.armorWeaponProficiencies = ["Light Armor", "Medium Armor", "Shields", "Simple Weapons", "Martial Weapons"]
