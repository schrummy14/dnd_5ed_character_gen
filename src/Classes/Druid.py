import rolls
from Classes.GenClass import GenClass
class Druid(GenClass):
    def __init__(self):
        self.hitDie = rolls.d8
        self.className = "Druid"
        self.primaryAbility = "Wisdom"
        self.savingThrowProficiencies = ["Intelligence", "Wisdom"]
        self.armorWeaponProficiencies = [
            "Light Armor (nonmetal)", "Medium Armor (nonmetal)", "Shields (nonmetal)", "Clubs", "Daggers",
            "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears"]
