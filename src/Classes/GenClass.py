class GenClass:
    def __init__(self, extra=None):
        self.hitDie = None
        self.className = None
        self.primaryAbility = None
        self.savingThrowProficiencies = None
        self.armorWeaponProficiencies = None
        self.classFeatures = list()
        self.numAttacks = 1
        self.speedMod = 0
        self.extraCritWeaponDice = 0
        self.acMod = ["dexterity"]
        self.atributeValueMod = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0
        }

    def levelUp(self, level):
        return None
