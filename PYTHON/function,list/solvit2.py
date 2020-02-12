# listInt = [40,100,1,5,25,10]

# listInt.sort()
# print(f'nilai tertingginya {listInt[0]}')
# print(f'nilai terendahnya {listInt[-1]}')

listInt = [40,100,1,5,25,10]

def minMax (x):
    listInt.sort()
    print(f'nilai terendahnya adalah {listInt[0]}')
    listInt.sort(reverse=True)
    print(f'nilai terendahnya adalah {listInt[0]}')

minMax(listInt)

    
