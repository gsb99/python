'''
#to print all natural number from 1 to n-while loop
number=int(input('Enter any number'))
print('The list of natural numbers from 1 to {} are'.format(number))
i=1
while i<=number:
    print(i,end=' ')
    i=i+1

#to print all natural number from 1 to n-for loop
number=int(input('Enter any number'))
print('The list of natural numbers from 1 to {} are'.format(number))
for i in range(1,number+1):
    print(i,end=' ')

#to print all natural number in reverse order -while loop
number=int(input('Enter any number'))
print('The list of natural numbers in reverse order from {} to 1  are'.format(number))
i=number
while i>=1:
    print(i,end=' ')
    i=i-1


#to print even natural number   -while loop
number=int(input('Enter any number'))
print('The list of even number from 1 to {} are'.format(number))
i=0
while i<=number:
    print(i,end=' ')
    i=i+2

#to print even natural number   -for loop
number=int(input('Enter any number'))
print('The list of even number from 1 to {} are'.format(number))
for i in range(1,number+1):
    if i%2==0:
        print(i,end=' ')

#to print odd natural number   -while loop
number=int(input('Enter any number'))
print('The list of even number from 1 to {} are'.format(number))
i=1
while i<=number:
    print(i,end=' ')
    i=i+2

#to print odd natural number   -for loop
number=int(input('Enter any number'))
print('The list of even number from 1 to {} are'.format(number))
for i in range(1,number+1):
    i=i+2
    print(i,end=' ')

#sum of all  number-while loop
number=int(input('Enter any number'))
print('The sum of numbers from 1 to {} are'.format(number))
i=1
sum =0
while i<=number:
    sum=sum+i
    i = i + 1
    print(sum, end=' ')

#Multiplication table
num=int(input('enter the num'))
i=1
while i<=10:
    mul=i*num
    print(mul,end=' ')
    i=i+1

#enter the number and enter its reverse
#num = int(input('Enter the num'))
a = [10,20,30,40]
for i in reversed(a):
    if list(reversed(a)):
        print(i,end=' ')

#to find version of python
import sys
print('python version')
print(sys.version)

# programe to find num dividable and multiple by 7 and 5
n=[]
for i in range(1500,2701):
    if (i%7==0)and (i%5==0):
        n.append(i)
print(n)

#to accept word in reverse order
a ='Gauri'
#print(a[::-1])   or
for char in range(len(a)-1,-1,-1):
 print(a[char],end=' ')

#in given list find even or odd
a = [12,13,14,2,5,9]
for i in a:
    print(i)
    if (i%2==0):
        print('it is even')
    else:
        print('it is odd')

#To print item and its type
s = [12,'gauri',1+5j,True]
for i in s:
    print(i,type(i))

#print 0 to 6 except 3 and 6
for i in range(0,7):
    if(i==3 or i==6):
        continue
    print(i,end=' ')

s = input('enter the string')
d=l=0
for i in s:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        l=l+1
    else:
       pass
print('letters',l)
print('digits', d)
'''














