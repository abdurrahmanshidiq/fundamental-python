somelist =  [40,100,1,5,25,10] 

def minMax (x):
    min = x[0]
    max = x[0]
    for i in range(len(x)):
        if x[i]<min:
            min = x[i]        
        elif x[i]>max:
            max = x[i]

    return [x,min,max]


res = minMax(somelist)

print(f'Hasil List,Min,Max = {res}')
print(
    f'List = {res[0]}\n'
    f'Min = {res[1]}\n'
    f'Max = {res[2]}'
)

