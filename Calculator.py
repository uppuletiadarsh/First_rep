def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
   return x/y

print('Enter your operation')
print('1 for addition')
print('2 subtraction')
print('3 for multiplication')
print('4 for division')
option = int(input('enter your option : '))
num1 = float(input('enter the number 1:'))
num2 = float(input('enter the number 2:'))

if(option==1):
    print(add(num1,num2))
elif(option==2):
    print(sub(num1,num2))
elif(option==3):
    print(mul(num1,num2))
elif(option==4):
    print(div(num1,num2))
else:
    print('Invalid Option')
