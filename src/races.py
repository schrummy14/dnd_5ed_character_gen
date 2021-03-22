import random
import features

class Races:
    def __init__(self):
        self.info = None

    def getRandom(self):
        race_id = random.randint(1,1)
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


class Dwarf:
    def __init__(self):
        self.modstats = {
            'constitution': 2
            }
        self.speed = 25

        dwarf_id = random.randint(1,2)
        if dwarf_id == 1:
            self.modstats['wisdom'] = 1
            self.features = features.raceFeatures(race='dwarf',subRace='hillDwarf')
        elif dwarf_id == 2:
            self.modstats['strength'] = 2
            self.features = features.raceFeatures(race='dwarf',subRace='mountainDwarf')

        return



class Elf:
    def __init__(self):

        self.modstats = {
            'dexterity': 2
            }
        elf_id = random.randint(1,3)
        if elf_id == 1: 
            self.modstats['intelligence'] = 1
            self.features = features.raceFeatures(race='elf',subRace='highElf')
        elif elf_id == 2:
            self.modstats['wisdom'] = 1
            self.features = features.raceFeatures(race='elf',subRace='woodElf')
        elif elf_id == 3:
            self.modstats['charisma'] = 1
            self.features = features.raceFeatures(race='elf',subRace='drow')
        return

class Halfling:
    def __init__(self):
        return

class Human:
    def __init__(self):
        return

class Dragonborn:
    def __init__(self):
        return

class Gnome:
    def __init__(self):
        return

class HalfElf:
    def __init__(self):
        return

class Tiefling:
    def __init__(self):
        return
