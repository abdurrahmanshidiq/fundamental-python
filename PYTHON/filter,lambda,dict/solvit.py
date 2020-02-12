kata = ['Merdeka','Hello','Hellos','Sohib','Kari ayam']
print(kata)
search = input('Masukkan kata : ')

res = []

for i in kata:
    x = search.lower() in i.lower()
    if x == True:
        res.append(i)
print(res)











