X = int(input('Masukkan kecepatan pertama : '))
Y = int(input('masukkan kecepatan kedua : '))
Z = int(input('Masukkan jarak antar keduanya : '))
to = input('Masukkan waktu awal : ')
tJam = int(to[0:2])
tMenit = int(to[3:5])
waktuTempuh = (Z/(X+Y))*60

jam = round(waktuTempuh/60)
menit = waktuTempuh%60

resultJam = tJam+jam
resultMenit = tMenit+menit

print('waktu temunya adalah '+str(resultJam)+' jam '+str(resultMenit)+' menit')
