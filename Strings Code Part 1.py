#Advanced-Python Strings Code Part 1

#(1)Begining Code:-
print("Hello World")#using double quototaion marks

print('Hello Friends')#using single quotation marks

print(''' 
Hello Universe!
How are you guys?
''')#using 3 quotation marks on each end we can type in several lines of strings

print("""
Hello Universe!
How are you guys?
""")#using 3 double-quotation marks on each end we can type in several lines of strings aswell.

#(2)Giving a quotation mark between Sentences

#There are some ways to do it!

#First Way!
strings = "I'm an Entrepreneur and Software Engineer"
print(strings)

#Second Way!
strings1 = 'I\'m an Entrepreneur and Software Engineer'
print(strings1)

#(3)Making the Sentence in one line though they are in 2 lines in the source code
stg = '''Hello \
People'''#giving a backslash tells our program to keep the code in one line in a string
print(stg)

#(4)Finding particular letters by giving their Index
s = "Hey world"
p = s[2]#we can use whole number and negative numbers only,no decimal
print(p)

#using negative numbers
v = "Hey Man!"
r = v[-2]
print(r)

#(5)Using slice in Strings

#First way!
u = "Hey Universe!"
k = u[1:4]
print(k)

#Second Way!
a = "Hey Universe!"
l = u[:4]
print(l)

#Third Way!
k = "Hey Mars"
t = k[:-2]
print(t)

#Fourth Way!(to skip letters in a string)
g = "Hello venus"
n = g[::2]#2 colons to give to skip the letters and then write the number , if you give 2 it will skip 1 letter but if you write 1 it will not skip any letter
print(n)

#Fifth Way!
q = "Hello neptune"
b = q[::-2]#we can use negative values too
print(b)

#(6)Adding 2 strings to make sentences
greetings = "Hello"
name = "Taha"
j = greetings + " " + name #using a empty string with space in between helps us to use space between our letters or else the words would be together
print(j)

#(7)For Loops in Strings
w = "Hello neptune"
for u in w:
    print(u)

#(8)If statements in Strings
r = "hello everyone"
if "ello" in r:
    print("yes")
else:
    print("no")

#(9)Making our strings full uppercase & Lowercase
Z = "hello everyone"
print(Z.upper())#Upppercase method

h = "HELLO EVERYONE out there"
print(h.lower())#lowercase method

#(10)Removing Wide spaces
G = "    Hello world    "
space = G.strip()#Remember strings are immutable if you still print G you will get the output with the wide spaces,non the less the strip() method helps to remove the wide spaces also remember to use variables to mention the strip() method because you are making a new string without wide spaces.
print(space)

#(11)Checking if what our strings end with and start with are true or false
V = "how to get your first $100 with dropservicing"
print(V.endswith('cing'))#we got true because our sentence end with this leters
print(V.startswith('he'))#we got false as our sentence starts with "ho"

#(12)Finding indexes in our strings
A = "Hello world"
print(A.find('or'))#notice that "or" sequence falls in the index 7 and 8 as "o" comes first it gives index 7 as output

#what if we give wrong finding arg.
T = "Hello world"
print(T.find('oooo'))#we are gonna get "-1" as output if the search we gave has no results, more like an error message

#(13)Counting how many numbers of letters we have in out string
W = "Hello world"
print(W.count('o'))#there are 2 o's in our string so output came 2
#If there is no value that we want to count in the string it will  simply give a 0

#Replacing words in our strings
K = "Hello world"
D = K.replace('world','Tom!')#remember a new string is being created our "K" string is not getting changed
print(D)

#END OF PART 1 OF STRINGS IN ADVANCED-PYTHON!!!