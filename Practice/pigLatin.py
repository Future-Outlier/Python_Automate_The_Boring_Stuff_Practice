# English to Pig Latin
print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y') #  y is a specific condition
#Ymay amenay isyay Obekay Yantbray andyay Iyay amyay yearsyay oldyay.
#Ymay amenay isyay Obekay Yantbray andyay Iyay amyay 4 yearsyay oldyay.
#todo is title: the first alphabet of the word is upper case.
piglatin = [] # A list of the words in Pig Latin.
for word in message.split():
    # Seperate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    #print(prefixNonLetters)
    if(len(word) == 0):
        piglatin.append(prefixNonLetters)
        continue

     # Seperate the non-letters at the end of this word:
    suffixNonletters = ''
    while not word[-1].isalpha():
        suffixNonletters += word[-1]
        word =  word[:-1]

    # Remember if the word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # Make the word lowercase for translation

    # Seperate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    piglatin.append(prefixNonLetters + word + suffixNonletters)

# Join all the words back to the start or end of the word.
print(' '.join(piglatin))


### structure:
### prefix suffix and word.
# test:
# My name is Kobe Bryant and I am 4,000 years old.!=_!!