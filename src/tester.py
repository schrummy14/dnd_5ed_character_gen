import player
import features

a = player.Player()
a.createRandom(1)

print(a.atributes.values)
print(a.atributes.modifiers)

print("race:", a.races.info.features['race'])
print("sub race:", a.races.info.features['subRace'])
print("features")
features.printFeatures(a.races.info.features['features'])
