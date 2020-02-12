# z=''
# for x in range(5,0,-1):
#    for y in range(0,x):
#       z += ' * '
#    z += '\n'
# for item in range(5):
#    for item1 in range(0, item+1):
#       z += ' * '
#    z += '\n'
# print(z)

z=''
for x in range(5,0,-1):
   for y in range(0,x):
      z += ' * '
   z += '\n'
for item in range(1,5,1):
   for item1 in range(0, item+1):
      z += ' * '
   z += '\n'
print(z)
