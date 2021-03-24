

_dwarf = {
    'darkvision' : """
    Darkvision: Accustomed to life underground, you have superior vision in dark and dim conditions.
                You can see in dim light within 60 feet of you as if it were bright light, and in
                darkness as if it were dim light. You can't discern color in darkness, only shades
                of gray.""", 

    'dwarvenResilience' : """
    Dwarven Resilience: You have advantage on saving throws against poison, and you have resistance
                        against poison damage.""", 

    'dwarvenCombatTraining' : """
    Dwarven Combat Training: You have proficiency with the battleaxe, handaxe, throwing hammer, and
                             warhammer.""", 

    'toolProficiency' : """
    Tool Proficiency: You gain proficiency with the artisan's tools of your choice: smith's tools,
                      brewer's supplies, or mason's tools.""",

    'stonecunning' : """
    Stonecunning: Whenever you make an Intelligence (history) check related to the origin of
                  stonework, you are considered proficient in the History skill and add double your
                  proficiency bonus to the check, instead of your normal proficiency bonus."""
    }
_hillDwarf = {
    'dwarvenToughness' : """
    Dwarven Toughness: Your hit point maximum increases by 1, and it increases by 1 every time you
                       gain a level."""
    }
_mountainDwarf = {
    'dwarvenArmorTraining' : """
    Dwarven Armor Training: You have proficiency with light and medium armor."""
    }

_elf = {
    'darkvision': """
    Darkvision: Accustomed to twilit forests and the night sky, you have superior vision in dark 
                and dim conditions. You can see in dim light within 60 feet of you as if it were
                bright light, and in darkness as if it were dim light. You can't discern color in
                darkness, only shades of gray.""", 

    'keenSenses' : """
    Keen Senses: You have proficiency in the perception skill.""",

    'feyAncestry' : """
    You have advantage on saving throws against being charmed, and magic can't put you to sleep.""",

    'trance' : """
    Trance: Elves don't need to sleep. Instead, they meditate deeply, remaining semiconscious, for
            4 hours a day. (The Common word for such meditation is 'trance.') While meditating, you
            can dream after a fashion; such dreams are actually mental exercises that have become
            reflexive through years of practice. After resting in this way, you gain the same
            benefit that a human does from 8 hours of sleep.""", 
    }
_highElf = {
    'elfWeaponTraining' : """
    You have proficiency with the longsword, shortsowrd, shortbow, and longbow.""", 
    'cantrip' : """
    Cantrip: You know one cantrip of your choice from the wizard spell list. Intelligence is your
             spellcasting ability for it.""",

    'extraLanguage' : """
    Extra Language: You can speak, read, and write one extra language of your choice."""
    }
_woodElf = {
    'elfWeaponTraining' : """
    You have proficiency with the longsword, shortsowrd, shortbow, and longbow.""", 
    'fleetOfFoot' : """
    Your base walking speed increases to 35 feet.""", 
    'maskOfTheWild' : """
    You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling
    snow, mist, and other natural phenomena."""
    }
_drow = {
    'superiorDarkvision' : """
    Superior Darkvision: your darkvision has a radius of 120 feet.""", 
    'sunlightSensitivity' : """
    Sunlight Sensitivity: You have disadvantage on attack rolls and on Wisdom (Perception) checks
                          that rely on sight when you, the target of your attack, or whatever you
                          are trying to perceive is in direct sunlight.""", 
    'drowMagic' : """
    Drow Magic: You know the dancing lightsv cantrip. When you reach 3rd level, you can cast the
                faerie fire spell once per day. When you reach 5th level, you can also cast the
                darkness spell once per day. Charisma is your spellcasting ability for these spells.""", 
    'drowWeaponTraining' : """
    Drow Weapon Training: You have proficiency with rapiers, shortswords, and hand crossbows."""
    }

    
_features = {
    "Dwarf": _dwarf,
    "Hill Dwarf": _hillDwarf,
    "Mountain Dwarf": _mountainDwarf,
    "Elf": _elf,
    "High Elf": _highElf,
    "Wood Elf": _woodElf,
    "Drow": _drow,


    
}

def raceFeatures(race,subRace):
    val = {
        "race": race,
        "subRace": subRace
    }
    features = _features[race]
    
    if subRace is None:
        val["features"] = features
        return val
    
    subFeatures = _features[subRace]
    keys = subFeatures.keys()
    for key in keys:
        features[key] = subFeatures[key]
    val["features"] = features
    return val

def printFeatures(features):
    keys = features.keys()
    for key in keys:
        print(features[key])
    print('')
