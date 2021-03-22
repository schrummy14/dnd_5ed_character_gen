
import races
import random
import skills
import classes
import atributes
import features


class Player:
    def __init__(this):
        this.health = 0
        this.atributes = atributes.Atributes()
        this.skills = skills.Skills()
        this.races = races.Races()
        this.classes = classes.Classes()
        this.level = 0
        this.ac = 0
        this.proficiencyBonus = 0
        this.alignment = None

    def createRandom(this,level=1):
        this.level = level
        this.races.getRandom()
        this.classes.getRandom()
        this.health = 10
        this.atributes.rollAtributes()
        this.addAtributeModifiers()

    def rollInitiative(this):
        val = random.randint(1,20) + this.atributes.modifiers['dexterity']
        return val
    
    def addAtributeModifiers(this):
        # Add atribute modifiers from race
        raceModifiers = this.races.info.modstats
        keys = raceModifiers.keys()
        for key in keys:
            this.atributes.values[key] += raceModifiers[key]

        # Add atribute modifiers from background or other...


        
        this.atributes.setModifiers()
        return

