# #SOAL 1

# #Cara 1

# # ['hello','my','name','is','bean']
# # [   0   , 1  ,   2  , 3  ,   4  ]  
# # x.reverse() 
# # z = x[0].split()
# # print(z)
# # print(x)

# # x = 'hello my friend'
# # x = x.split()

# # finalRes = []
# # for val in x:
# #     res = val[::-1]
# #     finalRes.append(res)

# # fullSentence = ' '.join(finalRes)
# # print(fullSentence)

# # ###################################################
def sentReverse (sentence):
    pisah = sentence.split()
    finalRes = []
    fullSentence = ''
    for val in pisah:
        res = val[::-1]
        finalRes.append(res)
    fullSentence = ' '.join(finalRes)
    return (fullSentence)

    # print(finalRes)
    
print(sentReverse('hello my name is bean'))
# ###################################################################

# #Soal 2


# # y = [2, 4, 0, 1, 11]
# # #idx[0  1  2  3  4 ]

# # indeks0 = y.index(0) #angka 0 terdapat pada index 2 --> index 2
# # frontLis = y[0:indeks0] #angka pada index 0 sampai 2 adalah = [2,4]
# # frontSum = sum(frontLis) # 2+4 = 6
# # # print(indeks0)
# # # print(frontLis)
# # # print(frontSum)

# # indeks1 = y.index(1) #angka 1 terdapat pada indeks 3 --> index 3
# # backLis = y[indeks1+1:] #indeks 3 ditambah 1 adalah = index 4, kemudian angka pada indeks 4 adalh 11 = [11]
# # backSum = sum(backLis) #11+0 = 11
# # # print(indeks1)
# # # print(backLis)
# # # print(backLis)

# # totalSum = frontSum+backSum # 6+11 = 17
# # print(totalSum)

# #########################################################################################################################

def sum01 (lis):
    indeks0 = lis.index(0)
    frontLis = lis[0:indeks0]
    frontSum = sum(frontLis)

    indeks1 = lis.index(1)
    backLis = lis[indeks1+1:]
    backSum = sum(backLis)

    totalSum = frontSum+backSum
    print(totalSum)

# sum01([2, 4, 0, 1, 11])
# sum01([7, 0, 3, 1, 7, 9])
# sum01([5, 0, 3, 2, 1])
########################################################################

seq = ['soup','dog','salad','cat','great']


# res = list(filter(lambda word: word[0]=='s',seq))
res = []

for i in seq:
    if i[0] == 's':
        res.append(i)

# print(res)

###########################################################################
n = ['foo', 'bar', 'baz']
while n :
    print(n.pop(-1))