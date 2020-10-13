fishes =['Perk','Pike','Bream','Eel','Roach']


for fish in fishes:
    print('fish: {}' .format(fish))
print('')
index =0

while index <len(fishes):
       print('fish: {}' .format(fishes[index]))

       index+=1

print('')
print('Unsorted Fishes ', format(fishes))
print('')
sortedFishes= sorted(fishes)
print(' Sorted Fishes ', format(sortedFishes))
print('')
fishes.sort();
print('Also  Sorted Fishes ', format(fishes))
print('')
fishes_2 =['Carp','Tench','PerchPike','Trout']
print('New Fishes ', format(fishes_2))
print('')
allFishes= fishes + fishes_2
print(' All Fishes ', format(allFishes))
