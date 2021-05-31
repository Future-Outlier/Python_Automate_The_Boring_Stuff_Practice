import re # the header file of the regex.
          # r'' means raw string (原始字串)
          # example: '\\t' == r'\t'
          # raw string can make you don't need to notice specific case such as \\

''' the normal character to use in regex.
\d 0~9 any numbers
\D not \d
\w characters such as alphabet, number or '_' baseline.
\W not \w
\s whitespace character or newline character 
\S not \s
'''
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is 415-555-4242')
# mo: match object.
if mo == None:
    print ("No phone number match.")
else:
    print('Phone number found: '+ mo.group())

print(mo.group(0) + '\n' + mo.group(1) + '\n' + mo.group(2)) # we will notice that it counts from 1.
print(mo.groups()) # the difference between group and groups.

heroRegex = re.compile(r'Batman|Tina Fey') # the '|' or expression
mo1 = heroRegex.search('Batman and Tina Fey.') # | means pipe in this case.
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman .')
print(mo2.group())

# if we want to search the same begin of a string todo |
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

# if we want to find a selectable string (string)?
# means that a part of string is selectable. todo 0 or 1 time
batRegex = re.compile(r'Bat(wo)?man') # todo ? means (wo) can be existed or not
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

# if we want to find a selectable string (string)?
# means that a part of string is selectable. todo 0 or >0 times.
# todo compare match  0 or lots of times.
batRegex = re.compile(r'Bat(wo)*man') # todo ? means (wo) can be existed or not
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowowowowowowowoman')
print(mo2.group())

# if we want to find a selectable string (string)?
# means that a part of string is selectable. todo at least 1 times.
# todo compare match  1 or lots of times.
batRegex = re.compile(r'Bat(wo)+man') # todo ? means (wo) can be existed or not
'''mo1 = batRegex.search('The Adventures of Batwoman') # will be none type.
print(mo1.group())'''
mo2 = batRegex.search('The Adventures of Batwowowowowowowowowoman')
print(mo2.group())

# the greedy search in python
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())
# so if we use big brackets {}, we will sue greedy to find the longest string
# if we use {}?, we will use greedy to find the shortest string.

# todo the practice of findall()
phonelist = phoneNumRegex.findall('Cell: 123-525-1234 Work: 123-556-7899')
print(phonelist) # if there's nothing, .findall will return a empty list.

# You can use middle brackets [] to define your own character type
vowelRegex = re.compile(r'[AEIOUaeiou]')
vowels = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(vowels)

# You can use middle brackets [] to define your own character type
vowelRegex = re.compile(r'[^AEIOUaeiou]') # todo ^ can do the opposite things
vowels = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(vowels)

# Also a way to use ^ and $ to
# caret ^ $ dollar
# carrots costs dollars
endwithnumber = re.compile(r'^\d+$') # todo means from begin to end we only want decimal numbers.
ewn = endwithnumber.search('42123456789')
print(ewn)

# wildcard . You can use in every case.
atRegex = re.compile(r'.at')
atobjects = atRegex.findall('The cat in the hat sat on the flat mat.')
print(atobjects)

# todo .* we can accept every characters except '\n' new line character
# todo Important Skills
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Eric Last Name: Chen')
print(mo)

# nongreedy case to .* vs greedy case to .*
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo)
greedyRegex = re.compile(r'<.*>') # todo no '?'
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo)

# use '.' character to find the new line character
nonewlineRegex = re.compile('.*')
nonewlineobject = nonewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law')

print(nonewlineobject.group())

nonewlineRegex = re.compile('.*', re.DOTALL) #todo re.DOTALL allow us to ignore \n new line character.
nonewlineobject = nonewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law')
print(nonewlineobject.group())

# todo  ignore case about upper or lower alphabet.
robocop = re.compile(r'robocop', re.IGNORECASE) # todo re.I == re.IGNORECASE
rob_object = robocop.search('Robocop is part man, part machine, all cop.').group()
print(rob_object)
rob_object = robocop.search('robocop is part man, part machine, all cop.').group()
print(rob_object)

# use sub() to replace string.  todo we substitute every things.
name = re.compile(r'Agent \w+')
nameobject = name.sub('X_secret', 'Agent Alice gave the secret documents to Agent Bob.')
print(nameobject)

# to show the first character
agentnameregex = re.compile(r'Agent (\w)(\w)\w*') # todo \1 means first (\w) \2 means second (\w)
agentname = agentnameregex.sub(r'\1****', 'Agent Alice told Agent Caro'
'l that Agent Eve knew Agent Bob was a double agent.')
print(agentname)

# VERBOSE MODE
phoneregex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?           # area code
    (\s|-|\.)?                   # separator
    (\d{3})                     # first 3 digits
    (\s|-|\.)                    # separator             
    (\d{4})                       # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extensions
)''', re.VERBOSE)





















