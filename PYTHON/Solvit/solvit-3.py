x = int(input('Masukan jumlah hari : '))
tahun = int(x/360)
selisih = int(x-360)
bulan = int(selisih/30)
hari = int(selisih-(bulan*30))

print( str(tahun)+' Tahun '+str(bulan)+' Bulan '+str(hari)+' Hari')