#Advanced-Python Itertools Module Code Part 2

#importing the module(accumulate)
from itertools import accumulate

a = [1,2,3,4]
acc = accumulate(a)#we can see that how our numbers(data) got added with the product we received by addidng at the very first.
print(list(acc))

#if we want our products to multiply with the input then:(import operator)
#importing the module(operator)
import operator

b = [1,2,3,4]
acc1 = accumulate(b, func=operator.mul)#if we give the function (func) and equal it to operator module with the .mul function our program multiplies the product with the given data and gives us the output.
print(list(acc1))

#we can also check the maximum values and minimum values compared with our product

c = [1,2,5,3,4]
acc2 = accumulate(c, func=max)#compared to the numbers after 5 , 5 in the most bigger number so 5 is the output in a row as 5 is compared wit 3 and 4 after.
print(list(acc2))

d = [1,2,5,3,4]
acc3 = accumulate(c, func=min)#over here 1 ia the smallest product among all the other numbers ahead of it
print(list(acc3))


#importing the module(groupby)
from itertools import groupby
#with groupby we can group our data depending on a parameter.

#Basic Code(with function)
def smaller_than_3(x):
    return x<3
a = [3,1,2,5,4]
group = groupby(a, key=smaller_than_3)
for key, value in group:
    print(key, list(value))

#Intermediate code(with lamda function)
name_age = [{'name': 'Tom','age':12}, {'name':'Jack', 'age':12},
            {'name': 'Tom','age':13}, {'name':'Jack', 'age':15}]
group_2 = groupby(name_age, key=lambda x: x['age'])#we can use the lamda function in place of writing a full function.
for u,z in group_2:
    print(u, list(z))

#Infinite Iterators(count,cycle,repeat)
#importing the module(count,cycle,repeat)
from itertools import count,cycle,repeat

#Using Count
for k in count(10):
    print(k)#(it will go infinite 1 by 1 infinitely to stop it we can add a breaking point with a if statement)
    if k == 15:
        break

#Using cycle
t = [1,2,3]
for h in cycle(t):
    print(h)
    if h == 3:#telling it to stop when it gets 3 or it will continue infinte
       break

#Using Repeat
j = [1,2,3]
for k in repeat(1, 5):#if we dont mention the number of 1 or 2 we want it will continue iterating so to mention it, give a  " , " and then give the number of times you want the specific number in your list to iterate
    print(k)

#END OF PART 2 OF ITERTOOLS MODULE IN ADVANCED-PYTHON!!!