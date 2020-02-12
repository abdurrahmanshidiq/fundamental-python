# listNum = [ 1, 2, 3, 4, 5]
# def genap(num) :
#     return num % 2 == 0

# listNum = list(filter(genap, listNum))
# print(listNum)

# # listNum = [ 1, 2, 3, 4, 5];

# # listNum = list(filter(lambda num: num % 2 == 0, listNum));
# # print(listNum);


listNum = [ 1, 2, 3, 4, 5]
def genap(num) :
    return num % 2 == 0


def hasil(fun,lis):
    x = []
    for i in lis:
        y = fun(i)
        if y == True:
            x.append(i)
    return x

xyz = hasil(genap,listNum)
print(listNum)
print(xyz)

