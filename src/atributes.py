import rolls

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

    def rollAtributes(self,min_val=1,max_val=6, maxAtributeValue=20, numberOfDice=4):
        self.values = {
            "strength": min(rolls.rollAtribute(min_val,max_val,numberOfDice),maxAtributeValue),
            "dexterity": min(rolls.rollAtribute(min_val,max_val,numberOfDice),maxAtributeValue),
            "constitution": min(rolls.rollAtribute(min_val,max_val,numberOfDice),maxAtributeValue),
            "intelligence": min(rolls.rollAtribute(min_val,max_val,numberOfDice),maxAtributeValue),
            "wisdom": min(rolls.rollAtribute(min_val,max_val,numberOfDice),maxAtributeValue),
            "charisma": min(rolls.rollAtribute(min_val,max_val,numberOfDice),maxAtributeValue)
        }
        self.setModifiers()

    def setAtribute(self,atribute,value):
        try:
            self.values[atribute] = value
            self.setModifiers()
        except:
            print("bad selection")
    
    def setAtributes(self,atributes):
        if isinstance(atributes,dict):
            # If you pass in atributes as a dictionary
            for key in self.values.keys():
                self.values[key] = atributes[key]
        else:
            # If you pass in atributes as a list
            for k,key in enumerate(self.values.keys()):
                self.values[key] = atributes[k]
        self.setModifiers()

    def setModifiers(self):
        keys = self.modifiers.keys()
        for key in keys:
            self.modifiers[key] = (self.values[key] - 10)//2
