import random

class Atributes:
    def __init__(self):
        self.values = {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10
        }
        self.modifiers = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0
        }

    def rollAtributes(self,min=3,max=18):
        self.values = {
            "strength": random.randint(min,max),
            "dexterity": random.randint(min,max),
            "constitution": random.randint(min,max),
            "intelligence": random.randint(min,max),
            "wisdom": random.randint(min,max),
            "charisma": random.randint(min,max)
        }
        self.setModifiers()

    def setAtribute(self,atribute,value):
        try:
            self.value[atribute] = value
            self.setModifiers()
        except:
            print("bad selection")

    def setModifiers(self):
        keys = self.modifiers.keys()
        for key in keys:
            self.modifiers[key] = (self.values[key] - 10)//2
