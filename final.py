'''# Python Program to Count Vowels in a String

str1 = input("Please Enter Your Own String : ")
vowels = 0
 
for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A'
       or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
 
print("Total Number of Vowels in this String = ", vowels)'''

#concatenation of string
'''str1= input("enter a string")
str2= input("enter a string")
c=str1+str2
print(c)'''

#Write a Python program to find maximum and minimum number in a list.

'''NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

NumList.sort()

print("The Smallest Element in this List is : ", NumList[0])
print("The Largest Element in this List is : ", NumList[Number - 1])'''

#fibnocci series

'''def fib(n):
    a=0
    b=1
    if(n==1):
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)

print("",fib(10))    

#reversing a digit
num = int(input("Enter the number: "))  
revr_num = 0    # initial value is 0. It will hold the reversed number  
def recur_reverse(num):  
    global revr_num   # We can use it out of the function  
    if (num > 0):  
        Reminder = num % 10  
        revr_num = (revr_num * 10) + Reminder  
        recur_reverse(num // 10)  
    return revr_num  
  
  
revr_num = recur_reverse(num)  
print("n Reverse of entered number is = %d" % revr_num)  

#Python program to display all integers within the range 100-200 whose sum of digits is an even number
for i in range(100,200):
    num = i
    sum = 0
    while(num!=0):
        digit = num%10
        sum = sum + digit
        num = num//10
    if(sum%2==0):
        print(i)


#to remove dups in list
list1 = [9,9,5,6,3,4,1,9,2,4,2]
list2 = list(set(list1))
print("New List : ", list2)

# Python Program to Count Number of Digits in a Number using Functions

def Counting(Number):
    Count = 0
    while(Number > 0):
        Number = Number // 10
        Count = Count + 1
    print(" Number of Digits in a Given Number = " ,Count)


#sum of digits
def getSum(n):
    
    sum = 0
    while (n != 0):
       
        sum = sum + (n % 10)
        n = n//10
       
    return sum
   
n = 12345
print(getSum(n))'''

#to insert a number in any position of listand remove
'''a=[13,15,16,17,18]
a[2]=34
a.pop(2)

print(a)'''

#print 1 to 100 
# Python program to print numbers from 1 to 100

'''print('Numbers from 1 to 100:')
for n in range(1, 101):
    print(n, end=' ')'''

#sum of tuples
'''a=(10,20,30)
b=sum(a)
print("sum of tuple is:",b)'''   

#linear search

'''def search(arr, x):

	for i in range(len(arr)):

		if arr[i] == x:
			return i

	return -1

arr=['hi','hello','world']
x='hello'
print("element at",search(arr,x))
'''

#exception handling

'''try:
    print("try block")
    x=int(input("enter a number:"))
    y=int(input("enter another number:"))
    z=x/y
except ZeroDivisionError:
    print("zero division block")
    print("division by 0 not possib;le")
else:
    print("else block")
    print("division",z)
finally:
    print("finally block")
print("out of try,except,else and finally block")   '''


#copy one file to another file
'''import sys 
f1=open(sys.argv[1],'r') 
f2=open(sys.argv[2],'w') 
while(True): 
filee=f1.readline() 
if filee=='': 
break 
f2.write(new_line) 
f1.close() 
f2.close() '''

#number of upper  case and lowercase
'''def up_low(s):      
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print( "No. of Upper case characters :",u,"No. of Lower case characters : ",l)

print("",up_low("HI hEllo World"))
'''

#tables
'''n=int(input("Enter the number to print the tables for:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)'''

#pallindrom
'''num=int(input("enter a number:"))
temp=num
sum=0
while(num>0):
    rem=num%10
    sum=sum*10+rem
    num=num//10
if(temp==sum):
    print("entered number is pallindrom")
else:
    print("entered number is not pallindrom")'''

#second largest number
'''NumList = []
Number = int(input("Enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Enter the Value of %d Element: " %i))
    NumList.append(value)

# Print the List Entered By the User
print("List: ", NumList)

NumList.sort()

print("The Second Largest Element in the Given List is: ", NumList[Number - 2])  '''  

#matrixaddition

'''a=[]
row=int(input("enter number of row of the matrix"))
col=int(input("enter number of col in the matrix"))
print("elements of first  matrix")
for i in range(row):
    a.append([])
    for j in range(col):
        a[i].append(int(input()))

b=[]
print("enter the element of second matrix")
for i in range(row):
    b.append([])
    for j in range(col):
        b[i].append(int(input()))

c=[]
for i in range(row):
    c.append([])
    for j in range(col):
        c[i].append(a[i][j]+b[i][j])

print("addition of two matrix is:")
for i in range(row):
    print(c[i]) '''   

#matrix multiplication

'''def Multiply(A,B):
    result=[ [0,0,0],[0,0,0],[0,0,0] ]
    #for rows
    for i in range(len(A)):
        #for columns
        for j in range(len(B[0])):
            #for rows of matrix B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    for p in result:
        print(p)

    return 0

A = [ [1, 2, 3],[6, 7, 4], [8, 10, 11] ]
  
B = [[1, 5, 3],[2, 6, 5], [7, 4, 9] ]

print("Result: ")
Multiply(A,B)'''


#transpose matrix
'''x=[[1,2,3],[2,4,8],[13,15,17]]
scalar=[[0,0,0],[0,0,0],[0,0,0]]
trans=[[0,0,0],[0,0,0],[0,0,0]]
n= int(input("enter a number to multiply"))
for i in range (len(x)):
    for j in range(len(x)):
        scalar[i][j]=x[i][j]*n
print("the resultant scalar matrix is:")
for r in scalar:
    print(r)

for i in range(len(x)):
    for j in range(len(x)):
        trans[j][i]=x[i][j]
print("the resultant transpose matrix is :")
for r in trans:
    print(r)'''

#faren to cel
'''celsius = float(input("Enter temperature in celsius :- "))
 
fahrenheit = (celsius * 9/5) + 32
 
print('%.2f Celsius is :- %0.2f Fahrenheit' %(celsius, fahrenheit))'''

#insertionsort
'''def insertionsort(a):
    for i in range (1,len(a)):
        currentvalue=a[i]
        pos=i
        while(currentvalue<a[pos-1]and pos>0):
            a[pos]=a[pos-1]
            pos=pos-1
            a[pos]=currentvalue

x=[10,3,7,4,8,9]
insertionsort(x)
print(x)      '''   

#selectionsort

'''def selectionSort(array):
  n = len(array)
  for i in range(n):
    # Initially, assume the first element of the unsorted part as the minimum.
    minimum = i

    for j in range(i+1, n):
      if (array[j] < array[minimum]):
        # Update position of minimum element if a smaller element is found.
        minimum = j

    # Swap the minimum element with the first element of the unsorted part.     
    temp = array[i]
    array[i] = array[minimum]
    array[minimum] = temp
    
  return array

# Driver code
array = [13, 4, 9, 5, 3, 16, 12]
print(selectionSort(array))'''

#linear search


'''def search(arr, x):

	for i in range(len(arr)):

		if arr[i] == x:
			return i

	return -1

arr=['hi','hello','world']
x='hello'
print("element at",search(arr,x))'''
    
#even and odd in a list
'''def splitevenodd(A): 
   evenlist = [] 
   oddlist = [] 
   for i in A: 
      if (i % 2 == 0): 
         evenlist.append(i) 
      else: 
         oddlist.append(i) 
   print("Even lists:", evenlist) 
   print("Odd lists:", oddlist) 
  
# Driver Code 
A=[1,2,3,4,5,6,7,8]
splitevenodd(A) '''

#print number between 200 to 300
'''for i in range(200,301):
    print(i)'''

#reversing digit(final)
'''number = int(input("Enter a positive integer: "))
rev = 0
while(number!=0):
    digit = number%10
    rev = (rev*10)+digit
    number = number//10
print(rev)'''

#between 12 and 37 sum  of even and odd
'''a=[]
b=[]
for i in range(12,38):
    if(i%2==0):
        a.append(i)
    else:
        b.append(i)
print("sum of even :",sum(a))
print("sum of odd:",sum(b)) '''   

#number of characters in a string   
'''st = input("enter a string")
dic={}
for ch in st:
    if ch in dic:
        dic[ch]+=1
    else:
        dic[ch]=1
for key in dic:
    print(key,':',dic[key])'''


    
        


















