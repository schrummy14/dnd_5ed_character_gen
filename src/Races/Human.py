import Races.features
from random import randint
from Races.GenRace import *

class Human(GenRace):
    def __init__(self, subRace=None):
        self.modstats = {
            'strength': 1,
            'dexterity': 1,
            'constitution': 1,
            'intelligence': 1,
            'wisdom': 1,
            'charisma': 1
            }
        self.speed = 30
        self.features = {'race': "Human",
                         'subRace': "None"}
        
        _human = {
            'none': """
            No features for you, you boring, boring human. """}
        
        
        self.features['features']= _human