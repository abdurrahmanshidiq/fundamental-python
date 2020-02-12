text = input('Masukkan kalimat : ')
text1 = text.lower()
huruf = input('Masukkan karakter yang ingin dihitung : ')
huruf1= huruf.lower()

hitung = text1.count(huruf1)

print('Terdapat karakter '+huruf1+' sebanyak '+str(hitung))