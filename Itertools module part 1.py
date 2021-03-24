#Advanced-Python Itertools Module Code Part 1

#importing the module(product)
from itertools import product

#Basic Code
a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod))

#using repeat
a = [1,2]
b = [3]
prod = product(a,b, repeat=2)#we see we get different combination of products
print(list(prod))

#importing the module(permutations)
from itertools import permutations
#permutitons allow us to get different orders of a set of data

#Basic code
c = [1,2,3]
permut = permutations(c)
print(list(permut))

#specifying length of our permutation we want
d = [1,2,3]
permuta = permutations(d, 2)#specifying the length of our permutation which is 2
print(list(permuta))

#importing the module(combinations)
from itertools import combinations

#Basic Code
e = [1,2,3,4]
comb = combinations(e, 2)#specifying the length of the combination is mandatory
print(list(comb))

#Getting repetation of the same number
#we have to specify some other function with our module to get the repitation
from itertools import combinations_with_replacement
f = [1,2,3,4]
comb_wr = combinations_with_replacement(f, 2)
print(list(comb_wr))

#END OF PART 1 OF ITERTOOLS MODULE IN ADVANCED-PYTHON!!!