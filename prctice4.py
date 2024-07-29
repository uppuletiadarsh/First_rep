#Python program to print all non repeating character in string.
s = 'Python program to print all non repeating character in string.'
new =''
for i in s :
    count = s.count(i)
    if count==1:
        new = new +i
print(new)

#"Python 10 20 program20 to67 calc233ulate7269 sum o32323f inte33gers323 in string."
string = "Python 10 20 program20 to67 calc233ulate7269 sum o32323f inte33gers323 in string."
sum = 0
for i in string:
    if i.isdigit():
        sum = sum +int(i)
print(sum)

# removing space
string = "Python 10 20 program20 to67 calc233ulate7269 sum o32323f inte33gers323 in string."
new = ''
for i in string:
    if i !=' ':
        new = new +i

print(new)
# Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.


