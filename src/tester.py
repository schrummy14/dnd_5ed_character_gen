import player
import features

a = player.Player()
a.races.setRace("Dwarf")
print("race:", a.races.info.features['race'])
print("sub race:", a.races.info.features['subRace'])

a.races.setRace("Dwarf","Mountain Dwarf")
print("race:", a.races.info.features['race'])
print("sub race:", a.races.info.features['subRace'])

a.classes.setClass("Fighter")
print("Class:", a.classes.info.className)
print("hit die roll:", a.classes.info.hitDie())

a.createRandom(1)

print(a.atributes.values)
print(a.atributes.modifiers)

print("race:", a.races.info.features['race'])
print("sub race:", a.races.info.features['subRace'])
print("features")
features.printFeatures(a.races.info.features['features'])

print("Class:", a.classes.info.className)
print("hit die roll:", a.classes.info.hitDie())

print("Current Health:", a.health)
