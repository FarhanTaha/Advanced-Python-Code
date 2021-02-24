#Advanced-Python Strings Code Part 2

#(1)Making a string into a list
my_string = "How are you?"
a = my_string.split()#The split() function makes our string into a list by putting a comma in every space it finds.
print(a)

#Let's see more possibilities of it

#First way!
my_string2 = "Howareyou?"
b = my_string2.split()#Now we will have it inside of a list but as only one value.
print(b)

#Second way!
my_string3 = "How,are,you?"#This time inserting commas between the letters of our string
c = my_string3.split(",")#If there are commas in our list we should use a string comma as an arg. in order to split them and make a list
print(c)

#(2)Joining strings

#First way!(to make a list in to a string)
my_list = ['How', 'are', 'you?']
print(''.join(my_list))#You can see because we gave no space between our two quotation, so thats why the letters are joined in with out spaces, to join them in give a space in between the quotation marks

#Checking with space
my_list = ['How', 'are', 'you?']
print(' '.join(my_list))#space applied

#Using joint to join many letters together
d = ['a'] * 5
print(''.join(d))

#(3)F-strings
name = "Taha"
age = 14
print(f'Hey my name is {name} and my age is {age}')#we gotta use a "f" inside print and before we start the string and then use curly brackets to input our variables

#we can also multiply or divide or add or sub in side the curly braces but only if the variable contains integers but multiply can be used with both strings and numbers
name = "Tom"
age = 15
no_books = 5
no_servants = 6
print(f'Hey my name is {name * 2} and my age is {age+2}, I read {no_books-2} books a month and I have {no_servants//2} in my house.')#We gave double divide sign for no decimals

#(4) % in strings
var1 = "Tom"
e = "The variable is %s" % var1 #More like F-strings , as our variable is a string thats why we had to give a "s" after "%" inside the quotation marks.
print(e)

#If our variable was a integer
var2 = 3
f = "The variable is %d" % var2 # "d" has to be given when the variable is a integer but lemme tell you this will not take decimal values.
print(f)

#To get decimal values in output aswell
var3 = 3.1234589
f = "The variable is %f" % var3 #to make the decimal values we gotta use "f" which stands for float
print(f)

#If we want to take a specific number of decimal places we can do that
var4 = 3.1234589
g = "The variable is %.2f" % var4 #giving .2 after % tells our program how many decimals to take.
print(g)

#(5)Using format() in strings
var5 = 3.1234589
var6 = "Tom"
h = 'The variable is {}.I am beast {}.'.format(var5,var6)#we gotta give curly braces inside our string to tell the program where we wanna put out variable values and then outside the string give .format() without the space and inside the brackets of .format() give the variable we wanna use as arg,also we can use as many arg we want to but they should be in order as we have inputed in our string .
print(h)

#How to give a specific decimal place using format
var7 = 3.1234589
i = 'The variable is {:.3f}'.format(var7)#we have to give a colon as a slic to indicate how many decimal we wanna take
print(i)

#Using strings not integers in format variable
var8 = 'Hello WORLD'
j = 'The variable is {}'.format(var8)
print(j)

#END OF PART 2 OF STRINGS IN ADVANCED-PYTHON!!!