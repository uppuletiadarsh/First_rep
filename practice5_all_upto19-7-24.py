# 1 coding 	How do you find a length of a string ?
"""a = input("enter the string :")
b = len(a)
print("The length Of string :",b)

# 2 Write a program to calculate the sum of first N natural numbers ?
n = int(input("Enter the number :"))
sum = 0
for i in range(0,n+1):
    sum +=i
print("The sum is :",sum)

# 3 Write a program to read integer and convert it into float ?
n = int(input("Enter the number :"))
flt = float(n)
print("The integer :",n)
print("The Float Value :",flt)
"""
# 4 write a program to find grater among two numbers, take input from the key board ? 
"""num1 = eval(input("Enter The Num1 :"))
num2 = eval (input("Enter The Num2 :"))
if num1 < num2 :
    print("The greater number is :",num2)
elif num1==num2:
    print("Both are equal ")
else:
    print("The greater number is  :",num1)

# 5 Python Program to count occurrence of a given characters in string.
string = "Python Program to count occurrence of a given characters in string."
char = input("Enter A single Character :")
if len(char)==1:
    res = string.count(char)
    print(res)
else:
    print("Enter Only A single character")
# 6 Python Program to check if two Strings are Anagram.
strin1 = input("Enter string1 :")
strin2 = input("Enter string2 :")
a = strin1.lower()
b = strin2.lower()
c = strin1.replace(' ','')
d = strin2.replace(' ','')
e = sorted(c)
f = sorted(d)
if e == f :
    print("Anagram")
else:
    print("Not a Anagram")

# 7 Python program to remove blank space from string.
string = 'Python program to replace the string space with a given character.'
new = ''
for i in string:
    if i != ' ':
        new = new + i
print(new)
# 8 Python program to replace the string space with a given character.
string = 'Python program to replace the string space with a given character.'
char = input("Enter the Char :")
new = ''
for i in string:
    if len(char)==1:
        if i == ' ':
            new = new + char
        else:
            new = new + i
    else:
        print("Enter Only Single Char")
print(new) 
# 9 cancatenation using for loop
strin1 = input("Enter string1 :")
strin2 = input("Enter string2 :")
new = ''
for i in strin1:
    new = new + i
for b in strin2:
    new = new + b
print(new)
string = 'Python program to remove repeated character from string.'
new = ''
for i in string :
    if i not in new:
        new = new + i
print(new)
# 10 Python program to delete vowels in a given string.
vow = 'eaiouAEIOU'
string = 'Python program to delete vowels in a given string.'
new = ''
for i in string:
    if i in vow:
        pass
    else:
        new = new + i
print(new)
# 11 Python program to print all non repeating character in string.
string = 'aabccdeefggh'
new = ''
for i in string:
    count = string.count(i)
    if count == 1:
        new = new + i
print(new)
# 12 Python program to count the Occurrence Of Vowels & Consonants in a String.
string = 'abcde'
vow_c = 0
con_c = 0
vow = 'aeiouAEIOU'
for i in string:
    if i in vow:
        vow_c=vow_c+1
    else:
        con_c =  con_c + 1
print("The Vowel Count :",vow_c)  
print("The Consonant Count :",con_c)  """
# Python program to print the highest frequency character in a String:
st = 'aaabbcc'
new = {}
for i in st :
    count = st.count(i)
    new[i]=count
res = max(new,key=new.get)
print(res)



       

    




