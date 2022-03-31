#swapping of two number
'''a = int(input("enter a number:"))
b=int(input("enter a number;"))
a=a+b
b=a-b
a=a-b
print(a)
print(b)'''

#sum of digits
'''a=int(input("enter"))
sum=0
while(a>0):
    rem=a%10
    sum=sum+rem
    a=a//10
print(sum)    
'''

#number of arguments
'''import sys
print ('There are %d arguments'%len(sys.argv))
print ('Argument are', str(sys.argv))
print ('File Name is: ', sys.argv[0])'''

#copy the contents of one file to another
'''import sys
source=open(sys.argv[1],'r')
destination=open(sys.argv[2],'w')
while(True):
    new_line=source.readline()
    if new_line=='':
        break
    destination.write(new_line)
source.close()
destination.close()'''

#exception handling \
'''try:
    f1=open("hello.txt","r")
    f1.write("exception handling")
except IOError:
    print("file dont have permission ")
else:
    print("successfullly printed")
    f1.close() '''   
# insertion of cards in a list
'''def insert(list,n):
    index=len(list)
    for i in range(len(list)):
        index=1
        break
    if (index==len(list)):
        list=list[:index]+[n]
    else:
        list=list[:index]+[n]+list[index]
    return list


list=[1,2,4]
n=3
print(insert(list,n))'''

#arbitary arguments
'''def my_fruit(*arg):
    print("favourite fruit is",arg[1])

my_fruit("bannana","apple","orange")'''





