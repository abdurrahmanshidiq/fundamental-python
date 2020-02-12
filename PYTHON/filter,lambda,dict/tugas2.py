#Duplikat filter menggunakan function

numList = [11, 12, 13 ,14 , 15, 16, 17, 18, 19, 20]

def even(num):
    return num % 2 == 0

def myFilert(fun,lis):
    filterList = []

    for i in lis:
        res = fun(i)
        if res == True:
            filterList.append(i)
    return filterList

myFilertRes = myFilert(even,numList)
print(numList)
print(myFilertRes)