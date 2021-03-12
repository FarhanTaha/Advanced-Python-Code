#Advanced-Python Collection Module Code Part 2

#importing the module(OrderedDict)
from collections import OrderedDict#this module helps us to order our dictionary, this is a old model,as the new built in dictionary in above python 3.7 already has this feature.

ordered_dict = OrderedDict()#initializing the code, we can also initialize the code by using this code:-ordered_dict = {}
ordered_dict['a'] = 'apple'
ordered_dict['b'] = 'banana'
ordered_dict[1] = 100
print(ordered_dict)


#importing the module(defaultdict)
from collections import defaultdict#it works almost similar to OrderedDict,just the difference we can set arguments and we can use it to understand if we are searching for wrong key without crashing our program

#Begining Code
d = defaultdict(int)#initializing code,we also have to mention what will be our the datatype of our values
d['c'] = 8
d[9] = 900
print(d)

#Finding the values by typing only the keys
d = defaultdict(int)
d['c'] = 8
d[9] = 900
print(d[9])

#If we give a wrong key then we get "0" if we use int as an arg,if we use str as arg then we get no output, if we give float we get "0.0",if we give a list we get a empty list as output
d = defaultdict(str)#we can use float and str and list here
d['c'] = 'yo'
d[9] = "man"
print(d['b'])

#importing the module(deque)
from collections import deque#we can simply modify our dictionary using this module, also we can make such a dict that will have no keyvalue pairs

j = deque()#initializing the module

j.append('a')#adding elements
j.append('b')
j.append('c')
j.remove('b')#removing elements
j.appendleft('d')#this function will help us to append this from the first or we can say left even if we inputted the code at the very first
j.appendleft('e')
print(j)

j.pop()#this will remove the last element on the right from our dictionary
print(j)

j.popleft()#this will remove the first element or the very left element on our dictionary
print(j)

j.extend([4, 5, 6])#when we want append a lot of elements together we can use the extend function as it takes more than one argument when we put a square bracket on both side of the elements.
print(j)

j.extendleft(['i', 't', 'k'])#now this will add all this elements to the very first of our dict,also we can see that the last element inside the extendleft function is at the very left
print(j)

j.rotate(2)#depending on what the number we give as argument, the more will our elements will rotate,as we see every letter went forward by 2 places and rotates
print(j)

j.rotate(-1)#we can rotate it from the left by using negative numbers
print(j)

j.reverse()#this will reverse the whole dict at once, more like before it was in assending order and now its in desending.
print(j)

copied_dict = j.copy()#we can copy our dict with this method so if we modify this dict further the before dict won't be harmed
print(copied_dict)

j.clear()#erasing all the data from the dict
print(j)

print(copied_dict)#we can see even though we erase all the data from the before dict we still have a copy of it in our copied_dict variable

count_option_variable = copied_dict.count("d")#this function helps us to know if there is element that has been written twice or more than that or how many times one element has been written.
print(count_option_variable)

copied_dict.insert(1,'w')#using the insert function we can replace the elements on the specific index we specified with the element we want to replace it.
print(copied_dict)

a = copied_dict.index('a',1,7)#this code can be said as, return the index of a if a fall between the index 1 to 7,if we try to find for a element that is not between the index we gave or we search for a element that is not their we get ta error.
print(a)

#END OF PART 2 OF COLLECTIONS MODULE IN ADVANCED-PYTHON!!!