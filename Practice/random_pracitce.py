# Let us practice the random library

import random
pets = ['Dog', 'Cat', 'Moose', 'Duck', 'Dragon']
ran_pet = random.choice(pets)
print(ran_pet)
# or
i = random.randint(0, 4) # randint return 0 ~ 4 (includes 4) in this case.
print(pets[i])
# shuffle -> means shuffle the cards
print(pets)
random.shuffle(pets)
print(pets)
random.shuffle(pets)
print(pets)

