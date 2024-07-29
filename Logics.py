"""# Prime check
count = 0
a = int(input("enter a number to check Prime or Not :"))
for b in range(1,a+1):
    if (a%b==0):
        count=count+1
if(count<=2):
    print('prime')
else:
    print('not a prime')   

# count Vowels in string

vow = "aeiouAEIOU"
str1 = input("Enter the string :")
count = 0
for a in str1:
    if(a in vow):
        count= count+1
print('The Number of Vowels :',count)"""

"""#reversing a string
a = input('enter a string :')
b = a[::-1]
print(b)"""
a = int(input("enter :"))
for b in range(a):
    for j in range(b):
        print('*',end=' ')
    print()