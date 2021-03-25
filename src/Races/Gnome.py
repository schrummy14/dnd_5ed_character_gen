import Races.features
from random import randint
from Races.GenRace import *



class Gnome(GenRace):
    def __init__(self, subRace=None):
        super(self.__class__, self).__init__()
        self.modstats = {
            'intelligence': 2
            }
        self.speed = 25
        
        if subRace is None:
            gnome_id = randint(1,2)
        else:
            if subRace == "Forest Gnome":
                gnome_id = 1
            elif subRace == "Rock Gnome":
                gnome_id = 2
            else:
                print("%s: is not valid" % (subRace))
                print("Valid Options:\n\tForest Gnome\n\tRock Gnome")
        if gnome_id == 1:
            self.modstats['dexterity'] = 1
            self.features = Races.features.raceFeatures(race='Gnome',subRace='Forest Gnome')
        elif gnome_id == 2:
            self.modstats['constitution'] = 1
            self.features = Races.features.raceFeatures(race='Gnome',subRace='Rock Gnome')
            
        
        
        return