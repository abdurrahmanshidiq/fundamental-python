#SOAL 1

def sentReverse (text): 
    pisah = text.split()
    pisah.reverse()
    res = ' '.join(pisah)

    print(res)

sentReverse('Hello my friends')

###################################################################################

# SOAL 2
# [1,9,9] true
# [5,9,2,9] false
# [9,3,9] false
# [7,9,9,6] true

def has99 (lis):
    indeks = lis.index(9)
    if lis[indeks+1] == 9:
       return True
    else:
        return False


#Cara lain

# def has99 (lis):
#     indeks = lis.index(9)
#     return lis[indeks+1] == 9
      


print(has99([1,9,9]))
print(has99([5,9,2,9]))
print(has99([9,3,9]))
print(has99([7,9,9,6]))


#####################################################################################


# x = 'Hello my friends'
# x = x.split()
# # x.reverse()
# z = []
# for i in x:
#     y = i[::-1]
#     z.append(y)
# print(z)

# x.reverse()
# print(x)
# print(y)
# print