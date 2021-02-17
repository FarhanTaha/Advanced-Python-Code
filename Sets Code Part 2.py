#Advanced-Python Dictonary SETS Part 2

#(1)Finding differences between both set
setA = {1,2,3,4}
setB = {1,2,5,6}
a = setA.symmetric_difference(setB)#Note that this will show the differences in both element in other words it will skip the intersection elements and show all the other elements in the 2 sets
print(a)

#(2)Updating our set

#Remember!! There are several ways to do it

#First way!
setC = {1,2,3,4}
setD = {1,2,5,6}
setC.update(setD)#This will give us all the elements from the both sets without repeating the same elements in the both sets also we just got new elements for setA by updating it
print(setC)

#Second way!
setE = {1,2,3,4}
setF = {1,2,5,6}
setE.intersection_update(setF)#this means update my setE by keeping all the elements between the both sets
print(setE)

#Third way!
setG = {1,2,3,4}
setH = {1,2,5,6}
setG.difference_update(setH)#this updates SetG by only keeping the values different from setH and removing the same elements in both sets
print(setG)

#Fourth Way!
setK = {1,2,5,6}
setJ= {1,2,3,4}
setK.symmetric_difference_update(setJ)#This will update SetK by putting the different elements in both sets in SetK
print(setK)

#(3)Using "is" statements in our sets
#Using subset
set1 = {1,2,3,4}
set2 = {1,2}
b = set1.issubset(set2)#The output is False because set1 have more different elements in it than set2
print(b)

#If we reverse the process
set3 = {1,2,3,4}
set4 = {1,2}
a = set4.issubset(set3)#The output is True because set4 has all the elements in it that set3 has
print(a)

#Using superset
seti = {1,2,3,4}
setk = {1,2}
a = seti.issuperset(setk)#Its output is True because not only it has the same element as setk but has different elements too
print(a)


#Using disjoint
set5 = {1,2,3,4}
set6 = {1,2}
y = set5.isdisjoint(set6)#the output will be False as there is same elements in both set,but if we do it with no same elements in both set we get True,so lets try it out
print(y)

#If we reverse the process
set7 = {1,2,3,4}
set8 = {7,8}
o = set7.isdisjoint(set8)#now the output will be True as there is no similarities between 2 sets
print(o)

#(4)Copying a set

#copying a set is mostly like copying a list

#There are many ways to do it!

#First way!
set_1 = {1,2,3,4}
set_2 = set_1#this will copy the elements of set_1 and use it in set_2 too,but be careful if you add something to set_2 then,set_1 will also be updated with that new update setted in set_2,this can be done in a better way
print(set_2)

#Second way!
set_3 = {1,2,3,4}
set_4 = set_3.copy()#and now its a pure copy so even if we add anything to either of the sets it will also not get updatted in both sets
print(set_4)

#Third way!
set_5 = {1,2,3,4}
set_6 = set(set_3)#it is a pure copy aswell
print(set_6)

#Using frozen set METHOD!(the only method to make a set immutable)
set_t = frozenset([1,2,3,4])#We gotta use a itterable such as list as an argument here as it can't take more than one argument
print(set_t)#note that, it cannot be modified

#Proof that it cannot be modified is:-
try:
    set_t = frozenset([1, 2, 3, 4])
    set_t.add(5)#you can see we can't add as we get an attribute error
    set_t.remove(1)
    print(set_t)
except:
    print("error")


#END OF PART 2 OF SETS IN ADVANCED-PYTHON!!!