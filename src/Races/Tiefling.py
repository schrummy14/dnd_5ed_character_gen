import Races.features
from Races.GenRace import *

class Tiefling(GenRace):
    def __init__(self, subRace=None):
        super(self.__class__, self).__init__()
        self.modstats = {
            'intelligence': 1,
            'charisma': 2
            }
        self.speed = 30
        
        self.features = Races.features.raceFeatures(race='Tiefling',subRace=None)
