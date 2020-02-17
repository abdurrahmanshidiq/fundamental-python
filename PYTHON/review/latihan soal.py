#Removing vowels form word/sentence



# def noVowels (sentence):
#     vowels = ['a','i','u','e','o']
#     for x in sentence:
#         if x in vowels:
#             return True
#         else:
#             return False

# word = 'Today is Friday'
# filteredWord = list(filter(noVowels,word))
# filteredWord = ' '.join(filteredWord)
# print(filteredWord)
# # finalRes = ' '.join(filter(noVowels,))
# # print(finalRes)




##############################################################
#Soal No.1, Menghilangkan huruf vokal pada kalimat

#REMOVING VOWELS FROM SENTENCE CARA 1
def check (x):
    return x not in 'aiueo'

def no_vowel (string):
    resFilter = list(filter(check,string))
    return ''.join(resFilter)

# print(no_vowel('Today is Friday'))

#REMOVING VOWELS FROM SENTENCE CARA 2

def check (x):
    res = []
    for i in x:
        if i not in 'aiueo':
            res.append(i)
    return res

# #tanpa filter
# print(''.join(check('this is saturday')))

# #dengan filter
word = 'this is saturday'
myFilter = ''.join(list(filter(check,word)))
# print(myFilter)

############################################################################################

#Soal No.2, Mencari oulier number pada list integer

for num in genap:
    if num % 2 ==0:
        print(num, end = " ")

genap = [2,12,4,7,8]
ganjil = [3,11,7,4,9]

def outliers (listNum):
    even = []
    odd = [] 

    for i in listNum:
        if i % 2 == 0:
           even.append(i)
        else :
            odd.append(i)
    print (f'even = {even}')
    print (f'odd = {odd}')
    
    if len(even) > len(odd):
        return odd[0]
    else:
        return even[0]

# print(outliers(genap))
# print('\n')
# print(outliers(ganjil))


##########################################################################################################################

#Soal No.3, mencari banyaknya perkalian yang bisa dioperasikan pada list integer
#misal :
#399 --> [3,9,9] dikalikan menjadi 243
#243 --> [2,4,3] dikalikan menjadi 24
#24 -->  [2,4] dikalikan menjadi 8
#8  -->  [8]   tinggal 1 angka saja di list.
#operasi diatas akan me return banyaknya angka yang bisa dikali didalam list. jumlahnya 3 kali
#fungsi akan me return 3

inputAngka = int(input('Masukkan Angka : '))

#Mengubah input(int) menjadi list angka(integer)
def turntoList (num) :
    listAngka = []
    for i in str(num):
        angka = int(i)
        listAngka.append(angka)
    return listAngka
# print(turntoList(inputAngka))

#Mengkalikan angka di dalam list integer
def multiply (lisNum):
    multiplyRes = 1
    for i in lisNum:
        multiplyRes = multiplyRes * i
    return multiplyRes
# print(multiply(turntoList(inputAngka)))

#Perulangan number
def perulangan (numbers):
    count = 0
    print(numbers)
    while numbers > 9:
        lisOfNum = turntoList(str(numbers))
        multOfNum = multiply(lisOfNum)
        print(multOfNum)
        numbers = multOfNum
        count += 1
    return count

print(f'Perulangannya adalah : {perulangan(inputAngka)}')

###############################################################################################

#Soal N0.4, Jika pada sebuah kata terdapat huruf yang sama (lebih dari satu), Maka fungsi akan me return FALSE,
#namun jika pada kata tsb tidak ada huruf yang berulang, maka me retrun TRUE
#Contoh : Hello = FALSE --> karena huruf 'l' lebih dari satu
#         Kursi = TRUE --> semua huruf pada kata 'Kursi' tidak ada yang lebih dari satu

inpWord = input('Masukkan Kata : ')
inpWord = inpWord.lower()

def benarSalah (word):
    eachOfLetter = []  #[2, 2, 1, 1, 3, 3, 3]
    boolList = []
    boolVal = 0

    for i in word:
        countLetter = word.count(i)
        eachOfLetter.append(countLetter) 
        
    for i in eachOfLetter:
        if i > 1 :
            boolList.append(False)
        else:
            boolList.append(True)

    if False in boolList:
        boolVal = False
    else:
        boolVal = True
     
    return boolVal

print(benarSalah(inpWord))

##############################################################################################