import Races.features
import random
from Races.GenRace import *

class HalfElf(GenRace):
    def __init__(self, subRace=None):
        super(self.__class__, self).__init__()
        attributes = ['strength','dexterity','constitution','intelligence','wisdom']
        attribute1 = random.choice(attributes)
        attributes.remove(attribute1)
        attribute2 = random.choice(attributes)
        
        self.modstats = {
            'charisma': 2,
            attribute1: 1,
            attribute2: 1
            }
        self.speed = 30
        
        self.features = {'race': "Half Elf",
                         'subRace': "None"}
        self.features = Races.features.raceFeatures(race='Half Elf',subRace=None)