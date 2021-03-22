import random

class Atributes:
    def __init__(this):
        this.values = {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10
        }
        this.modifiers = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0
        }

    def rollAtributes(this,min=3,max=18):
        this.values = {
            "strength": random.randint(min,max),
            "dexterity": random.randint(min,max),
            "constitution": random.randint(min,max),
            "intelligence": random.randint(min,max),
            "wisdom": random.randint(min,max),
            "charisma": random.randint(min,max)
        }
        this.setModifiers()

    def setAtribute(this,atribute,value):
        try:
            this.value[atribute] = value
            this.setModifiers()
        except:
            print("bad selection")

    def setModifiers(this):
        keys = this.modifiers.keys()
        for key in keys:
            this.modifiers[key] = (this.values[key] - 10)//2
