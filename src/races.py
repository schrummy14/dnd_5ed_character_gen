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
        race_id = randint(1,9)
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
    
    def setRace(self, race, subRace="None"):
        self.info = _Races[race](subRace)

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
