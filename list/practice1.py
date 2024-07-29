# Sum of Even Numbers in a list
"""list1 = [12,23,43,54,67,87,98,24,56,21,22,46]
sum = 0
for i in list1:
    if i%2==0:
        sum = sum + i
print(sum)
# Unique Elements 
un_list = []
list1 = ['a','a','b',10,20,10,2,3,4,2,3,4,90,9,0,9,10]
for i in list1:
    if i not in un_list:
        un_list.append(i)
print(un_list)
# List Reversal using list without slicing
rev = []
list1 = ['a', 'b', 10, 20, 2, 3, 4, 90, 9, 0]
ln = len(list1)-1
for i in range(ln,-1,-1):
    a = list1[i]
    rev.append(a)
print(rev)
# List Sorting
a = ['a','e','b','c','d']
b = sorted(a)
print(b)
# Use list comprehension to create a new list that contains squares of all numbers from 1 to 10.
a = [2,3,4,5,6,7]
sq = []
for i in a :
    res = i*i
    sq.append(res)
print(sq)
# Write a function that filters a list of integers to only include numbers greater than a specified number.
a = [10,20,30,40,50,60,69,70,78,79,34,2,348,67]
nu_limit =45
new = []
for i in a:
    if i > nu_limit:
        new.append(i)
print(new)
#List Concatenation:
# Write a function that concatenates two lists
new = []
def cancate(a,b):
    for i in a:
        new.append(i)
    for c in b :
        new.append(c)
    return new
l1 = [1,2,3,4]
l2 = [10,20,30,40]
print(cancate(l1,l2))

# Write a code that returns a list containing elements common to both  lists

s1 = [1,2,3,4,5]
s2 = [1,3,8,9,0]
common = []
for i in s1:
    if i in s2:
        common.append(i)
print(common)"""

# Write a function that modifies a list by removing duplicates and preserving the order of elements.
li = [1,2,1,2,3,4,1,3,5,6,4,5,6]
nl =[]
for i in li :
    if i not in nl :
        nl.append(i)
print(nl)

# high frequency
a = [1,2,1,1,2,2,2,2]
new = []
for i in a :
    c = a.count(i)
    new.append(c)
max = max(new)
ind = new.index(max)
print(a[ind])

# max and mini 
a = [1,2,3,4,56]
m = a[0]
mi = a[0]
for i in a :
    if i > m :
        m = i
    elif i < mi:
        mi = i
print(m)
print(mi)
# Python program to insert element at a given location in Array.

a = [1,2,3,5]
ln = len(a)-1
print("The length is :",ln)
char = input("Enter the char :")
ind = int(input("Enter the ind :"))
print("the length is :",ln)
if len(char)==1 and ind < ln :
    a.insert(ind,char)
else:
    print("enter the proper ind ")