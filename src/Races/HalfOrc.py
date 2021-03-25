import Races.features
from Races.GenRace import *

class HalfOrc(GenRace):
    def __init__(self, subRace=None):
        self.modstats = {
            'strength': 2,
            'constitution': 1
            }
        self.speed = 30
        self.features = Races.features.raceFeatures(race='Half Orc',subRace=None)
        
        
