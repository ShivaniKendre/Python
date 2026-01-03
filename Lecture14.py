#List
#list can contain duplicate values
#list is mutable
#list is ordered
l = [10,20,30,40,50,10,20]
print("l =",l)
print(type(l))

#ways to create list
#empty list
#l = []
l= list()
print("Data type of l is:",type(l))
l.append(10)
l.append(20)
l.append(30)
print("l =",l)

#list using list() function
l=[10,20,30,40,50]
print("l =",l)

#using constructor
from array import *
arr=array("i",[10,20,30,40,50])
l=list(arr)
print("l =",l)

t=(10,20,30,40,50)
#l=list(t) or
l=list(x for x in t)
print("l =",l)
print("t =",t)

x=[10,20,30,40,50]
l=list(x)
print("Id of x is:",id(x))
print("Id of l is:",id(l))

s={10,20,30,40,50}
l=list(s)
print("l =",l)

d={"a":10,"b":20,"c":30}
l=list(d)
print("l =",l)

x="Hello"
l=list(x)
print("l =",l)

#list is mutable del=delete element, append=add element
l=[10,20,30,40,50]
l[0]=100
print("l =",l)
del l[2]
print("l =",l)
l.append(60)
print("l =",l)

#Accessing List Element
mylist = [10,20,30,40,50]
print("Forward List Indexes :")
print("mylist[0] ",mylist[0])
print("mylist[1] ",mylist[1])
print("mylist[2] ",mylist[2])
print("mylist[3] ",mylist[3])
print("mylist[4] ",mylist[4])

print("Reverse List Indexes :")
print("mylist[-1] ",mylist[-1])
print("mylist[-2] ",mylist[-2])
print("mylist[-3] ",mylist[-3])
print("mylist[-4] ",mylist[-4])
print("mylist[-5] ",mylist[-5])

#Using for in loop
l=[10,20,30,40]
for x in l:
    print("x =",x)
#end of loop

l=[10,20,30,40,50]
for x in range (0, len(l)):
    print(l[x])
#end of loop

#A list is a collection of values of same or different datatypes.
from array import *
l=[10,1.1,"JACK",[10,20,30],(40,50),array("i",[1,2,3]),{80,60,70},{'A':65,'B':66}]
for x in l:
    print("x =",x)
print(l[4][0])

#isinstance() function
from array import *
from collections.abc import *
l=[10,1.1,"JACK",[10,20,30],(40,50),array("i",[1,2,3]),{80,60,70},{'A':65,'B':66}]
for x in l:
    if isinstance(x, Iterable):
        for y in x:
            print(y,end=" ")
        #end of loop
        print()
    else:
        print(x)
    #end of if
#end of outer loop
