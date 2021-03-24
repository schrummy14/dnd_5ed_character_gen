import Races.features
import random
from Races.GenRace import GenRace



class Dragonborn(GenRace):
    def __init__(self, subRace=None):
        self.modstats = {
            'strength': 2,
            'charisma': 1
            }
            
        self.speed = 30
        self.features = {'race': "Dragonborn",
                         'subRace': "None"}
        
        
        if subRace is None:          
                dragon_id = random.randint(1, 10)

        if dragon_id == 1:
            subRace = 'black'
            damageType = 'acid'
            shapeType = '5 by 30 ft. line'
            saveType = 'dexterity'
        elif dragon_id == 2:
            subRace = 'blue'
            damageType = 'lightning'
            shapeType = '5 by 30 ft. line'
            saveType = 'dexterity'
        elif dragon_id == 3:
            subRace = 'brass'
            damageType = 'fire'
            shapeType = '5 by 30 ft. line'
            saveType = 'dexterity'
        elif dragon_id == 4:
            subRace = 'bronze'
            damageType = 'lightning'
            shapeType = '5 by 30 ft. line'
            saveType = 'dexterity'
        elif dragon_id == 5: 
            subRace = 'copper'
            damageType = 'acid'
            shapeType = '5 by 30 ft. line'
            saveType = 'dexterity'
        elif dragon_id == 6:
            subRace = 'gold'
            damageType = 'fire'
            shapeType = '15 ft. cone'
            saveType = 'dexterity'
        elif dragon_id == 7:
            subRace = 'green'
            damageType = 'poison'
            shapeType = '15 ft. cone'
            saveType = 'constitution'
        elif dragon_id == 8:
            subRace = 'red'
            damageType = 'fire'
            shapeType = '15 ft. cone'
            saveType = 'dexterity'
        elif dragon_id == 9:
            subRace = 'silver'
            damageType = 'cold'
            shapeType = '15 ft. cone'
            saveType = 'constitution'
        elif dragon_id == 10:
            subRace = 'white'
            damageType = 'cold'
            shapeType = '15 ft. cone'
            saveType = 'constitution'
            


        _dragonborn = { 'draconicAncestry': "Draconic Ancestry: You have draconic ancestry, which provides you with two unique benefits based upon your specific ancestry, %s" % (subRace),
 'BreathWeapon': "Breath weapon: Because of your ancestry (%s), your breath weapon deals %s type damage in a %s. The DC for this saving throw is 8 + your Constitution modifier + your proficiency bonus, and is a %s save. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increases to 3d6 at 6th level, 4d6 at 11th level, and 5d6 at 16th level." % (subRace,damageType,shapeType,saveType),
 'damageResistance': 'Damage Resistance: you have resistance to the damage type associated with your draconic ancestry (%s).' % (damageType)
 }
        self.features['features']= _dragonborn
        
        return
