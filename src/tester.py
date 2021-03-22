import player


a = player.Player()
a.createRandom(1)

print(a.atributes.values)

a.atributes.rollAtributes(10,15)
print(a.atributes.values)

print(a.features.race)
