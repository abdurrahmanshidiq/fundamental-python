fruits = ['Apel', 'Anggur', 'Jeruk']
stock = [5, 7, 8]
price = [1000, 15000, 20000]

# fungsi untuk menampilkan semua data
def showData():
    if len(fruits) <= 0:
        print ("BELUM ADA DATA")
    else:
        for indeks in range(len(fruits)):
            print ("[%d] %s" % (indeks, fruits[indeks]))

# fungsi untuk menambah data buah
def insertData():
    fruitsBbaru = input("Jenis Buah: ")
    fruits.append(fruitsBaru)

# fungsi untuk belanja
def belanja():




# fungsi untuk menampilkan menu
def show_menu():
    print ("\n")
    print ("----------- MENU ----------")
    print ("[1] Show Data")
    print ("[2] Insert Data")
    print ("[3] Belanja")

    
    menu = int(input("PILIH MENU> "))
    print ('\n')

    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        belanja
    else:
        print ("Salah pilih!")