# islower(), isupper(), isalnum(), isalpha(), isdecimal(), istitle(), isspace
# They can be used in validinput case.
while True:
    print('Enter your age')
    age = input()
    if age.isdecimal():
        break
    print("Please enter a number for your age.")
while True:
    print("Select a new password(letters and numbers only):")
    password = input()
    if password.isalnum():
        break
    print("Password can only have letters and numbers.")

## startswith and endswith
# we can observe that startswith check form start and
# endswith check from ends.
check = 'Hello world!'
print(check.startswith('Hello'))
print(check.endswith('world!'))
print(check.startswith('Hello world!'))
print(check.endswith('Hello world!'))

## important function join and split

# we can observe that join change list into str
#                     split change str into list
#                     partition change str into tuple
pets = ['cats', 'rats', 'bats']
petstr = ' '.join(pets)
print(petstr)
petstr = " ABC ".join(pets)
print(petstr)
petlist = petstr.split() # we can observe that the default is ' '
print(petlist)           # a blank space, and we split it.
petlist = petstr.split(' ABC ')
print(petlist)

#partition() to get everything in the string  without discarding
part = "Hello, world!".partition('w')
print(part)

# practice about rjust, ljust and center












