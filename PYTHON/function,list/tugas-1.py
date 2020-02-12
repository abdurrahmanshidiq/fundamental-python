def kaliDua (x):
    z = []
    for i in range(0,len(x)):
        z.append(x[i]*2)
    return (z) 

x=[1,3,5,7]

print(kaliDua(x))

########################################################################################################
# # Cara lain

lstO =[1,3,5,7]

def kaliDua(x):
    lstA = []

    for i in x:
        res = i*2
        lstA.append(res)
    return lstA

hasil = kaliDua(lstO)

# print(lstO)
# print(hasil)


    






