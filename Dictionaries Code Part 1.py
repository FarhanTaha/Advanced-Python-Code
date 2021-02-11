#Advanced-Python Dictonary Code Part 1

#(1)Begining Code:-
mydict = {"name": "Taha", "age": 16, "city": "Dhaka"}#The keys and the values should be sperated with a colon
print(mydict)#code run

#(2)Other way to use dictonary
mydict2 = dict(name="James", age=26, city="New York")#Over here we don't need to put the keys inside of Quotations
print(mydict2)

#(3)Adding new KeyValues in our Dictionary
mydict3 = {"name": "Ana", "age": 32, "city": "Boston"}
mydict3["email"] = "ana@xyz.com"#Remember put the key in square brackets & value out of the brackets specified with a equal
print(mydict3)

#(4)Rewriting or Changing our Values
mydict3 = {"name": "Ana", "age": 32, "city": "Boston", "email": "anawhite@xyz.com"}
mydict3["age"] = 41 #We can change our values by specifying the key inside the square brackets & then write our new value specified with a equal
print(mydict3)

#(5)Removing keyvalues from our Dictionary

#REMEMBER!!! there are several ways to remove keyvalues from our dictionary

#First way!
mydict4 = {"name": "Johnson", "age": 19, "city": "Sydney"}
del mydict4["age"]#Use the del function then put the dictionary variable,after that put the key in square brackets so the key value would get deleted from our dictionary.
print(mydict4)

#Second way!
mydict5= {"name": "John", "age": 15, "city": "Kuala Lampur"}
mydict5.pop("name")#Pop method also removes the key we want to remove
print(mydict5)

#Third way!(Applicable only for python 3.7 and above)
mydict6= {"name": "Tom", "age": 14, "city": "Sylhet"}
mydict6.popitem()#It basically removes the last Key Value in our dictionary
print(mydict6)

#(6)Find Key Values in our Dictionary

#REMEMBER!!! there are several ways to find key values from our dictionary

#First way!
mydict7= {"name": "Tommy", "age": 12, "city": "New Delhi"}
if "name" in mydict7:
    print(mydict7[("name")])
else:
    print("no such keywords")

#Second way!
mydict8 = {"name": "Jimmy", "age": 10, "city": "Melbourne"}
try:
    print(mydict8[("city")])
except:
    print("error")

#Third Way!
mydict9 = {"name": "Jimmy", "age": 10, "city": "Melbourne"}
i = input("Enter the key: ")
if i == "name" in mydict8:
    print("Name:",mydict9[("name")])
elif i == "age" in mydict9:
    print("Age:",mydict9[("age")])
elif i == "city" in mydict9:
    print("City:",mydict9[("city")])
else:
    print("Key not in dictonary.")

#END OF PART 1 OF DICTIONARIES IN ADVANCED-PYTHON!!!
