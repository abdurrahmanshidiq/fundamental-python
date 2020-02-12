consonant = ('B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','Y','V','X','Z')
vowel = ('A','E','I','O','U')
inWord = input('Masukkan kata : ')
ay = 'ay'
firstLetter = inWord[0]
firstLetter = str(inWord[0])
firstLetter = firstLetter.upper()

        
if firstLetter in vowel:
    print(f'{firstLetter} adalah Vokal')
    print(f'{inWord}{ay}')
elif firstLetter in consonant:
    print(f'{firstLetter} adalah Konsonan')
    lengthOfWord = len(inWord)
    c_firstLetter = inWord[0]
    removeFirstLetter = inWord[1:lengthOfWord]
    # removeFirstLetter = inWord[1:]
    print(f'{removeFirstLetter}{c_firstLetter}{ay}')
else:
    print(f'{inWord} bukan alfabet')



#######################################################################


def changeWord (text): 
    if text[0] in ['a','i','u','e','o']:
        text = text + 'yay'
    else:
        text = text[1:]+text[0]+'ay'

    print(text)

changeWord('Friday')