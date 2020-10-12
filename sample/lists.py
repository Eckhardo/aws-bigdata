fishes = ['Perk','Pike','Roach']
print('First  Fish {}' .format(fishes[0]))
print('Last  Fish {}' .format(fishes[-1]))
print('First  Fish {}' .format(fishes[-3]))

fishes.append('Carp');
""" Carp """
print('Apended  Fish {}' .format(fishes[-1]))
fishes.extend( ['Bream','PerchPike'])
print('Extended  Fishes {},{}' .format(fishes[-1], fishes[-2]))
fishes.insert(1, 'Eel')
print('Inserted  Fishes {}' .format(fishes[1]))


""" SLICES"""
some_fishes= fishes[0:4]
print('First 4 Fishes {}' .format(some_fishes))
first_two= fishes[:2]
print('First 2 Fishes {}' .format(first_two))
last_two= fishes[-2:]
print('Last 2 Fishes {}' .format(last_two))

fish ='Salmon' [0:2]
print('First 2 Letters of Salmon "{}"' .format(fish))
fish ='Salmon' [-2:]
print('Last 2 Letters of Salmon "{}"' .format(fish))


""" INDEX"""

eel_index = fishes.index('Eel')
print(' Index of Eel: {}'.format(eel_index))

""" Index Error out of range """

try:
    shark_index = fishes.index('Shark')
    print(' Index of Shark: {}'.format(shark_index))
except:
    print(' Shark is not a Freshwater fish')
