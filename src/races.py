import Races.features
from random import randint
from Races.Dwarf import Dwarf
from Races.GenRace import GenRace
from Races.Elf import Elf
from Races.Dragonborn import Dragonborn
from Races.Gnome import Gnome
from Races.Halfling import Halfling
from Races.Human import Human
from Races.HalfElf import HalfElf
from Races.HalfOrc import HalfOrc
from Races.Tiefling import Tiefling

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
        elif race_id == 9:
            self.info = HalfOrc()
    
    def setRace(self, race, subRace=None):
        self.info = _Races[race](subRace)

# class GenRace:
#     def __init__(self, subRace=None):
#         self.modstats = None
#         self.speed = None
#         self.features = None


# class Dwarf(GenRace):
#     def __init__(self, subRace=None):
#         self.modstats = {
#             'constitution': 2
#             }
#         self.speed = 25

#         if subRace is None:
#             dwarf_id = randint(1,2)
#         else:
#             if subRace == "Hill Dwarf":
#                 dwarf_id = 1
#             elif subRace == "Mountain Dwarf":
#                 dwarf_id = 2
#             else:
#                 print("%s: is not valid" % (subRace))
#                 print("Valid Options:\n\tHill Dwarf\n\tMountain Dwarf")
#         if dwarf_id == 1:
#             self.modstats['wisdom'] = 1
#             self.features = features.raceFeatures(race='Dwarf',subRace='Hill Dwarf')
#         elif dwarf_id == 2:
#             self.modstats['strength'] = 2
#             self.features = features.raceFeatures(race='Dwarf',subRace='Mountain Dwarf')

#         return



# class Elf(GenRace):
#     def __init__(self, subRace=None):

#         self.modstats = {
#             'dexterity': 2
#             }
#         self.speed = 30

#         if subRace is None:
#             elf_id = randint(1,3)
#         else:
#             if subRace == "High Elf":
#                 elf_id = 1
#             elif subRace == "Wood Elf":
#                 elf_id = 2
#             elif subRace == "Drow":
#                 elf_id = 3
#             else:
#                 print("%s: is not valid" % (subRace))
#                 print("Valid Options:\n\tHigh Elf\n\tWood Elf\n\tDrow")
        
#         if elf_id == 1: 
#             self.modstats['intelligence'] = 1
#             self.features = features.raceFeatures(race='Elf',subRace='High Elf')
#         elif elf_id == 2:
#             self.modstats['wisdom'] = 1
#             self.features = features.raceFeatures(race='Elf',subRace='Wood Elf')
#         elif elf_id == 3:
#             self.modstats['charisma'] = 1
#             self.features = features.raceFeatures(race='Elf',subRace='Drow')
#         return









_Races = {
    "Dwarf": Dwarf,
    "Elf": Elf,
    "Halfling": Halfling,
    "Human": Human,
    "Dragonborn": Dragonborn,
    "Gnome": Gnome,
    "Half Elf": HalfElf,
    "Tiefling": Tiefling,
    "Half Orc": HalfOrc
}
