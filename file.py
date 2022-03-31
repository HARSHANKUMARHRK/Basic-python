#armstrong number
'''num=int(input("enter a number:"))
temp=num
sum=0
while(num>0):
    rem=num%10
    sum=sum+rem**3
    num=num//10
if(temp==sum):
    print("the given number is armstrong  number")
else:
    print("th
    e given number is not armstrong number")'''


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


#mean median mode
'''def mean(list,n):
    get_sum=sum(list)
    mean=get_sum/n
    return mean

def median(list,n):
    if(n%2==0):
        median1=list[n//2]
        median2=list[n//2-1]
        median=(median1+median2)/2
    else:
        median=list[n//2]
    return median
def mode(list,n):
    fre={}
    for i in list:
        fre.setdefault(i,0)
        fre[i]+=1
    hifre=max(fre.values())
    high=[]
    for n,k in fre.items():
        if(k==hifre):
            high.append(n)
    return high 

n= int(input("enter the number of element in the list"))
a=[]
for i in range(n):
    a.append(int(input("enter number")))
print("mean of the given number is ",mean(a,n))
print("median of the given number is ",median(a,n)) 
print("mode of the given number is ",mode(a,n))'''

#duplicates in array
'''def dups (arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                print(arr[j])

arr = [1,2,3,4,2,7,8,8,3]
print("duplicate arr elements are:")
dups(arr)'''

#unique list
'''def uniquelist(list1):
    unique_list=[]
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print(x)

list1=[10,20,10,30,40,40]
uniquelist(list1)'''

#gcd
'''a= int(input("enter a number"))
b=int(input("enter a number"))
def gcd (a,b):
    rem =  a%b
    if(rem==0):
        return b
    else:
        return gcd(b,rem)

print(gcd(a,b))

gcd(46,6)'''

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



#binary search
# Returns index of x in arr if present, else -1
'''def binary_search(arr, low, high, x):

	# Check base case
	if high >= low:

		mid = (high + low) // 2

		# If element is present at the middle itself
		if arr[mid] == x:
			return mid

		# If element is smaller than mid, then it can only
		# be present in left subarray
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		# Else the element can only be present in right subarray
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		# Element is not present in the array
		return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
	print("Element is present at index", result)
else:
	print("Element is not present in array")'''

#linear search

'''def search(arr, x):

	for i in range(len(arr)):

		if arr[i] == x:
			return i

	return -1

arr=['hi','hello','world']
x='hello'
print("element at",search(arr,x))'''

#factorial with reccursion
'''
def f(a):
    if(a==2):
        return a
    else:
        return (a*f(a-1))

print("factorial of 3 is",f(3))'''

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

print("",fib(10))    '''   

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
print("out of try,except,else and finally block")               
'''
#insert and pop
'''a=[10,20,30,40,50]
a.insert(2,60)
print(a)
a.pop()
print(a)'''

# Python Program to Count Vowels in a String

'''str1 = input("Please Enter Your Own String : ")
vowels = 0
 
for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A'
       or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
 
print("Total Number of Vowels in this String = ", vowels)'''

#greatest of three numbers
'''a = float(input("Please Enter the First value: "))
b = float(input("Please Enter the First value: "))
c = float(input("Please Enter the First value: "))

if (a > b and a > c):
          print("{0} is Greater Than both {1} and {2}". format(a, b, c))
elif (b > a and b > c):
          print("{0} is Greater Than both {1} and {2}". format(b, a, c))
elif (c > a and c > b):
          print("{0} is Greater Than both {1} and {2}". format(c, a, b))
else:
          print("Either any two values or all the three values are equal")'''


#electricity bill
# Python Program to Calculate Electricity Bill
#Write a python program to input electricity unit charges and calculate total electricity bill according to the given condition:
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit	
#For next 100 units Rs. 1.20/unit For unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill
 
'''units = int(input(" Please enter Number of Units you Consumed : "))

if(units < 50):
    amount = units * 2.60
    surcharge = 25
elif(units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35
elif(units <= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45
else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75

total = amount + surcharge
print("Electricity Bill =", total)'''

#reversing number

# Python Program to Print Natural Numbers in Reverse Order
 


#quadratic eqn
## Python Program to find roots of a Quadratic Equation

#students grade

# Python Program to find Student Grade
 
# Python Program to find Student Grade
 
'''biology = float(input(" Please enter biology Marks: "))
math = float(input(" Please enter Math score: "))
computers = float(input(" Please enter Computer Marks: "))
physics = float(input(" Please enter Physics Marks: "))
chemistry = float(input(" Please enter Chemistry Marks: "))

total = biology + math + computers + physics + chemistry
percentage = (total / 500) * 100

print("Total Marks = ",total)
print("Marks Percentage = ",percentage)

if(percentage >= 90):
    print("A Grade")
elif(percentage >= 80):
    print("B Grade")
elif(percentage >= 70):
    print("C Grade")
elif(percentage >= 60):
    print("D Grade")
elif(percentage >= 40):
    print("E Grade")
else:
    print("fail")'''

#count number of digits
# Python Program to Count Number of Digits in a Number using Functions

'''def Counting(Number):
    Count = 0
    while(Number > 0):
        Number = Number // 10
        Count = Count + 1
    print(" Number of Digits in a Given Number = " ,Count)

Counting(1234)'''

#concadinate string
# Python Program to Concatenate Strings

'''concat1 = 'Tutorial ' 'Gateway'
print("The Final String = ", concat1)

concat2 = ('Python ' 'Programming ' 'Examples')
print("The Final String = ", concat2)'''

#largest and smallest in a list
'''NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

print("The Smallest Element in this List is : ", min(NumList))
print("The Largest Element in this List is : ", max(NumList))'''
#output
'''Python largest and smallest list number output

Please enter the Total Number of List Elements: 5
Please enter the Value of 1 Element : 50
Please enter the Value of 2 Element : 45
Please enter the Value of 3 Element : 33
Please enter the Value of 4 Element : 78
Please enter the Value of 5 Element : 66
The Smallest Element in this List is :  33
The Largest Element in this List is :  78'''

#Write a Python program:	tuple1 = (10,50,20,40,30)
#Write a Python program:	tuple1 = (10,50,20,40,30)
#i#.	To display the elements 10 and 50 from tuple1
#ii.	To display length of a tuple1.
#iii.	To find the minimum element from tuple1.	
#iv.	To add all elements in the tuple1.
#v.	To display same tuple1 multiple times
#first question
'''tuple1=(10,50,20,40,30)
n= int(input("enter a number to multiply the tuple"))
print("",tuple1[0:2])
#second question
print("",len(tuple1))
#third question
print("",min(tuple1))
#fourth question
print("",sum(tuple1))
#fifth question
print("",(tuple1)*n)'''

#Write a python program to Manipulate using list.
#i.	To add new elements to the end of the list
#ii.	To reverse elements in the list	
#iii.	To display same list elements multiple times.
#iv.	To concatenate two list
#v.	To sort the elements in the list in ascending order.

'''n=int(input("enter a number to multiply the list:"))
a=[10,20,30,40,50]
a.append(60)
print(a)

a.reverse()
print(a)

print("multiplication of list",a*n)

b=[80,90,60,70,50]
c=a+b
print(c)

print("ascending order:"a.sort())
print("ascending order of list b:",b.sort())'''

#matrix addition
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

#scalar,transpose determinant of matrix
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



#string anagram
'''def areanagram(str1,str2):
    n1=len(str1)
    n2=len(str2)
    if(n1!=n2):
        return 0
    str1=sorted(str1)
    str2=sorted(str2)
    for i in range(0,n1):
        if (str1[i]!=str2[i]):
            return 0
        return 1
str1=input("enter a string")
str2=input("enter a string")
str1=str1.lower()
str2=str2.lower()
if(areanagram(str1,str2)):
    print("the string are anagram to each other:")
else:
    print("not anagram to each other")   '''                 

#alphabetical order
'''a= input("enter a string")
b=sorted(a)
a="".join(b)
print(a)'''

#selection sort
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

#insertion sort

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

#commandline arguments

'''import sys
file=open(sys.argv[1],"r+")
wordcount={}
for word in file.read().split():
    if(word not in wordcount):
        wordcount=1
    else:
        wordcount+=1
file.close()
maxfreq=0
for key in wordcount.keys():
    if(wordcount[key]>maxfreq):
        maxfreq=wordcount[key]
    print("most specified word in the file")
for key in wordcount.keys():
    if(wordcount[key]==maxfreq):
        print(key)'''                    


#reversing a string
'''def reverse(str):   
    str = str[::-1]   
    return str
str="hello"     
print("after reversing ",reverse(str))  '''

#sum of number between 100 to 200
'''sum = 0 
for i in range(100,201): 
	sum += i 
print(sum)'''

#exponent
'''n=int(input("enter a number"))
m=int(input("enter second number"))
c=n**m
print(c)'''

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

#leap year
'''def leap(year):
    if(year%400==0 or year%4==0 and year%100!=0):
        print("entered year is leap year")
    else:
        print("entered year is not a leap year")   

print(leap(2004))
print(leap(2022))     '''   

'''#python program to find number of words characters 

# Python implementation to compute
# number of characters, words, spaces
# and lines in a file

# Function to count number
# of characters, words, spaces
# and lines in a file
def counter(fname):

	# variable to store total word count
	num_words = 0
	
	# variable to store total line count
	num_lines = 0
	
	# variable to store total character count
	num_charc = 0
	
	# variable to store total space count
	num_spaces = 0
	
	# opening file using with() method
	# so that file gets closed
	# after completion of work
	with open(fname, 'r') as f:
		
		# loop to iterate file
		# line by line
		for line in f:
			
			# incrementing value of
			# num_lines with each
			# iteration of loop to
			# store total line count
			num_lines += 1
			
			# declaring a variable word
			# and assigning its value as Y
			# because every file is
			# supposed to start with
			# a word or a character
			word = 'Y'
			
			# loop to iterate every
			# line letter by letter
			for letter in line:
				
				# condition to check
				# that the encountered character
				# is not white space and a word
				if (letter != ' ' and word == 'Y'):
					
					# incrementing the word
					# count by 1
					num_words += 1
					
					# assigning value N to
					# variable word because until
					# space will not encounter
					# a word can not be completed
					word = 'N'
					
				# condition to check
				# that the encountered character
				# is a white space
				elif (letter == ' '):
					
					# incrementing the space
					# count by 1
					num_spaces += 1
					
					# assigning value Y to
					# variable word because after
					# white space a word
					# is supposed to occur
					word = 'Y'
					
				# loop to iterate every
				# letter character by
				# character
				for i in letter:
					
					# condition to check
					# that the encountered character
					# is not white space and not
					# a newline character
					if(i !=" " and i !="\n"):
						
						# incrementing character
						# count by 1
						num_charc += 1
						
	# printing total word count
	print("Number of words in text file: ", num_words)
	
	# printing total line count
	print("Number of lines in text file: ", num_lines)
	
	# printing total character count
	print('Number of characters in text file: ', num_charc)
	
	# printing total space count
	print('Number of spaces in text file: ', num_spaces)
	
# Driver Code:
if __name__ == '__main__':
	fname = 'hii.txt'
	try:
		counter(fname)
	except:
		print('File not found')'''


#copying a fiile using command line arguments
'''import sys
try:

    def copy(f1,f2):
        source=open(f1,"r")
        destination=open(f2,"w")
        while (True):
            new_line=source.readline()
            if new_line=="":
                break
            destination.write(new_line)
            source.close()
            destination.close()
except IOError:
    print("THE GIVEN FILE IS NOT EXISTING")
    new_source=str(input("enter the file"))
    new_destination=str(input("enter the secnd file"))
copy(new_source,new_destination)'''

#newtons method for square root
'''a=int(input("enter a number"))
x=int(input("enter a number"))
y=(x+a/x)/2
print(" the square root of ",a,x ,"is ",y)'''

#descending order
'''n=int(input("enter element"))
for i in range(n,1,-1):
    print(i)'''

#
'''tuple1=(10,50,20,40,30)
print(tuple1[0])   
print(tuple1[1]) 

print("length of tuple1",len(tuple1))

print("minimum",min(tuple1))

print("sum",sum(tuple1))

n= int(input("enter a number to multiply"))
a=n*tuple1
print(a)'''

#dic
'''d1= {1:'a',2:'b',3:'c'}
d2= {1:'a',4:'b',5:'c'}
d3= {}
for key, val in d1.items():
    if key not in d2.keys():
        d3.update({key:val})
print(d3)'''


































                                  
