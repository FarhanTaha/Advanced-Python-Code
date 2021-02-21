#Advanced-Python SETS Part 1

#(1)Begining Code
myset = {1,2,3}#the functions of set is similar to dictionary but a set doesn't require a keyvalue pair
print(myset)

#(2)Using Duplicate Data in Sets
myset2 = {4,5,6,4,5}#the duplicate data did not get writen because a set does not allow duplicate data
print(myset2)

#(3)Differentiating between a set and a dictionary
myset3= {}
print(type(myset3))#You can see we got <class 'dict'> as output, to make a empty set we will be needing to do this:-

myset4 = set()
print(type(myset4))#Now you can see we got <class 'set'> as output

#(4)Adding Data to our set
myset5 = {5,6,8}
myset5.add(9)#remember add() function can only hold 1 argument
myset5.add(10)#we can add like this as much as we want
print(myset5)

#(5)Removing Data from our set

#Remember there are several ways to remove data from our set

#First way
myset6 = {1,2,3,4}
myset6.remove(4)#the fuction remove() helps us to remove the data we want to remove in our sets
print(myset6)

#Second Way
myset7 = {5,6,7,8}
myset7.discard(6)##the fuction discard() helps us to remove the data we want to remove in our sets
print(myset7)

#Third Way
myset9 = {9,10,11,12,8}
myset9.pop()#pop() function works different in sets, as it dosen't delete the last element in our set but the lowest value in our sett.
print(myset9)

#Fourth Way(to erase all the elements from out set)
myset10 = {9,10,11,12,8}
myset10.clear()#removes all the element from our list
print(myset10)

#(6)Using for loop in our set
myset11 = {9,10,11,12,8}
for x in myset11:
    print(x)

#(7)Using if statements in our set
myset12 = {9,10,11,12,8}
if 10 in myset12:
    print("yes")#remember the program will still run even if you don't specify a else or elif function.
else:
    print("No")
#(8)Working with Union in sets
even = {2,4,6,8,10}#set of even numbers
odd = {11,13,15,17,19}#set of odd numbers
prime= {2,3,5,7,11}#set of prime numbers
i = even.union(odd)#this means all the values in set even and odd to be outputted
print(i)

#(9)Working with intersections in sets
evens = {2,4,6,8,10}#set of even numbers
odds = {11,13,15,17,19}#set of odd numbers
primes = {2,3,5,7,11}#set of prime numbers
u = evens.intersection(primes)#the output is 2 as the only common element between even and prime numbers are 2
print(u)

#what if there was no common element between 2 sets,what would be the output?
even1 = {2,4,6,8,10}#set of even numbers
odd1 = {13,15,17,19}#set of odd numbers
prime1 = {2,3,5,7,11}#set of prime numbers
a = odd1.intersection(primes)#AS you can see from the output we got a empty set
print(a)

#(10)Difference between two sets
setA = {1,2,3,4,5,6}
setB = {7,8,9,1,2,3}
difference1 = setA.difference(setB)#Over here the code means setA is different from setB because it has the elements (4,5,6)
print(difference1)

#IF we now exchange the diffence to how setB is different from setA,we would get:-
setA = {1,2,3,4,5,6}
setB = {7,8,9,1,2,3}
differences = setB.difference(setA)##Over here the code means setB is different from setA because it has the elements (8, 9, 7)
print(differences)

#END OF PART 1 OF SETS IN ADVANCED-PYTHON!!!
