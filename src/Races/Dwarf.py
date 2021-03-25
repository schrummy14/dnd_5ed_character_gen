import Races.features
from random import randint
from Races.GenRace import *

class Dwarf(GenRace):
    def __init__(self, subRace=None):
        super(self.__class__, self).__init__()
        self.modstats = {
            'constitution': 2
            }
        self.speed = 25

        if subRace is None:
            dwarf_id = randint(1,2)
        else:
            if subRace == "Hill Dwarf":
                dwarf_id = 1
            elif subRace == "Mountain Dwarf":
                dwarf_id = 2
            else:
                print("%s: is not valid" % (subRace))
                print("Valid Options:\n\tHill Dwarf\n\tMountain Dwarf")
        if dwarf_id == 1:
            self.modstats['wisdom'] = 1
            self.features = Races.features.raceFeatures(race='Dwarf',subRace='Hill Dwarf')
        elif dwarf_id == 2:
            self.modstats['strength'] = 2
            self.features = Races.features.raceFeatures(race='Dwarf',subRace='Mountain Dwarf')
