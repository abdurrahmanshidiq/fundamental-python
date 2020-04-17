#No 1    

def phoneNum (lisNum):
    if len(lisNum) == 10:
        lisStr =[]
        for num in lisNum:
            lisStr.append(str(num))
        phoneStr = (''.join(lisStr)) #1234567890
        return f'({phoneStr[:3]}) {phoneStr[3:6]}-{phoneStr[6:]}'
    else:
        return False

# print(phoneNum([1,2,3,4,5,6,7,8,9,0])) #(123) 456-7890
# print(phoneNum([1,2,3,4,5,6,7,8,9]))
# print(phoneNum([1,2,3,4,5,6,7,8,9,0,1]))

#######################################################################
#No.2

def hashtag(txt):
    lisTxt = txt.split()
    joinTxt = ''.join(lisTxt)
    res = '#'+joinTxt
    failed = False
    if len(txt) < 1:
        return failed
    else:
        return res

# print(hashtag('Hello there how are you doing'))
# print(hashtag(''))

################################################################
#No.3

def unqChar (value):
    lisVal = list(value) #['K', 'K', 'K', 'L', 'L', 'L', 'M', 'M', 'N', 'K', 'K', 'K', 'L', 'L', 'L']
    unique=[]
    for i in lisVal:
        if i not in unique:
            unique.append(i)
    return unique


# print(unqChar('KKKLLLMMNKKKLLL'))
# print(unqChar('KLLMmKn'))
# print(unqChar([1,2,2,3,3]))

##############################################################################
#No.4

lisNum = []
count=1

while count<=7:
    inNum = int(input(f'Masukkan integer 0-9, angka ke- {count}: ')) 
    lisNum.append(inNum)
    if inNum > 9:
        break

    count += 1

print('\n')
print('-'*50)
print(f'Angka yang di input : {lisNum}')
lisNum.sort()
print(f'Sort ASC : {lisNum}')
lisNum.sort(reverse=True)
print(f'Sort DESC : {lisNum}')

even = []
odd = []

for i in lisNum:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

# print(f'Hasil Jumlah Bilangan Ganjil : {sum(odd)}')
# print(f'Hasil Jumlah Bilangan Genap : {sum(even)}')
