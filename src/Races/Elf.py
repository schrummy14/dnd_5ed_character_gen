import Races.features
from random import randint
from Races.GenRace import *

class Elf(GenRace):
    def __init__(self, subRace=None):
        super(self.__class__, self).__init__()
        self.modstats = {
            'dexterity': 2
            }
        self.speed = 30

        if subRace is None:
            elf_id = randint(1,3)
        else:
            if subRace == "High Elf":
                elf_id = 1
            elif subRace == "Wood Elf":
                elf_id = 2
            elif subRace == "Drow":
                elf_id = 3
            else:
                print("%s: is not valid" % (subRace))
                print("Valid Options:\n\tHigh Elf\n\tWood Elf\n\tDrow")
        
        if elf_id == 1: 
            self.modstats['intelligence'] = 1
            self.features = Races.features.raceFeatures(race='Elf',subRace='High Elf')
        elif elf_id == 2:
            self.modstats['wisdom'] = 1
            self.features = Races.features.raceFeatures(race='Elf',subRace='Wood Elf')
        elif elf_id == 3:
            self.modstats['charisma'] = 1
            self.features = Races.features.raceFeatures(race='Elf',subRace='Drow')
        return
