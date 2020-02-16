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
inputAngka = int(input('Masukkan Angka : '))

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

print(f'Perulangannya adalah : {persistence(inputAngka)}')

