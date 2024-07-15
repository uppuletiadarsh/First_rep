'''row = int(input('enter the number of rows:'))
for i in range(1,row+1):
    for j in range(1,i+1):
        print('$',end='')
    print(j)
for i in range(1,7):
    for j in range(1,i+1):
        print(j,end='')
    print()  '''
"""for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print() """

"""n = 5 #square
for i in range(n):
    for j in range(n):
        print("*",end=' ')
    print()"""
# increasing triangle
"""n = 5
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()"""

#decreasing triangle and if we give end space at last loop it will become pyramid
n = 5
for i in range(n):
    for j in range(i,n+1):
        print('',end=' ')
    for m in range(i+1):
        print("*",end='')
    print()
#second commit