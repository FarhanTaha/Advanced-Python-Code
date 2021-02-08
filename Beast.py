# Function naming and putting in parameters
def cmn(name,age):
    name = input("Enter in your name: ") #fidding knowledge to the parameter,we are just saying the name is going to be what will be inputed....
    age = input("Enter in your age: ")   #fidding knowledge to the parameter,we are just saying the age is going to be what will be inputed....
    if name == "Munni" or name == "Dr.Farhana Faruque" or name == "Dr.Farhana Faruque Munni" or name == "Farhana Faruque Munni" or name == "Dr.Farhana" or name == "Farhana" and age == "38" or age == "37" or age == "39":
        print(f'Hello {name}. You are {age}, and you are the Best Mother,and your children loves you a lot.')  # Message that needs to be given.
    elif name == "Farhan Mubasshir Taha" and  age == "16":
        print(f'Hello {name}. You are {age}, and you are a great Motivational Speaker, Software Engineer, Entrepreneur and Debater.')
    elif name == "Mashrafi Bin Salahuddin Tabith" or name == "Tabith" and age == "6" or age == "5":
        print(f'Hello {name}. You are {age},You can cycle and do Fakibaji. but you are a very good human being and good son and brother.')
    elif name == "Md.Salahuddin Miah Likhon" or name == "Salahuddin Miah Likhon" or name == "Likhon" and age == "48" or age == "47" or age == "49":
        print(f'Hello {name}. You are {age}, You are a very good person and a very good father and husband')
    else:
        print("Human being not in List.")
cmn("","") #initializing the Function



