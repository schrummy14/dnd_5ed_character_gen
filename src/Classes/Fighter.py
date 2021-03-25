import rolls
from random import randint
from Classes.GenClass import GenClass
class Fighter(GenClass):
    def __init__(self):
        super(Fighter, self).__init__()
        self.hitDie = rolls.d10
        self.className = "Fighter"
        if randint(1,2) == 1:
            self.primaryAbility = "Strength"
        else:
            self.primaryAbility = "Dexterity"
        self.savingThrowProficiencies = ["Strength", "Constitution"]
        self.armorWeaponProficiencies = ["All Armor", "Shields", "Simple Weapons", "Martial Weapons"]
