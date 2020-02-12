X = int(input('Masukkan kecepatan pertama : '))
Y = int(input('masukkan kecepatan kedua : '))
Z = int(input('Masukkan jarak antar keduanya : '))
to = int(input('Masukkan waktu awal : '))
waktuTempuh = (Z/(X+Y))*60

jam = round(waktuTempuh/60)
menit = waktuTempuh%60

resultjam = to+jam

print('waktu temunya adalah '+str(resultjam)+' jam '+str(menit)+' menit')