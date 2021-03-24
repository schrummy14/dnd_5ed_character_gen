import player
import classes
import features

a = player.Player()
b = player.Player()
# Create a random character at level 1
a.createRandom(1)
# Create a dwarf fighter at level 1 with specific base atributes
b.create('Tiefling','Fighter',level=1,atributes=[10,11,12,13,14,15])
# Re roll atributes, reset level and level to 1
a.atributes.rollAtributes(min_val=1,max_val=6)
a.level = 0
a.levelUp(1)

print("race:", b.races.info.features['race'])
print("sub race:", b.races.info.features['subRace'])
print("features")
features.printFeatures(b.races.info.features['features'])

print("Class:", b.classes.info.className)
print("Level:", b.level)
print("starting hit die:", classes._HitDie[a.classes.info.className])
print("Current Health:", b.health)
print(b.atributes.values)
print(b.atributes.modifiers)

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

print("\n")
