import rolls
from random import sample
from Classes.GenClass import GenClass
class Monk(GenClass):
    def __init__(self, extra=None):
        super(Monk, self).__init__()
        self.hitDie = rolls.d8
        self.className = "Monk"
        self.primaryAbility = ["Dexterity", "Wisdom"]
        self.savingThrowProficiencies = ["Strength", "Dexterity"]
        self.armorWeaponProficiencies = ["Simple Weapons", "Shortswords"]

        self.martialArtsId = 0
        self.kiPointsId = -1
        self.unarmoredMovementId = -1

        self.classFeatures.append("MartialArts:")

        if extra is None:
            self.monasticTraditions = sample(["Way of the Open Hand", "Way of Shadow", "Way of the Four Elements"],1)[0]
        else:
            self.monasticTraditions = extra


    def getFeatures(self, level):
        if level == 1:
            self.pickSkills()
            self.classFeatures[self.martialArtsId] = "Martial Arts: " + self.getMartialArtsDie(level)
            self.classFeatures.append("Unarmored Defense")
            self.acMod.append('wisdom')
        elif level == 2:
            self.kiPointsId = len(self.classFeatures)
            self.classFeatures.append('Ki: %d' % (self.getKiPoints(level)))
            self.unarmoredMovementId = len(self.classFeatures)
            self.classFeatures.append("Unarmored Movement: %dft" % (self.getUnarmoredMovement(level)))
        elif level == 3:
            self.getMonasticTraditionFeature(level)
            self.classFeatures.append("Deflect Missiles")
        elif level == 4:
            self.classFeatures.append("Slow Fall")
        elif level == 5:
            self.classFeatures.append("Extra Attack")
            self.classFeatures.append("Stunning Strike")
            self.numAttacks += 1
        elif level == 6:
            self.classFeatures.append("Ki-Empowered Strikes")
            self.getMonasticTraditionFeature(level)
        elif level == 7:
            self.classFeatures.append("Evasion")
            self.classFeatures.append("Stillness of Mind")
        elif level == 9:
            self.classFeatures.append("Improved Unarmored Movement")
        elif level == 10:
            self.classFeatures.append("Purity of Body")
        elif level == 11:
            self.getMonasticTraditionFeature(level)
        elif level == 13:
            self.classFeatures.append("Tongue of the Sun and Moon")
        elif level == 14:
            self.classFeatures.append("Diamond Soul")
        elif level == 15:
            self.classFeatures.append("Timeless Body")
        elif level == 17:
            self.getMonasticTraditionFeature(level)
        elif level == 18:
            self.classFeatures.append("Empty Body")
        elif level == 20:
            self.classFeatures.append("Perfect Self")


        
        if level > 2:
            self.classFeatures[self.martialArtsId] = "Martial Arts: " + self.getMartialArtsDie(level)
            self.classFeatures[self.kiPointsId] = 'Ki: %d' % (self.getKiPoints(level))
            self.classFeatures[self.unarmoredMovementId] = "Unarmored Movement: %dft" % (self.getUnarmoredMovement(level))
            self.speedMod = self.getUnarmoredMovement(level)

    def getMonasticTraditionFeature(self, level):
        if self.monasticTraditions == "Way of the Open Hand":
            f = "Way of the Open Hand: "
            if level == 3:
                self.classFeatures.append(f + "Open Hand Technique")
            elif level == 6:
                self.classFeatures.append(f + "Wholeness of Body")
            elif level == 11:
                self.classFeatures.append(f + "Tranquility")
            elif level == 17:
                self.classFeatures.append(f + "Quivering Palm")
        elif self.monasticTraditions == "Way of Shadow":
            f = "Way of Shadow: "
            if level == 3:
                self.classFeatures.append(f + "Shadow Arts")
            elif level == 6:
                self.classFeatures.append(f + "Shadow Step")
            elif level == 11:
                self.classFeatures.append(f + "Cloak of Shadows")
            elif level == 17:
                self.classFeatures.append(f + "Opportunist")
        elif self.monasticTraditions == "Way of the Four Elements":
            f = "Way of the Four Elements: "
            if level == 3:
                self.classFeatures.append(f + "Disciple of the Elements")
        pass

    def getKiPoints(self, level):
        return level

    def getUnarmoredMovement(self, level):
        if level < 6:
            return 10
        elif level < 10:
            return 15
        elif level < 14:
            return 20
        elif level < 18:
            return 25
        else:
            return 30

    def getMartialArtsDie(self, level):
        if level < 5:
            return '1d4'
        elif level < 11:
            return '1d6'
        elif level < 17:
            return '1d8'
        elif level < 21:
            return '1d10'
        else:
            return '1d12'

    def pickSkills(self):
        self.profSkills = sample(["acrobatics", "athletics", "history", "insight", "religon", "stealth"],2)

    def levelUp(self, level):
        self.getFeatures(level)
        self.updateSkills(level)