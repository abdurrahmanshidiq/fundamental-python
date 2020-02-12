inApel = int(input("Berapa jumlah apel yang ingin dibeli : "))
inAnggur = int(input ("Berapa jumlah anggur yang ingin dibeli : "))
inJeruk = int(input ("Berapa jumlah jeruk yang ingin dibeli : "))

stkApel = 5
stkAnggur = 7
stkJeruk = 8

prcApel = 10000
prcAnggur = 15000
prcJeruk = 20000

if inApel <= stkApel and inAnggur <= stkAnggur and inJeruk <= stkJeruk :
    print (f"Total harga apel = Rp {inApel*prcApel}\nTotal harga Anggur = Rp {inAnggur*prcAnggur}\nTotal harga jeruk = Rp {inJeruk*prcJeruk}\nGrand Total = Rp {(inApel*prcApel)+(inAnggur*prcAnggur)+(inJeruk*prcJeruk)}")
elif inApel > stkApel and inAnggur <= stkAnggur and inJeruk <= stkJeruk :
    print(f'Kesalahan input, Stok Apel Kurang {inApel}/{stkApel} \nGRAND TOTAL = Rp {(((inApel*prcApel)+(inAnggur*prcAnggur)+(inJeruk*prcJeruk))*0)}')
elif inApel <= stkApel and inAnggur > stkAnggur and inJeruk <= stkJeruk :
    print(f'Kesalahan input, Stok Anggur Kurang {inAnggur}/{stkAnggur} \nGRAND TOTAL = Rp {(((inApel*prcApel)+(inAnggur*prcAnggur)+(inJeruk*prcJeruk))*0)}')
elif inApel <= stkApel and inAnggur <= stkAnggur and inJeruk > stkJeruk :
    print(f'Kesalahan input, Stok Jeruk Kurang {inJeruk}/{stkJeruk} \nGRAND TOTAL = Rp {(((inApel*prcApel)+(inAnggur*prcAnggur)+(inJeruk*prcJeruk))*0)}')
else :
    print(f'Kesalahan input,\nStok Apel Kurang {inApel}/{stkApel}\nStok Anggur Kurang {inAnggur}/{stkAnggur}\nStok Jeruk Kurang {inJeruk}/{stkJeruk}\nGRAND TOTAL = Rp {(((inApel*prcApel)+(inAnggur*prcAnggur)+(inJeruk*prcJeruk))*0)}')