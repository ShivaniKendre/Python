#Array
#Syntax: 1
import array 
a=array.array("i",[10,20,30])
print("a = ",a)

#Syntax: 2
from array import *
b=array("i",[10,20,30,40,50])
print("b = ",b)

#Syntax: 3
import array as arr
c=arr.array("i",[10,20,30,40,50])
print("c =",c)

print("Forward Traversal:")
print("a[0]",a[0])
print("a[1]",a[1])
print("a[2]",a[2])
print("Backward Traversal:")
print("a[2]",a[2])
print("a[1]",a[1])
print("a[0]",a[0])

#Length of array
l=a.__len__()
print("Length of a = ",l)
#or
l = len(b)
print("Length of a = ",l)

#Array using for loop
print("Array a using for loop:")
for x in c:
    print("X = ",x)

for i in range(0,len(c)):
    print(c[i])
#or
for i in range(0,a.__len__()):
    print(a[i])

#Read an array of 5 integers and display it
import array
d=array.array("i",[])
for i in range (0,5):
    d.append(int(input("Enter array Element:")))

print("Tha Array is as following : ")
for x in d:
    print(x)

#
from array import *
arr=array("i",[])
for i in range(0,5):
    x=int(input("Enter array element : "))
    arr.append(x)

print("arr",arr)
s=0
for x in arr:
    s=s+x
print("Sum =",s)

#Maltidimensional Array
l=[[1,2,3],[4,5,6],[7,8,9]]
for x in l:
    for y in x:
        print(y,end=" ")
    print()






