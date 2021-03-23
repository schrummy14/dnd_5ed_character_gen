import features
from random import randint

class Races:
    def __init__(self):
        self.info = GenRace()

    def getRandom(self):
        race_id = randint(1,1)
        if race_id == 1:
            self.info = Elf()
        elif race_id == 2:
            self.info = Halfling()
        elif race_id == 3:
            self.info = Human()
        elif race_id == 4:
            self.info = Dragonborn()
        elif race_id == 5:
            self.info = Gnome()
        elif race_id == 6:
            self.info = HalfElf()
        elif race_id == 7:
            self.info = Tiefling()
        elif race_id == 8:
            self.info = Dwarf()
    
    def setRace(self, race, subRace=None):
        self.info = _Races[race](subRace)

class GenRace:
    def __init__(self, subRace=None):
        self.modstats = None
        self.speed = None
        self.features = None


class Dwarf(GenRace):
    def __init__(self, subRace=None):
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
            self.features = features.raceFeatures(race='Dwarf',subRace='Hill Dwarf')
        elif dwarf_id == 2:
            self.modstats['strength'] = 2
            self.features = features.raceFeatures(race='Dwarf',subRace='Mountain Dwarf')

        return



class Elf(GenRace):
    def __init__(self, subRace=None):

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
            self.features = features.raceFeatures(race='Elf',subRace='High Elf')
        elif elf_id == 2:
            self.modstats['wisdom'] = 1
            self.features = features.raceFeatures(race='Elf',subRace='Wood Elf')
        elif elf_id == 3:
            self.modstats['charisma'] = 1
            self.features = features.raceFeatures(race='Elf',subRace='Drow')
        return

class Halfling(GenRace):
    def __init__(self, subRace=None):
        return

class Human(GenRace):
    def __init__(self, subRace=None):
        return

class Dragonborn(GenRace):
    def __init__(self, subRace=None):
        return

class Gnome(GenRace):
    def __init__(self, subRace=None):
        return

class HalfElf(GenRace):
    def __init__(self, subRace=None):
        return

class Tiefling(GenRace):
    def __init__(self, subRace=None):
        return

_Races = {
    "Dwarf": Dwarf,
    "Elf": Elf,
    "Halfling": Halfling,
    "Human": Human,
    "Dragonborn": Dragonborn,
    "Gnome": Gnome,
    "HalfElf": HalfElf,
    "Tiefling": Tiefling
}
