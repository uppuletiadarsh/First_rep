# Python program to interchange first and last elements in a list
"""a = [1,2,3]
b = a.copy()
ln = len(a)-1
a[0] = a[ln]
a[ln] = b[0]
print(a)
# Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.

list1 = [1,2,3,4]
list2 = list1.copy()
ln = len(list1)-1
print("The Lenght Of the list :",ln)
pos1 = int(input("enter Posi2 :"))
pos2 = int(input("Enter Posi2 :"))
if pos1 > 0 and pos2 > 0 and pos1 < ln and pos2 < ln :
    list1[pos1] = list2[pos2]
    list1[pos2] = list2[pos1]
    print(list1)
elif pos1 == 0 and pos2 > 0 or pos2== 0 and pos1 > 0  and pos1 < ln and pos2 < ln:
    list1[pos1],list1[pos2]=list1[pos2],list1[pos1]
    print(list1)
else:
    print("enter Proper Positions")"""
# replacing a given char in list in place of 10
"""a = [10,20,30,40,10,20,40,10]
b = input("Enter a single charracter :")
new = []
if len(b) == 1:
    for i in a :
        if i == 10:
            new.append(b)
        else:
            new.append(i)
else:
    print("enter only a single character")
print(new)"""
# replacing a given char in list FOR STRING in place of 'a
"""a = ['adarsh','avinesh','abhi']
b = input("Enter a single charracter :")
new = []
if len(b) == 1:
    for i in a :
        for c in i:
           if c == 'a':
               new.append(b)
           else:
               new.append(c)
    print()
else:          
    print("enter only single char")
print(new)
# Python | Ways to find length of list
a = [10,20,30,40,10,20,40,10]
c = 0
for i in a:
    c=c+1
print("the Length Of the list :",c)          
"""
 # Maximum of two numbers in Python
"""a = [10,20,30,40,10,20,40,10]
a.sort()
print(a)
h1 = len(a)-1
h2 = len(a)-2
num1 = a[h1]
num2 = a[h2]
print(num1+num2)"""

# Python Program to find sum and average of List in Python
"""a = [10,20,30,40,10,20,40,10]
sum =0
avg = 0
for i in a:
    sum = sum + i
    avg = sum/len(a)
print(sum)
print(avg)"""

# removing vowels in words of list
"""a = ['Adarsh','anil','Avinesh']
vowels = 'aeiouAEIOU'
new = []
for words in a:
    for word in words:
        if vowels in word:
            a.remove(word)
        
print(a)
 
#Python program to print even numbers in a list

a = [10,20,31,41,10,21,40,10]
new = []
for i in a :
    if i % 2 == 0:
        new.append(i)
print(new)

# Python3 Code to Demonstrate Remove empty List
a = [1,2,3,[],3,6,[]]
new = []
for i in a:
    if i :
        new.append(i)
print(new)"""




