#Different Data Structures in Python
#Mutable vs Immutable
#Sequence vs Non-Sequence
#Iterables

#List in phythan
# mylist =[10,20,30,40,50]
# print("mylist = ",mylist)
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[3])
# print(mylist[4])
# print(mylist[-1])
# print(mylist[-2])
# print(mylist[-3])
# print(mylist[-4])
# print(mylist[-5])
# mutable,sequence
# mylist[2]=80
# print("mylist",mylist)

#Tuple in python
# mytuple =(10,20,30)
# print("mytuple",mytuple)
# print(mytuple[0])
# print(mytuple[1])
# print(mytuple[2])
# print(mytuple[-1])
# print(mytuple[-2])
# print(mytuple[-3])
# immutable,sequence
# mytuple[1]=50
# print("mytuple",mytuple)

#Array in python
# import array as arr
# #import array 
# #from array import *
# a=arr.array("i",[10,20,30])
# print("a=",a)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[-1])
# print(a[-2])
# print(a[-3])
# # mutable,sequence
# a[1]=50
# print("a=",a)

#Dictionary in python
# mydict={"A":10,"B":20,11:30}
# print("mydict=",mydict)
# print(mydict["A"])
# print(mydict["B"])
# print(mydict[11])
# # mutable,non-sequence
# mydict["B"]=50
# print("mydict=",mydict)

#Set in python
# myset={10,20,30,40,50}
# print("myset=",myset)
# #print(myset[0])
# #print(myset[1])
# # mutable,non-sequence
# myset.add(60)
# print("myset=",myset)
# myset.remove(20)
# print("myset=",myset)

#Frozen Set in python
# myfrozenset=frozenset([10,20,30,40,50])
# print("myfrozenset=",myfrozenset)
# #print(myfrozenset[0])
# #print(myfrozenset[1])
# # immutable,non-sequence
# # myfrozenset.add(60)
# # print("myfrozenset=",myfrozenset)
# # myfrozenset.remove(20)
# # print("myfrozenset=",myfrozenset)

#String in python
# mystring="Hello "
# print("mystring=",mystring)
# print(mystring[0])
# print(mystring[1])
# print(mystring[2])
# print(mystring[3])
# print(mystring[4])
# print(mystring[5])
# print(mystring[-1])
# print(mystring[-2])
# print(mystring[-3])
# print(mystring[-4])
# print(mystring[-5])
# print(mystring[-6])
# # immutable,sequence
# # mystring[0]="h"