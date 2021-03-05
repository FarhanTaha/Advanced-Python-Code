#Advanced-Python Collection Module Code Part 1

#importing the module(Counter)
from collections import Counter

#(1)Beginning Code
my_counter = "aaaaabbbbccc"
a = Counter(my_counter)#we can see that the number of times a certain letter is we got the count of it.
print(a)

#(2)Looking at the key value pairs
my_counter1 = "aaaaabbbbccc"
b = Counter(my_counter1)
print(b.items())

#(3)Looking at the keys and values separately
my_counter3 = "aaaaabbbbccc"
c = Counter(my_counter)
print(c.keys())#gives us only the keys

my_counter4 = "aaaaabbbbccc"
d = Counter(my_counter)
print(d.values())#gives us only the keys

#(4)Looking at the most common letter in the counter by using their indexes
my_counter5 = "aaaaabbbbbccc"
e = Counter(my_counter)
print(e.most_common(2))#depending on how many common we wanna see we give a number in the parenthesis
print(e.most_common(3)[2])#the value inside the parenthesis means the number of the key it can be ranged to (1-3) as there is only 3 tuples and 3 keys and the value inside the square brackets means to give us the 2nd tuple in index values.
print(e.most_common(2)[1][1])#the value in the second square bracket means the index of the value if we gave 0 it would give us the key , so basically 0 will give key and 1 will give the value, remember the specific tuple and element should be mentioned  firstly int he first parenthesis and square bracket.

#We can use list as an itterable also other itterables
my_counter6 = ['a', 'b', 'c']
f = Counter(my_counter6)
print(f.most_common(3)[2][1])

#Making a list out of our string in counter
my_counter7 = "aaaaabbbbbccc"
g = Counter(my_counter5)
print(list(g.elements()))#we gotta mention elements() as in we want each and every letter in our string to become a info in our list and then apply list function, remember without the element fuction we won't get the duplicate letters as they will appear only once as an info

#without elements
my_counter8 = "aaaaabbbbbccc"
h = Counter(my_counter5)
print(list(g))


#importing the module(namedtuple)
from collections import namedtuple

#Basic Code
#over here we are basically naming our tuples using class
Pnt = namedtuple('Point', 'x,y,u')#over here first mention the variable name and then give the module name then create a class, my class name is Point and put it inside a string inside the parenthesis and then put a comma and then put your argument in a sense of how you want your output to be implemented
clss = Pnt(-2,5,8)#over here use a new variable and then give the above variable inside the parenthesis mention the values you want to put but remember they should in the right sequence of the argument pattern we mentioned
print(clss)

#to remove the names(ex: x,y,z) we can simply use this code
Pnt1 = namedtuple('Point', 'x,y')
clss1 = Pnt1(-2,5)
print(clss1.x, clss1.y)#giving .(the name of the tuple) we have already mentioned the names in out source code so we know the name of the each of the values we have in our tuple so as a result the names won't show now

#END OF PART 1 OF COLLECTIONS MODULE IN ADVANCED-PYTHON!!!
