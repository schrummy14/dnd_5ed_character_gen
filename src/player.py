
import races
import rolls
import skills
import classes
import atributes
import features


class Player:
    def __init__(self):
        self.health = 0
        self.atributes = atributes.Atributes()
        self.skills = skills.Skills()
        self.races = races.Races()
        self.classes = classes.Classes()
        self.level = 0
        self.exp = 0
        self.ac = 0
        self.proficiencyBonus = 0
        self.alignment = None

    def createRandom(self,level=1):
        self.level = level
        self.races.getRandom()
        self.classes.getRandom()
        self.atributes.rollAtributes()
        self.addAtributeModifiers()

        self.health = classes._HitDie[self.classes.info.className] + self.atributes.modifiers["constitution"]

    def rollInitiative(self):
        val = rolls.d20() + self.atributes.modifiers['dexterity']
        return val
    
    def addAtributeModifiers(self):
        # Add atribute modifiers from race
        raceModifiers = self.races.info.modstats
        keys = raceModifiers.keys()
        for key in keys:
            self.atributes.values[key] += raceModifiers[key]

        # Add atribute modifiers from background or other...
        
        self.atributes.setModifiers()
        return

