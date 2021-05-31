### this is about the dictionary.
#let's practice a small project about storing birthdays.
## dictionary .key(), .value(), .item()
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print("I don't have the name of " + name)
        print("Can you tell me the birthday information of %s ?" %name)
        bornday = input()
        birthdays[name] = bornday

for keys in birthdays.keys():
    print("%s %s" %(keys, birthdays[keys]))

for item in birthdays.items(): ## after print it, we can observe that .items return tuples.
    print(item)

if  'Eric' in birthdays.keys(): ## we can check whether the key exists in it.
    pass
if  'Eric' not in birthdays.keys():  ## we can check whether the key exists in it.
    pass

## the usage of get() funciton
picnicitems = {'apples': 5, 'cups': 2}
print("I am bringing " + str(picnicitems.get('apples', 0)) + " apples")
print("I am bringing " + str(picnicitems.get('eggs', 0))+ " eggs")
## setdefault
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black') # if the key doesn't exist, we create the item
print(spam)                       # else we don't do anything
spam['color'] = 'blue'
print(spam)

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1
print(count)

import pprint # a beauty way to print the dictionary
pprint.pprint(count)



