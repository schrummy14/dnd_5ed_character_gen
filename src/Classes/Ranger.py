import rolls
from Classes.GenClass import GenClass
class Ranger(GenClass):
    def __init__(self):
        super(Ranger, self).__init__()
        self.hitDie = rolls.d10
        self.className = "Ranger"
        self.primaryAbility = ["Dexterity", "Wisdom"]
        self.savingThrowProficiencies = ["Strength", "Dexterity"]
        self.armorWeaponProficiencies = ["Light Armor", "Medium Armor", "Shields", "Simple Weapons", "Martial Weapons"]
