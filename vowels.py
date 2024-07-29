# count vowels 

"""def Count(string):
    vowels = "aeiouAEIOU"
    Vow_count = 0
    for i in string:
        if i in vowels:
            Vow_count = Vow_count+1
    return Vow_count
a = input("Enter A string :")
print(Count(a))"""
        
"""# removing duplicates from list
a = [12,23,45,23,12,45,23,67,89,98,98]
b = []
for i in a:
    if i not in b :
        b.append(i)
print(b)"""
"""# 
a ='Write a function to sort a list of integers in ascending order.'
new = ''
for i in a:
    if i not in new:
        new = new+i
print(new)

#removing vowels 
a = 'Write a function to sort a list of integers in ascending order.'
vowels = "eaiouAEIOU"
new = ''
for i in a:
    if i not in vowels:
        new = new +i
print(new)"""



#Write a code that takes a string as input and returns the length of the longest substring that does not contain any vowels.
s = "Write a code that takes a string as"
vowels = "aeiouAEIOU"
new =[]
b = s.split()
for i in b:
    vow_c=0
    for chr in i:
        if chr in vowels:
            vow_c=vow_c+1
    new.append(vow_c)
print(new)

#swapping cases of vowels
s = "WrItE A cOdE thAt tAkEs A strIng As"
vowels = "aeiouAEIOU"
new = ''
for i in s :
    if i in vowels:
        new = new +i.swapcase()
    else:
        new = new +i
print(new)
