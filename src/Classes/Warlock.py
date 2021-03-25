import rolls
from Classes.GenClass import GenClass
class Warlock(GenClass):
    def __init__(self):
        super(Warlock, self).__init__()
        self.hitDie = rolls.d8
        self.className = "Warlock"
        self.primaryAbility = "Charisma"
        self.savingThrowProficiencies = ["Wisdom", "Charisma"]
        self.armorWeaponProficiencies = ["Light Armor", "Simple Weapons"]
