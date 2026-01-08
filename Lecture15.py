#List Methods
#list append
#It is use to Add elements to the last position of the Liat 
#The element can be value(int,flot) or iterable(array,list,string,dictionary,tuple)
l=[10,20,30]
l.append(40)
print("l=",l)

tup=(1.1,2.2)
l.append(tup)
print("l =",l)

from array import *
arr=array("i",[40,50])
l.append(arr)
print("l=",l)

str="shivani"
l.append(str)
print("l =",l)

#list insert
#It will insert the given element at specified index
l=[10,20,30]
l.insert(2,40)
print("l = ",l)
# The index must be within the range of list
# If the index is positive : it will add the element at the end of the list
l.insert(5,50)
print("l =",l)
# If the index is negative :it will add the element at the starting of the list
l.insert(-8,60)
print("l = ",l)

#list extend
# It will Add all the elements from the given iterable at the end of current list object
# It cannot accept int or float as an argument
l=[10,20]
t=(1.1,2.2,3.3)
l.extend(t)
print("l=",l)

s="SHIVANI"
l.extend(s)
print("l =",l)

dic={"A":10,"B":20}
l.extend(dic)
print("l = ",l)

#list count
# It will count and return total number of occurrences of the given element in the list
l=[10,20,30,40,10.0,10,"10"]
print("l =",l)
x=l.count(10)
print("x = ",x)
x=l.count("10")
print("x = ",x)

#list index
# It will search for the given element in the list 
# If found then it will return the index of its first occurrence 
# If not found then it will case value error
l=[10,20,30,20,40,20.0,60,"20"]
# list_obj.index(element,[start index,[end index]])
x=l.index(20,2)
print("x = ",x)
try:
    l=["SHIVNI","Shivani","shivani"]
    x=l.index("Shivani")
except ValueError:
    print("Not found..")
#end of try
print("x = ",x)


#list sort
# It will the current list in ascending or in descending order.
# To sort a list all the list elements must belong to same or similar data types otherwise it will cause TypeError
l=[30,60,50,10,90,20,40]
l.sort()
print("l = ",l)
l.sort(reverse=True)
print("l = ",l)

l=["shivani","ajay","dipali","ram","pooja"]
l.sort()
print("l = ",l)

#list reverse
# It will simply reverse the contents of the current list (without sorting)
l=[20,50,30,10]
l.reverse()
print("l =",l)

#list pop
# It will delete the last element or element having specified index from the list and return the deleted element
l=[10,20,30,40,50]
x=l.pop(2)
print("l = ",l)
print("Deleted Element =",x)

#list remove
# It will remove the first occurrence specified limit from the list 
# It will not return any value
l=[10,20,30,40,30,50]
l.remove(30)
print("l = ",l)

#list clear
# It will remove all the elements from the list
l=[80,90,40,10]
l.clear()
print("l = ",l)

#list copy
# It will return a copy of the current list 
l1=[10,20,30,40]
l2=l1
print("Id of l1 = ",id(l1))
print("l1 = ",l1)
print("Id of l2 = ",id(l2))
print("l2 = ",l2)
l2.pop()
print("l1 = ",l1)
print("l2 = ",l2)
# (l2=l1) not making copy of l1 list 
# It only refer one list two name

# With the help of copy we can make a copy of list 
l1=[10,20,30,40]
l2=l1.copy()
print("Id of l1 = ",id(l1))
print("l1 = ",l1)
print("Id of l2 = ",id(l2))
print("l2 = ",l2)
l2.pop()
print("l1 = ",l1)
print("l2 = ",l2)
