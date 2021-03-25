import rolls
from Classes.GenClass import GenClass
class Cleric(GenClass):
    def __init__(self):
        super(Cleric, self).__init__()
        self.hitDie = rolls.d8
        self.className = "Cleric"
        self.primaryAbility = "Wisdom"
        self.savingThrowProficiencies = ["Wisdom", "Charisma"]
        self.armorWeaponProficiencies = ["Light Armor", "Medium Armor", "Shields", "Simple Weapons"]