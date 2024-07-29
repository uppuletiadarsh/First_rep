# Python program to replace the string space with a given character.
"""str1 = "Python program to replace the string space with a given character."
chr = input("Enter a Char :")
new = ''
for i in str1:
    if i == ' ':
        new = new+chr
    else:
        new = new+i
print(new)
"""
#Python program to convert lowercase vowel to uppercase in string.
"""str1 = "Python program to replace the string space with a given character."
new = ''
vow = "aeiou"
for a in str1:
    if a in vow:
        new = new+a.upper()
    else:
        new = new + a
print(new)"""

#Python program to concatenate two strings without using join() method.
"""string1= input("Enter the String1 :")
string2= input("Enter the String2 :")
new = ''
for i in string1:
    new = new +i
for b in string2:
    new = new+b
print(new)"""
"""string = "Python program to replace the string space with a given character."
chr = input("Enter a string to Replace In the place Of Space :")
new = ''
for i in string:
    if i == ' ':
        new = new +chr
    else:
        new = new +i
res = ''.join(new)
print(res)
"""
s =input("enter : ")
if s.isalnum():
    if s.isalpha():
        print("alpa")
    elif s.isdigit():
        print("dig")
    else:
        print("both alp and dig")
elif s.isspace():
    print("space")
else:
    print("special")