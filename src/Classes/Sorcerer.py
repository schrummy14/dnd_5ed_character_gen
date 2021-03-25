import rolls
from Classes.GenClass import GenClass
class Sorcerer(GenClass):
    def __init__(self):
        super(Sorcerer, self).__init__()
        self.hitDie = rolls.d6
        self.className = "Sorcerer"
        self.primaryAbility = "Charisma"
        self.savingThrowProficiencies = ["Constitution", "Charisma"]
        self.armorWeaponProficiencies = ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light Crossbows"]
