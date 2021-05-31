# Let's try to dicuss how to use list to make programming better
## small tips if you want to use '+' to concatenate objects in your
## print function, you need to make sure  every obejct is in str type.
import random

catNames = [] # an empty list

while True:
    print('Enter the name of cat' + str(len(catNames) + 1) +
        '(Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
## The below does the same thing to visit all the list.
for name in catNames:
    print(' ' + name)
for i in range(0, len(catNames)):
    print(' ' + catNames[i])

### Let us practice the random library


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

### Let us practice the method
spam = ['hello', 'fuck', 'hi', 'howdy', 'heyas']
print(spam.index('hello')) # .index() is a method for list object.
spam.append('how are you')
print(spam)
spam.insert(1, "I'm fine")
print(spam)
spam.remove('hi')
print(spam)

### sort
numbers = [0,9,5,7,2,3,41,15,135,45,53435,456]
numbers.sort(reverse=True) ## so we can do two things in one line.
print(numbers)
numbers.reverse()
print(numbers)
## we can't sort between type str and int, but we can sort one of these by alphabetical order
word = ['as', 'sd', 'car', 'bag', '1', '20', '100']
word.sort()
print(word)


name = 'Kobe Bryant'
for i in name:
    print('* * * ' + i+ ' * * *') # so in this case we show that we can make i to str type.

# str is unchangeable, and list is changeable
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(name)
print(newName)

# compare about tuple and list
# 'tuple' object does not support item assignment
eggs = ['hello', 1, 0.5]
tmp = (1,2,)
eggs[0] = 123
# tmp[0] = 5  tuple can't be changed.
print(tmp, type(tmp), type(eggs))
print(eggs)

# id identity about python
print(id('Eric'))
name = 'Eric'
print(id(name))
name += ' is so handsome.'
print(id(name))  # We can see the first and second str have the same id but the third
                 # doesn't, because str is unchangeable, so the third str is a new str
                 # it doesn't have any relation to the previous one.
### test reference
a = 1
b = 1
b += 2
c = 1
c += 100
print(id(a), id(b), id(c))

