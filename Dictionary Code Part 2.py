#Advanced-Python Dictonary Code Part 2

#(1)Using For loop in dictionaries
mydict = {"name": "Taha", "age": 16, "city": "Dhaka"}
for y in mydict:#this method will only give us the keys in a row
    print(y)

#another method that will give us keys are:-
mydict2 = {"name": "Morris", "age": 17, "city": "Boston"}
for z in mydict2.keys():#.keys() will also give us the keys
    print(z)

#method to get the values
mydict3 = {"name": "Max", "age": 18, "city": "Sydney"}
for a in mydict3.values():#this method will give us the values only
    print(a)

#method to get both values and key
mydict4 = {"name": "Tom", "age": 14, "city": "Belmont"}
for g,b in mydict4.items():#this method will only give us both keys and values
    print(g,b)

#(2)Copying Dictionary
mydict5 = {"name": "Tim", "age": 12, "city": "Bristole"}
mydict_cpy = mydict5#this is the most common way to do it but be careful when your adding a new keyvalue to the copy dictionary the main dictionary will also add the key value to itself as they are specified by equals
print(mydict_cpy)

#another way to copy a dictionary is
mydict6 = {"name": "Ben", "age": 33, "city": "Sylhet"}
mydict_cpy2 = mydict6.copy()#this is one of the best & easy ways to do it as it has noway for the main dictionary to be edited when the copied dictionary is edited
print(mydict_cpy2)

#other way to copy a dictionary is
mydict7 = {"name": "Mary", "age": 11, "city": "Brisbane"}
mydict_cpy3 = dict(mydict7)#same as the last way we saw just over here we are declaring that it is a dictionary
print(mydict_cpy3)

#Updating a dictionary
mydict8 = {"name": "Daisy", "age": 10, 'email':'nial@xyz.com'}
mydict9 = dict(name='Nial', age=21,city="Abu Dhabi")
mydict8.update(mydict9)#all of the keyvalue pairs got over written as they got updated and if any keys don't match it will stay as it is
print(mydict8)

#Using different data types as Key and Values

#Using Int as Key, value is also possible
mydict10 = {8:10,9:11,10:12}#using integers
print(mydict10)

#Using tuples as key, value is also possible
mytuple = (8,10)#Using a tuple as key as it is immutable,remember we cannot use a list as it is mutable or unhashable
my_dict = {mytuple:18}#using the variable to represent the key and then giving the value as int inside of braces specifying it as dictionaries
print(my_dict)

#Using Boolean as value, key is also possible
mybool = True#specifying boolean as True/False
my_dict = {"isred":mybool}
print(my_dict)

#END OF PART 2 OF DICTIONARIES IN ADVANCED-PYTHON!!!