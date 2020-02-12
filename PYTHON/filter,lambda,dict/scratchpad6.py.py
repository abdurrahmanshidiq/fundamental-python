# geektechstuff – Pig Latin version 2 (Impractical Python Excercise)
ay = 'ay'
way = 'way'
consonant = ('B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','Y','V','X','Z')
vowel = ('A','E','I','O','U')
user_sentence = input('Enter a sentence to translate to Pig Latin: ')
pig_latin_string =''

words = user_sentence.split()
print(words)

for user_word in words:
   print(user_word)

# getting first letter and making sure its a string and setting it to uppercase
   first_letter = user_word[0]
   first_letter = str(first_letter)
   first_letter=first_letter.upper()

   if first_letter in consonant:
      length_of_word = len(user_word)
      remove_first_letter = user_word[1:length_of_word]
      pig_latin = remove_first_letter+first_letter+ay
      pig_latin_string = pig_latin_string+' '+pig_latin
   elif first_letter in vowel:
      pig_latin = user_word+way
      pig_latin_string = pig_latin_string+' '+pig_latin
   else:
      print('?')
print(pig_latin_string)

