massa = float(input('Masukkan berat badan : '))
tinggi = float(input('Masukkan tinggi badan : '))
konversi = tinggi/100

imt = (massa/(konversi**2))

if imt < 18.5:
    print(str(imt)+', BERAT BADAN KURANG !')
elif imt >= 18.5 and imt <= 26.5:
    print(str(imt)+', BERAT BADAN IDEAL !')
elif imt >= 25.0 and imt <= 29.9:
    print(str(imt)+', BERAT BADAN BERLEBIH !')
elif imt >= 30.0 and imt <= 39.9:
    print(str(imt)+', BERAT BADAN SANGAT BERLEBIH !')
else :
    print(str(imt)+', OBESITAS LO !')