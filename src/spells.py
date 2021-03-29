# Contains all spells...

def getSpell(sName):
    val = dict()
    val[sName] = _allSpells[sName]
    return val

_allSpells = {
    'light': {
        "level": 0,
        "range": 'touch',
        "dice": None,
        "location": 'PH: 255'
    }
}