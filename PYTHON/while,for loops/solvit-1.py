# z=''
# for x in range(5,0,-1):
#    for y in range(0,x):
#       z += ' * '
#    z += '\n'
# print(z)



z=''
for x in range(5):
   for y in range(5,x,-1):
      z += ' * '
   z += '\n'
print(z)