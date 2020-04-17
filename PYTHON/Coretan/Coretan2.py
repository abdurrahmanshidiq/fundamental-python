# print(list(range(0,3)))

# x = 399
# x = str(x)
# lis = list(x)
# # print(lis)
#1 Mengubah angka menjadi list integer
# def turnToList (num):
#     listnum = []
#     for i in numbers:
#         angka = int(i)
#         listnum.append(angka)
#     return listnum
# print(turnToList(numbers))

# #2 Mengkalikan angka dalam list integer
# def multiplyList (lisNum):
#     multiply = 1
#     for i in lisNum:
#         multiply = multiply * i 
#     return multiply
# print(multiplyList(turnToList(numbers)))

###########################################################################
# inputAngka = int(input('Masukkan Angka : '))

# #Mengubah input(string) menjadi list angka(integer)

def turntoList (num) :
    listAngka = []
    for i in str(num):
        angka = int(i)
        listAngka.append(angka)
    return listAngka

# print(turntoList(inputAngka))

# #mengkalikan angka di dalam list integer

def multiply (lisNum):
    multiplyRes = 1
    for i in lisNum:
        multiplyRes = multiplyRes * i
    return multiplyRes

# print(multiply(turntoList(inputAngka)))

#persistence number

def persistence (numbers):
   
    count = 0
    print(numbers)
    while numbers > 9:
        lisOfNum = turntoList(str(numbers))
        multOfNum = multiply(lisOfNum)
        print(multOfNum)
        numbers = multOfNum
        count += 1
    return count

# print(f'Perulangannya adalah : {persistence(inputAngka)}')

##############################################################################################################

# x = 'Hhhellooooaaa'
# x = x.lower()

# print(x.count('a'))

inpWord = input('Masukkan Kata : ') # Hhelooo
inpWord = inpWord.lower() #hhelooo

def benarSalah (word):
    eachOfLetter = []  #[2, 2, 1, 1, 3, 3, 3]
    boolList = []
    boolVal = 0
    for i in word:
        countLetter = word.count(i)
        eachOfLetter.append(countLetter) 
        
    #################################################################
    # if 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 in eachOfLetter:
    #     boolVal = False
    # else:
    #     boolVal = True
    #################################################################

    for i in eachOfLetter:
        if i >1 :
            boolList.append(False)
        else:
            boolList.append(True)

    if False in boolList:
        boolVal = False
    else:
        boolVal = True
    # return eachOfLetter 
    return boolVal

print(benarSalah(inpWord))  


#########################################################################################

# inNum = int(input('enter number: '))  

# coolNumbers = [3, 1, 88, 7, 20, 95, 26, 7, 9, 34]
# if inNum in coolNumbers:
#    print("26 is in")
# else:
#     print(f'{inNum} not in list')


# days = ['Sunday', 'Monday', 'Tuesday']
# # for i in range(len(days)):
# #     print(f'Loop i : {i}')
# #     print(f'Loop {i} : {days[i]}')



num = 23455
#LIST COMPREHENSION
lisnum = [int(i) for i in str(num)]
print(lisnum)

#NORMAL LOOP
lisnum2 = []
for i in str(num):
    lisnum2.append(int(i))
print(lisnum2)