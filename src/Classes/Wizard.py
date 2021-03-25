import rolls
from Classes.GenClass import GenClass
class Wizard(GenClass):
    def __init__(self):
        super(Wizard, self).__init__()
        self.hitDie = rolls.d6
        self.className = "Wizard"
        self.primaryAbility = "Inteligence"
        self.savingThrowProficiencies = ["Inteligence", "Wisdom"]
        self.armorWeaponProficiencies = ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light Crossbows"]
