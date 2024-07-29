"""
#square
n = 5
for i in range(n):
    for j in range(n):
        print("*",end=' ')
    print()"""

"""
#increasing Triangle
n = 5
for i in range(n):
    for j in range(i):
        print("*",end=' ')
    print()"""


"""
#decreasing triangle

n = 5
for i in range(n):
    for j in range(i,n):
        print('*',end=' ')
    print()"""

"""#right sided triangle

n = 5
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=" ")
    print()"""

"""
#left sided triangle
n= 5
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for j in range(i,n):
        print("*",end=' ')
    print()"""

"""n = 4
for i in range(0,n):
    for j in range(n):
        print("*",end=' ')
    print()"""
def draw_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j:
                print('*', end='')
            else:
                print(' ', end='')
        print()
n = 4
draw_square(n)
# Example usage:

