#Tuple
# Tuples are immutable and Sequential.
# The tuple is a collection of elements of different data types.
# The tuppal can contain duplicate elements.
# the tuple can contain another tuple, list, array, int, float, string, set, dictionary, etc. as its members.
# If the tuple contains mutable iterables, then we can change the elements in the mutaable iterables.
# the tupple supports forward and reverse indexes.
t=(10,20,30)
print("t = ",t)
from array import *
t=(10,1.1,(20,30,40),[50,60,70],array("i",[80,90,100]))
print("t =",t)
print("[4][0] = ",t[4][0])
t[4][0]=50
print("[4][0] = ",t[4][0])

# 4-Way to create tuple 

# Way-1
# empty tuple
t=()
print("Datatype of t = ",type(t))
print("t = ",t)

# Way-2
t=(10,20,30)
print("Datatype of t = ",type(t))
print("t = ",t)


# Way-3
from array import *
a=array("i",[10,20,30])
t=tuple(a)
print("Datatype of t = ",type(t))
print("t = ",t)

l=[40,50,60]
t=tuple(l)
print("Datatype of t = ",type(t))
print("t = ",t)
print("l = ",l)

t1=(80,90,100)
t=tuple(t1)
print("Datatype of t = ",type(t))
print("Id of t = ",id(t))
print("t = ",t)
print("Id of t1 = ",id(t1))
print("t1 = ",t1)

s={10,20,30,40,50}
t=tuple(s)
print("Datatype of t = ",type(t))
print("t = ",t)
print("s = ",s)

d={"A":65,"B":66}
t=tuple(d)
print("Datatype of t = ",type(t))
print("t = ",t)
print("d = ",d)

str="SHIVANI"
t=tuple(str)
print("Datatype of t = ",type(t))
print("t = ",t)
print("str = ",str)

# Way-4
# It is int data type 
t=10 
print("Datatype of t = ",type(t))
print("t = ",t)

t=10,20,30
print("Datatype of t = ",type(t))
print("t = ",t)

# it is tuple 
t=10,
print("Datatype of t = ",type(t))
print("t = ",t)

#loop in tuple
from array import *
t=(10,1.1,(20,30,40),[50,60,70],array("i",[80,90,100]))
print("t =",t)
for x in t:
    print("x = ",x)
# end of loop 

#Accessing tuple elements
t=(10,20,30)
print("Forward Index :")
print("t[0] =",t[0])
print("t[1] =",t[1])
print("t[2] =",t[2])
print("Reverse Index :")
print("t[-1] =",t[-1])
print("t[-2] =",t[-2])
print("t[-3] =",t[-3])

t=(10,20,30)
x=len(t)
print("x = ",x)

t=(10,20,30)
for i in range(0,len(t)):
    print(t[i])
#end of loop

# Tuple Methods
# Count Methods
t=(10,20,10.0,30,10,"10")
c=t.count(10)
print("count =",c)

# Index Methods 
t=(10,20,10,10.0,30,10,"10",20,30,40)
i=t.index(20)
print("i =",i)

# Create duplicate of tuple
t1=(10,20,30)
l=list(t1)
print("l = ",l)
t2 = tuple(l)
print("t1 =",t1)
print("t2 =",t2)
print("id of t1 =",id(t1))
print("id of t2 =",id(t2))

t=(30,50,10,20,40)
l1 = sorted(t)
l2 = sorted(t,reverse=True)
print("l2 =",l2)
print("l1 =",l1)
print("t =",t)
