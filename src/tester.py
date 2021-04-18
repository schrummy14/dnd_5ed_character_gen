import player
import classes
import features
import characterSheet

import spells

a = player.Player()
# Create a random character at level 1
# a.createRandom(1)
a.create(race='Elf', subrace='Drow',className='Monk',atributes=[12,13,15,12,12,18])
# Re roll atributes, reset level and level to 1
# a.atributes.rollAtributes(min_val=5,max_val=6)
# a.level = 0
# a.levelUp(1)

print("race:", a.races.info.features['race'])
print("sub race:", a.races.info.features['subRace'])
print("features")
features.printFeatures(a.races.info.features['features'])

print("Class:", a.classes.info.className)
print("Level:", a.level)
print("starting hit die:", classes._HitDie[a.classes.info.className])
print("Current Health:", a.health)
print(a.atributes.values)
print(a.atributes.modifiers)

# Make a level 20 character
a.levelUp(20)
print("\nClass:", a.classes.info.className)
print("Level:", a.level)
print("starting hit die:", classes._HitDie[a.classes.info.className])
print("Current Health:", a.health)
print(a.atributes.values)
print(a.atributes.modifiers)

print("Class Features")
for key in sorted(a.classes.info.classFeatures):
    print('\t' + key)

print("Skills")
for key in a.skills.keys():
    print('\t', key, a.skills[key])
print("\n")

characterSheet.createCharacterSheet(a,'test.pdf')


# allSpells = spells.getAllSpells()
# for spell in allSpells:
#     print(spell)
# print(spells.getSpell('Acid Splash'))
# print(spells.getSpell('Light'))
# print(spells.getSpell('Fireball'))
# print(spells.getRandomSpell())
# print(spells.getRandomSpell(0,'druid'))

# import Classes.Druid
# for land in Classes.Druid._landNames.keys():
#     curLand = Classes.Druid._landNames[land]
#     for lvl in curLand.keys():
#         curSpells = curLand[lvl]
#         for spell in curSpells:
#             print(land, lvl, spell, spells.getSpell(spell))