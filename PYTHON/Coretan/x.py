list_word = ['merdeka', 'hello', 'sohib', 'kari ayam', 'pesawat', 'mobil', 'loker', 'kamar', 'saya', 'motor', 'pertamax', 'merah']
keyword = input('user input: ')

def filtered(x):
    # res = keyword.lower() in x.lower()
    if keyword.lower() in x.lower():
        return x
    else:
        return False

final = filter(filtered,list_word)
output = []
for i in final:
    output.append(i)

print(output)