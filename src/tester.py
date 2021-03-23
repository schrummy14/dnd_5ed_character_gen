import player
import classes
import features

a = player.Player()

# Create a random character at level 1
a.createRandom(1)

# Re roll atributes, reset level and level to 1
a.atributes.rollAtributes(min_val=1,max_val=6)
a.level = 0
a.levelUp(1)

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
