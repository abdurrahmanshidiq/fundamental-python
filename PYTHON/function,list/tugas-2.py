x=[11, 22, 34, 41, 52, 63, 71, 86]

def ganjilGenap (y):
    ganjil = []
    genap = []
    gG = []

    for i in x:
        if i%2 == 0 :
            genap.append(i)
        else :
            ganjil.append(i)

    gG.append(ganjil)
    gG.append(genap)
    return gG
    

hasil = ganjilGenap(x)

print(hasil)