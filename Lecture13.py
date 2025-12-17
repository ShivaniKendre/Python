#Array functions and del statement
#apppend function
from array import *
arr = array("i",[10,20,30])
print("arr =",arr)
arr.append(40)
arr.append(10)
print("arr = ",arr)

#Buffer info Function
import array 
a=array.array("i",[10,20,30,40])
t = a.buffer_info()
print("t = ",t)
print("ID of array =",id(a))
print("Adress = ",t[0])
print("Number of Elements = ",t[1])

#Count Function
import array as arr
b = arr.array("i",[10,20,10,40,50,20,20])
print("b = ",b)
c = b.count(10)
print("Count =",c)
c = b.count(20)
print("Count =",c)
c = b.count(b[3])
print("Count =",c)
c = b.count(50)
print("Count =",c)
c = b.count(30)
print("Count =",c)

#Extend 
from array import *
arr= array("i",(10,20))
print(arr)
a = array("i",(80,90))
l = [40,50]
t = (30,70)
arr.extend(l)
arr.extend(t)
arr.extend(a)
print("arr = ",arr)

#From list
from array import *
arr = array("i",[10,20])
l = [30,40]
arr.fromlist(l)
print("arr =",arr) 

#tolist 
from array import *
arr = array("i",[10,20,30])
l = arr.tolist()
print("Datatype of l = ",type(l))
print("l = ",l)
print("arr = ",arr)

#del statement
from array import *
arr = array("i",[10,20,30,40,20])
del arr[1]
print("arr = ",arr)
s = [10,20,30,40,50]
del s[2]
print("s = ",s)
