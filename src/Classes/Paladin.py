import rolls
from Classes.GenClass import GenClass
class Paladin(GenClass):
    def __init__(self):
        super(Paladin, self).__init__()
        self.hitDie = rolls.d10
        self.className = "Paladin"
        self.primaryAbility = ["Strength", "Charisma"]
        self.savingThrowProficiencies = ["Wisdom", "Charisma"]
        self.armorWeaponProficiencies = ["All Armor", "Shields", "Simple Weapons", "Martial Weapons"]
