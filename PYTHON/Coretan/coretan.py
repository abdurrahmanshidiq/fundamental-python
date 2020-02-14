# number = 25

# for i in range(0,40):
#     print(i)
#     if i is number:
#         print(f'angka ditemuka {i}')
#         break
#     else:
#         print(f'angka tidak ditemukan')


# def disemvowel(word):
#     List = list(word)
#     Vowels = ["a", "e", "i", "o", "u"]
#     for letter in List:
#         if letter.lower() in Vowels:
#             List.remove(letter)
#     word = ''.join(List)
#     return word

# print(disemvowel("treehouse"))

# word = 'Today is Friday'
# def disemvowel(word):
#     vowelList = ['a', 'e', 'i', 'o', 'u']
#     wordList = list(word)  
#     word_list_copy = wordList[:]  
#     for letter in wordList: 
#         if letter.lower() in vowelList:
#             word_list_copy.remove(letter) 

#     word = ''.join(word_list_copy)  
#     return word

# print(disemvowel('Today is Firday'))

# even = [2, 4, 6, 8, 10, 12, 14, 2091] #2091 is the outlier and len(x) = 8
# odd = [1, 3, 5, 7, 9, 11, 13, 4720] #4720 is the outlier and len(x) = 8

# def find_outlier(x):
#     # Determine if list is even and length of list is odd
#     if sum(x) % 2 != 0 and len(x) % 2 != 0:
#         for x in x:
#             if x % 2 != 0:
#                 return x
#     # Determine if list is even and length of list is even
#     elif sum(x) % 2 != 0 and len(x) % 2 == 0:
#         for x in x:
#             if x % 2 != 0:
#                 return x
#     # Determine if list is odd and length of list is odd
#     elif sum(x) % 2 == 0 and len(x) % 2 != 0:
#         for x in x:
#             if x % 2 == 0:
#                 return x
#     # Determine if list is odd and length of list is even (PROBLEM)
#     elif sum(x) % 2 == 0 and len(x) % 2 == 0:
#         for x in x:
#             if x % 2 == 0:
#                 return x

# print (find_outlier(even))
# print (find_outlier(odd))




x= 399
res = list(str(x))
print(res)

