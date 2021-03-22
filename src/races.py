import random
import features

class Races:
    def __init__(this):
        this.info = None

    def getRandom(this):
        race_id = random.randint(1,1)
        if race_id == 1:
            this.info = Elf()
        elif race_id == 2:
            this.info = Halfling()
        elif race_id == 3:
            this.info = Human()
        elif race_id == 4:
            this.info = Dragonborn()
        elif race_id == 5:
            this.info = Gnome()
        elif race_id == 6:
            this.info = HalfElf()
        elif race_id == 7:
            this.info = Tiefling()
        elif race_id == 8:
            this.info = Dwarf()


class Dwarf:
    def __init__(this):
        this.modstats = {
            'constitution': 2
            }
        this.speed = 25

        dwarf_id = random.randint(1,2)
        if dwarf_id == 1:
            this.modstats['wisdom'] = 1
            this.features = features.raceFeatures(race='dwarf',subRace='hillDwarf')
        elif dwarf_id == 2:
            this.modstats['strength'] = 2
            this.features = features.raceFeatures(race='dwarf',subRace='mountainDwarf')

        return



class Elf:
    def __init__(this):

        this.modstats = {
            'dexterity': 2
            }
        elf_id = random.randint(1,3)
        if elf_id == 1: 
            this.modstats['intelligence'] = 1
            this.features = features.raceFeatures(race='elf',subRace='highElf')
        elif elf_id == 2:
            this.modstats['wisdom'] = 1
            this.features = features.raceFeatures(race='elf',subRace='woodElf')
        elif elf_id == 3:
            this.modstats['charisma'] = 1
            this.features = features.raceFeatures(race='elf',subRace='drow')
        return

class Halfling:
    def __init__(this):
        return

class Human:
    def __init__(this):
        return

class Dragonborn:
    def __init__(this):
        return

class Gnome:
    def __init__(this):
        return

class HalfElf:
    def __init__(this):
        return

class Tiefling:
    def __init__(this):
        return
