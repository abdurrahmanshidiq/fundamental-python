# number = 25

# for i in range(0,40):
#     print(i)
#     if i is number:
#         print(f'angka ditemuka {i}')
#         break
#     else:
#         print(f'angka tidak ditemukan')


# def disemvowel(word):
#     List = list(word)
#     Vowels = ["a", "e", "i", "o", "u"]
#     for letter in List:
#         if letter.lower() in Vowels:
#             List.remove(letter)
#     word = ''.join(List)
#     return word

# print(disemvowel("treehouse"))

# word = 'Today is Friday'
# def disemvowel(word):
#     vowelList = ['a', 'e', 'i', 'o', 'u']
#     wordList = list(word)  
#     word_list_copy = wordList[:]  
#     for letter in wordList: 
#         if letter.lower() in vowelList:
#             word_list_copy.remove(letter) 

#     word = ''.join(word_list_copy)  
#     return word

# print(disemvowel('Today is Firday'))


#######################################################################
#FIND OUTLIERS NUMBER IN INTEGER LIST


# findEven = [160, 3, 1719, 19, 11, 13, -21]

# def find_outlier(integers):
#     evens = []
#     odds = []
#     for i in integers:
#         if i % 2 == 0:
#             evens.append(i)
#         else:
#             odds.append(i)

#     print ("Evens: ", evens)
#     print ("Odds: ", odds)
    
#     if len(evens) > len(odds):
#         return odds[0]
#     else:
#         return evens[0]

# print (find_outlier(findEven))

###########################################################################################################

#REMOVING VOWELS FROM SENTENCE

# def check (x):
#     res = []
#     for i in x:
#         if i not in 'aiueo':
#             res.append(i)
#     return res

# #tanpa filter
# print(''.join(check('this is saturday')))

# #dengan filter
# word = 'this is saturday'
# myFilter = ''.join(list(filter(check,word)))
# print(myFilter)

##########################################################################################################

# x= 399
# x = list(str(x))
# print(x)

#####################################################################################

numbers = input('Masukkan Angka : ')


#Mengubah angka menjadi list integer

#Cara 1
listNumbers = [int(i) for i in str(numbers)]
print(f'Cara 1 = {listNumbers}')

#Cara 2
# numbers = input('Masukkan Angka : ')
# listnum = []
# for i in numbers:
#     angka = int(i)
#     listnum.append(angka)
# print(f'Cara 2 = {listnum}')

#function nya
def turnToList (num):
    listnum = []
    for i in numbers:
        angka = int(i)
        listnum.append(angka)
    return listnum
# print(turnToList(numbers))


###################################################################################

#Mengkalikan angka dalam list integer

#Contoh
# def multiplyList(myList) : 
#     result = 1
#     for x in myList: 
#          result = result * x  
#     return result  
# list1 = [1, 2, 3]  
# list2 = [3, 2, 4] 
# print(multiplyList(list1)) 
# print(multiplyList(list2)) 

def multiply (listNum):
    multiplyRes = 1
    for i in listNum:
        multiplyRes = multiplyRes * i
    return multiplyRes

# print('Hasil Kalinya :')
# print(multiply(turnToList(numbers)))


###########################################################################

# def faktorisasi (inputAngka):
#     perulangan = []
#     menjadiList = turnToList(inputAngka)
#     perkalian = multiply(inputAngka)
#     print(f'listnya {menjadiList} dan perkaliannya {perkalian}')

# perulangan = []
# menjadiList = turnToList(inputAngka)
# while len(inputAngka) is not 1:
#     perkalian = multiply(inputAngka)
#     perulangan.append(perkalian)
# return perulangan

# def pengulanganList (inputAngka) :
#     listTerulang = []
#     while len(turnToList(inputAngka)>1:
#         listTerulang.append(turnToList(inputAngka))
#         multiply(inputAngka)

def persistence(num):
    count = 0
    while num >= 10:
        num = multiply(turnToList(numbers))
        count += 1
    return count
# print('Perulangannya : ')



#####################################################################

#Jawaban 1   
number = int(input("enter number :"))
product = 1
persistence = 0
print(number)
while number > 9:
    for digit in range(0, len(str(number))):
        product *= int(str(number)[digit])
    print(product)
    persistence += 1
    number = product
    product = 1
print("persistence:", persistence)


#jawaban 2
# def get_digits(num):
#     digits = []
#     while num:
#         num, digit = divmod(num, 10)
#         digits.append(digit)
#     return digits

# print(get_digits(399))

# def multiply_all(digits):
#     multiplier = 1
#     while digits:
#         multiplier *= digits.pop()
#     return multiplier

# print(multiply_all(get_digits(399)))

# def persistence(num):
#     count = 0
#     while num >= 10:
#         num = multiply_all(get_digits(num))
#         count += 1
#     return count

# print(persistence(399))
