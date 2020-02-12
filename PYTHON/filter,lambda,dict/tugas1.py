#Duplikat map menggunakan function

numList = [2,3,4]

def times2 (num):
    return num*2

def myMap(fun,lis):
    mapList = []

    for i in lis:
        res = fun(i)
        mapList.append(res)
    return mapList


myMapRes = myMap(times2,numList)
print(numList)
print(myMapRes)