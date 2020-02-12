stockApple = 5
stockGrape = 7
stockOrange = 8

priceApple = 10000
priceGrape = 15000
priceOrange = 20000


qtyApple =  int(input('Masukkan jumlah Apel : '))
while qtyApple>stockApple :
    qtyApple = int(input('Quantity Melebihi Stock, Masukkan jumlah Apel : '))

qtyGrape =  int(input('\nMasukkan jumlah Anggur : '))
while qtyGrape>stockGrape :
    qtyGrape = int(input('Quantity Melebihi Stock, Masukkan jumlah Anggur : '))

qtyOrange =  int(input('\nMasukkan jumlah Jeruk : '))
while qtyOrange>stockOrange :
    qtyOrange = int(input('Quantity Melebihi Stock, Masukkan jumlah Jeruk : '))

TotalApple = qtyApple*priceApple
TotalGrape = qtyGrape*priceGrape
TotalOrange = qtyOrange*priceOrange
GrandTotal = TotalApple+TotalGrape+TotalOrange

print('Detail Belanja \n\n'+
f'Apel = {TotalApple}\n'+
f'Anggur = {TotalGrape}\n'+
f'Jeruk = {TotalOrange}\n\n'+
f'GRAND TOTAL = {GrandTotal}'
)

amountMoney = int(input('\nMasukan Jumlah Uang : '))
while amountMoney<GrandTotal:
    print(f'Uang Anda Kurang = {GrandTotal-amountMoney}')
    amountMoney = int(input('Masukan Jumlah Uang : '))

print(
    f'Terima Kasih, Kembalian Anda = {amountMoney-GrandTotal}\n\n'+
    'Silakan Ambil Belanjaan anda'
    )
    