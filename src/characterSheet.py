import os
from skills import skill2atribute
from PyPDF2 import PdfFileWriter, PdfFileReader
import PyPDF2.generic
import PyPDF2.pdf
import PyPDF2.utils

_maxFeaturesPageOne = 25

def createCharacterSheet(player, outFileName="document-output.pdf"):
    inFile = open("characterSheet" + os.sep + "blank.pdf", 'rb')
    input1 = PdfFileReader(inFile)
    output = PdfFileWriter()

    # Add pages
    output.addPage(input1.getPage(0))
    output.addPage(input1.getPage(1))
    output.addPage(input1.getPage(2))

    newVals = dict()
    gg = input1.getFormTextFields()
    for k,key in enumerate(gg):
        newVals[key] = "(%d)" % (k)
    #     print("%d: \"%s\"," % (k, key))
    newVals.update(_setClassLevel(player))
    newVals.update(_setRaceName(player))
    newVals.update(_setAtributes(player))
    newVals.update(_setAC(player))
    newVals.update(_setSkills(player))
    newVals.update(_setFeatures(player))
    newVals.update(_setSpells(player))

    # Update fields with new values
    output.updatePageFormFieldValues(input1.getPage(0), newVals)
    output.updatePageFormFieldValues(input1.getPage(1), newVals)
    output.updatePageFormFieldValues(input1.getPage(2), newVals)

    # finally, write "output" to document-output.pdf
    outputStream = open(outFileName, "wb")
    output.write(outputStream)
    outputStream.close()
    inFile.close()

def readCharacterSheet(fileName, inFileName="document-output.pdf"):
    pass

def _setSpells(player):
    vals = dict()
    if len(player.spellStructure) == 0:
        return vals
    curStr = list()
    for k in range(10):
        curStr.append(list())
    for key in player.spells.keys():
        spellName = key.title()
        spellLevel = int(player.spells[key]['level'])
        spellLocation = player.spells[key]['location']
        spellRange = player.spells[key]['range'].title()
        spellDice = player.spells[key]['dice']
        if spellDice is None:
            curStr[spellLevel].append("%s: %s [%s]" % (spellName, spellRange, spellLocation))
        else:
            curStr[spellLevel].append("%s: %s, %s [%s]" % (spellName, spellRange, spellDice, spellLocation))
    for k in range(10):
        if k > 0:
            numSpells = player.spellStructure[k+1]
            if numSpells == 0:
                continue
            vals[_num2field[_spellSlot2field[k]]] = str(numSpells)
        for kk, spell in enumerate(curStr[k]):
            vals[_num2field[_spell2field[k][kk]]] = spell
        
    return vals

def _setFeatures(player):
    vals = dict()
    curStr = list()
    curStr.append("")
    curStr.append("")
    for k, feat in enumerate(player.features):
        curStrId = 0*(k<=_maxFeaturesPageOne) + 1*(k>_maxFeaturesPageOne)
        curStr[curStrId] += "* " + feat + '\n'
    vals[_num2field[87]] = curStr[0][:-1]
    vals[_num2field[10]] = curStr[1][:-1]
    return vals

def _setSkills(player):
    vals = dict()
    for key in skill2atribute.keys():
        vals[_num2field[_skills2num[key]]] = str(player.skills[key])
    vals[_num2field[79]] = str(player.skills['perception'] + 10)
    return vals


def _setAC(player):
    return {
        _num2field[22]: str(player.ac),
        _num2field[23]: str(player.initiative),
        _num2field[24]: str(player.races.info.speed + player.classes.info.speedMod),
        _num2field[27]: str(player.maxHealth),
        _num2field[30]: str(player.health),
        _num2field[33]: str(player.tempHealth),
        _num2field[21]: str(player.proficiencyBonus),
        _num2field[36]: str(player.level),
        _num2field[38]: str(player.level)
    }

def _setClassLevel(player):
    return {
        _num2field[12]: "%s & %s" % (player.classes.info.className, str(player.level))
        }

def _setRaceName(player):
    curStr = "%s" % (player.races.info.features['race'])
    if player.races.info.features['subRace'] != "None" and not player.races.info.features['subRace'] is None:
        curStr += " (%s)" % (player.races.info.features['subRace'])
    return {
        _num2field[16]: curStr
    }

def _setAtributes(player):
    vals = dict()
    for key in player.atributes.values.keys():
        loc = _name2num[key]
        # Set Values
        for k in loc:
            vals[_num2field[k]] = str(player.atributes.values[key])
        # Set Mods
        # print(_num2field[_name2num[key+"_mod"]], player.atributes.modifiers[key])
        vals[_num2field[_name2num[key+"_mod"]]] = str(player.atributes.modifiers[key])
    return vals

_name2num = {
    "strength": [20, 28],
    "dexterity": [29, 41],
    "constitution": [35, 42],
    "intelligence": [40, 43],
    "wisdom": [61, 44],
    "charisma": [68, 45],
    "strength_mod": 26,
    "dexterity_mod": 32,
    "constitution_mod": 37,
    "intelligence_mod": 56,
    "wisdom_mod": 67,
    "charisma_mod": 76
}

_spell2field = {
    0: [94,96,97,98,99,100,101,102],
    1: [95,103,104,105,106,107,108,109,110,111,112,113],
    2: [128,116,117,118,119,120,121,122,123,124,125,126,127],
    3: [132,131,133,134,135,136,137,138,139,140,141,142,143],
    4: [147,146,148,149,150,151,152,153,154,155,156,157,158],
    5: [162,161,163,164,165,166,167,168,169],
    6: [173,172,174,175,176,177,178,179,180],
    7: [184,183,185,186,187,188,189,190,191],
    8: [195,194,196,197,198,199,200],
    9: [204,203,205,206,207,208,209]
}

_spellSlot2field = [-1, 92, 114, 129, 144, 159, 170, 181, 192, 201]

_skills2num = {
    "acrobatics": 46,
    "animal handling": 47,
    "arcana": 64,
    "athletics": 48,
    "deception": 49,
    "history": 50,
    "insight": 51,
    "intimidation": 52,
    "investigation": 60,
    "medicine": 71,
    "nature": 69,
    "perception": 66,
    "performance": 70,
    "persuasion": 74,
    "religion": 72,
    "sleight of hand": 75,
    "stealth": 73,
    "survival": 77
}

_num2field = {
    -1: "Empty",
    0: "CharacterName 2",
    1: "Age",
    2: "Height",
    3: "Weight",
    4: "Eyes",
    5: "Skin",
    6: "Hair",
    7: "Allies",
    8: "FactionName",
    9: "Backstory",
    10: "Feat+Traits",
    11: "Treasure",
    12: "ClassLevel",
    13: "Background",
    14: "PlayerName",
    15: "CharacterName",
    16: "Race ",
    17: "Alignment",
    18: "XP",
    19: "Inspiration",
    20: "STR",
    21: "ProfBonus",
    22: "AC",
    23: "Initiative",
    24: "Speed",
    25: "PersonalityTraits ",
    26: "STRmod",
    27: "HPMax",
    28: "ST Strength",
    29: "DEX",
    30: "HPCurrent",
    31: "Ideals",
    32: "DEXmod ",
    33: "HPTemp",
    34: "Bonds",
    35: "CON",
    36: "HDTotal",
    37: "CONmod",
    38: "HD",
    39: "Flaws",
    40: "INT",
    41: "ST Dexterity",
    42: "ST Constitution",
    43: "ST Intelligence",
    44: "ST Wisdom",
    45: "ST Charisma",
    46: "Acrobatics",
    47: "Animal",
    48: "Athletics",
    49: "Deception ",
    50: "History ",
    51: "Insight",
    52: "Intimidation",
    53: "Wpn Name",
    54: "Wpn1 AtkBonus",
    55: "Wpn1 Damage",
    56: "INTmod",
    57: "Wpn Name 2",
    58: "Wpn2 AtkBonus ",
    59: "Wpn2 Damage ",
    60: "Investigation ",
    61: "WIS",
    62: "Wpn Name 3",
    63: "Wpn3 AtkBonus  ",
    64: "Arcana",
    65: "Wpn3 Damage ",
    66: "Perception ",
    67: "WISmod",
    68: "CHA",
    69: "Nature",
    70: "Performance",
    71: "Medicine",
    72: "Religion",
    73: "Stealth ",
    74: "Persuasion",
    75: "SleightofHand",
    76: "CHamod",
    77: "Survival",
    78: "AttacksSpellcasting",
    79: "Passive",
    80: "CP",
    81: "ProficienciesLang",
    82: "SP",
    83: "EP",
    84: "GP",
    85: "PP",
    86: "Equipment",
    87: "Features and Traits",
    88: "Spellcasting Class 2",
    89: "SpellcastingAbility 2",
    90: "SpellSaveDC  2",
    91: "SpellAtkBonus 2",
    92: "SlotsTotal 19",
    93: "SlotsRemaining 19",
    94: "Spells 1014",
    95: "Spells 1015",
    96: "Spells 1016",
    97: "Spells 1017",
    98: "Spells 1018",
    99: "Spells 1019",
    100: "Spells 1020",
    101: "Spells 1021",
    102: "Spells 1022",
    103: "Spells 1023",
    104: "Spells 1024",
    105: "Spells 1025",
    106: "Spells 1026",
    107: "Spells 1027",
    108: "Spells 1028",
    109: "Spells 1029",
    110: "Spells 1030",
    111: "Spells 1031",
    112: "Spells 1032",
    113: "Spells 1033",
    114: "SlotsTotal 20",
    115: "SlotsRemaining 20",
    116: "Spells 1034",
    117: "Spells 1035",
    118: "Spells 1036",
    119: "Spells 1037",
    120: "Spells 1038",
    121: "Spells 1039",
    122: "Spells 1040",
    123: "Spells 1041",
    124: "Spells 1042",
    125: "Spells 1043",
    126: "Spells 1044",
    127: "Spells 1045",
    128: "Spells 1046",
    129: "SlotsTotal 21",
    130: "SlotsRemaining 21",
    131: "Spells 1047",
    132: "Spells 1048",
    133: "Spells 1049",
    134: "Spells 1050",
    135: "Spells 1051",
    136: "Spells 1052",
    137: "Spells 1053",
    138: "Spells 1054",
    139: "Spells 1055",
    140: "Spells 1056",
    141: "Spells 1057",
    142: "Spells 1058",
    143: "Spells 1059",
    144: "SlotsTotal 22",
    145: "SlotsRemaining 22",
    146: "Spells 1060",
    147: "Spells 1061",
    148: "Spells 1062",
    149: "Spells 1063",
    150: "Spells 1064",
    151: "Spells 1065",
    152: "Spells 1066",
    153: "Spells 1067",
    154: "Spells 1068",
    155: "Spells 1069",
    156: "Spells 1070",
    157: "Spells 1071",
    158: "Spells 1072",
    159: "SlotsTotal 23",
    160: "SlotsRemaining 23",
    161: "Spells 1073",
    162: "Spells 1074",
    163: "Spells 1075",
    164: "Spells 1076",
    165: "Spells 1077",
    166: "Spells 1078",
    167: "Spells 1079",
    168: "Spells 1080",
    169: "Spells 1081",
    170: "SlotsTotal 24",
    171: "SlotsRemaining 24",
    172: "Spells 1082",
    173: "Spells 1083",
    174: "Spells 1084",
    175: "Spells 1085",
    176: "Spells 1086",
    177: "Spells 1087",
    178: "Spells 1088",
    179: "Spells 1089",
    180: "Spells 1090",
    181: "SlotsTotal 25",
    182: "SlotsRemaining 25",
    183: "Spells 1091",
    184: "Spells 1092",
    185: "Spells 1093",
    186: "Spells 1094",
    187: "Spells 1095",
    188: "Spells 1096",
    189: "Spells 1097",
    190: "Spells 1098",
    191: "Spells 1099",
    192: "SlotsTotal 26",
    193: "SlotsRemaining 26",
    194: "Spells 10100",
    195: "Spells 10101",
    196: "Spells 10102",
    197: "Spells 10103",
    198: "Spells 10104",
    199: "Spells 10105",
    200: "Spells 10106",
    201: "SlotsTotal 27",
    202: "SlotsRemaining 27",
    203: "Spells 10107",
    204: "Spells 10108",
    205: "Spells 10109",
    206: "Spells 101010",
    207: "Spells 101011",
    208: "Spells 101012",
    209: "Spells 101013"
}