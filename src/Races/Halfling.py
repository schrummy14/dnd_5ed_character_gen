import Races.features
from random import randint
from Races.GenRace import *


class Halfling(GenRace):
    def __init__(self,subRace=None):
        self.modstats = {
            'dexterity': 2
            }
        self.speed = 25
        
        if subRace is None:
            halfling_id = randint(1,2)
        else:
            if subRace == 'Lightfoot':
                halfling_id = 1
            elif subRace == 'Stout':
                halfling_id = 2
            else:
                print("%s: is not valid" % (subRace))
                print("Valid Options:\n\tLightfoot\n\tStout")
        if halfling_id == 1:
            self.modstats['charisma'] = 1
            self.features = Races.features.raceFeatures(race='Halfling',subRace="Lightfoot")
        if halfling_id == 2:
            self.modstats['constitution'] = 1
            self.features = Races.features.raceFeatures(race='Halfling',subRace='Stout')
