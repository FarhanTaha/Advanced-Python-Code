#while Loops and Try and except methods are given 
#so that we can track and again loop if value-error
#is found rather than breaking the program
while True:
    number_1stt = input("Enter the first number: ")
    try:
        float(number_1stt)
    except ValueError:
        print("this is not a number.")
        continue
    number_1stt_int = float(number_1stt)
    break

while True:
    constant_1st_str = input("Enter the constant with the first number: ")
    if constant_1st_str.isalpha():
        break
    else:
        print("This is not a constant")
    continue

while True:
    number_2ndd = input("Enter the second number: ")
    try:
        float(number_2ndd)
    except ValueError:
        print("this is not a number.")
        continue
    number_2ndd_int = float(number_2ndd)
    break

while True:
    constant_2ndd_str = input("Enter the constant with the second number: ")
    if constant_2ndd_str.isalpha():
        break
    else:
        print("This is not a  constant")
    continue

#this is to multiply the two integers
xx = number_1stt_int * number_2ndd_int

#making the answer of the two integers into a string
#because you cannot add a string and int/float in a variable
ii = str(xx)

#if/elif/else statements so that we can square two constants 
#if they are same and multiply if not same
if constant_1st_str == "a" and constant_2ndd_str == "a":
    a_square = "a^2"
    print(ii+a_square)
elif constant_1st_str == "b" and constant_2ndd_str == "b":
    b_square = "b^2"
    print(ii+b_square)
elif constant_1st_str == "c" and constant_2ndd_str == "c":
    c_square = "c^2"
    print(ii+c_square)
elif constant_1st_str == "d" and constant_2ndd_str == "d":
    d_square = "d^2"
    print(ii+d_square)
elif constant_1st_str == "e" and constant_2ndd_str == "e":
    e_square = "e^2"
    print(ii+e_square)
elif constant_1st_str == "f" and constant_2ndd_str == "f":
    f_square = "f^2"
    print(ii+f_square)
elif constant_1st_str == "g" and constant_2ndd_str == "g":
    g_square = "g^2"
    print(ii+g_square)
elif constant_1st_str == "h" and constant_2ndd_str == "h":
    h_square = "h^2"
    print(ii+h_square)
elif constant_1st_str == "i" and constant_2ndd_str == "i":
    i_square = "i^2"
    print(ii+i_square)
elif constant_1st_str == "j" and constant_2ndd_str == "j":
    j_square = "j^2"
    print(ii+j_square)
elif constant_1st_str == "k" and constant_2ndd_str == "k":
    k_square = "k^2"
    print(ii+k_square)
elif constant_1st_str == "l" and constant_2ndd_str == "l":
    l_square = "l^2"
    print(ii+l_square)
elif constant_1st_str == "m" and constant_2ndd_str == "m":
    m_square = "m^2"
    print(ii+m_square)
elif constant_1st_str == "n" and constant_2ndd_str == "n":
    n_square = "n^2"
    print(ii+n_square)
elif constant_1st_str == "o" and constant_2ndd_str == "o":
    o_square = "o^2"
    print(ii+o_square)
elif constant_1st_str == "p" and constant_2ndd_str == "p":
    p_square = "p^2"
    print(ii+p_square)
elif constant_1st_str == "q" and constant_2ndd_str == "q":
    q_square = "q^2"
    print(ii+q_square)
elif constant_1st_str == "r" and constant_2ndd_str == "r":
    r_square = "r^2"
    print(ii+r_square)
elif constant_1st_str == "s" and constant_2ndd_str == "s":
    s_square = "s^2"
    print(ii+s_square)
elif constant_1st_str == "t" and constant_2ndd_str == "t":
    t_square = "t^2"
    print(ii+t_square)
elif constant_1st_str == "u" and constant_2ndd_str == "u":
    u_square = "u^2"
    print(ii+u_square)
elif constant_1st_str == "v" and constant_2ndd_str == "v":
    v_square = "v^2"
    print(ii+v_square)
elif constant_1st_str == "w" and constant_2ndd_str == "w":
    w_square = "w^2"
    print(ii+w_square)
elif constant_1st_str == "x" and constant_2ndd_str == "x":
    x_square = "x^2"
    print(ii+x_square)
elif constant_1st_str == "y" and constant_2ndd_str == "y":
    y_square = "y^2"
    print(ii+y_square)
elif constant_1st_str == "z" and constant_2ndd_str == "z":
    z_square = "z^2"
    print(ii+z_square)

#multiplying the constants if they are not same
#starting with if the first constant is "a":
elif constant_1st_str ==  "a" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)    
elif constant_1st_str ==  "a" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "a" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "b":
elif constant_1st_str ==  "b" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)    
elif constant_1st_str ==  "b" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "b" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "c":
elif constant_1st_str ==  "c" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)    
elif constant_1st_str ==  "c" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "c" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "d":
elif constant_1st_str ==  "d" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)    
elif constant_1st_str ==  "d" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "d" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "e":
elif constant_1st_str ==  "e" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)    
elif constant_1st_str ==  "e" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "e" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "f":
elif constant_1st_str ==  "f" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)    
elif constant_1st_str ==  "f" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "f" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "g":
elif constant_1st_str ==  "g" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)    
elif constant_1st_str ==  "g" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "g" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "h":
elif constant_1st_str ==  "h" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)    
elif constant_1st_str ==  "h" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "h" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "i":
elif constant_1st_str ==  "i" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)    
elif constant_1st_str ==  "i" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "i" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "j":
elif constant_1st_str ==  "j" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)    
elif constant_1st_str ==  "j" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "j" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "k":
elif constant_1st_str ==  "k" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)    
elif constant_1st_str ==  "k" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "k" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "l":
elif constant_1st_str ==  "l" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)    
elif constant_1st_str ==  "l" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "l" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "m":
elif constant_1st_str ==  "m" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)    
elif constant_1st_str ==  "m" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "m" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "n":
elif constant_1st_str ==  "n" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)    
elif constant_1st_str ==  "n" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "n" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "o":
elif constant_1st_str ==  "o" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)    
elif constant_1st_str ==  "o" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "o" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "p":
elif constant_1st_str ==  "p" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)    
elif constant_1st_str ==  "p" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "p" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "q":
elif constant_1st_str ==  "q" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)    
elif constant_1st_str ==  "q" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "q" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "r":
elif constant_1st_str ==  "r" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)   
elif constant_1st_str ==  "r" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "r" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "s":
elif constant_1st_str ==  "s" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)   
elif constant_1st_str ==  "s" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "s" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)


#if the first constant is "t":
elif constant_1st_str ==  "t" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)   
elif constant_1st_str ==  "t" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "t" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)


#if the first constant is "u":
elif constant_1st_str ==  "u" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)   
elif constant_1st_str ==  "u" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "u" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "v":
elif constant_1st_str ==  "v" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)   
elif constant_1st_str ==  "v" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "v" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "w":
elif constant_1st_str ==  "w" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)   
elif constant_1st_str ==  "w" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "w" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "x":
elif constant_1st_str ==  "x" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)   
elif constant_1st_str ==  "x" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "x" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "y":
elif constant_1st_str ==  "y" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)   
elif constant_1st_str ==  "y" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "y" and constant_2ndd_str == "z":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)

#if the first constant is "z":
elif constant_1st_str ==  "z" and constant_2ndd_str == "a":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "b":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "c":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "d":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "e":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "f":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "g":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "h":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "i":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "j":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "k":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "l":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "m":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "n":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "o":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "p":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "q":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "r":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "s":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "t":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "u":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "v":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "w":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)   
elif constant_1st_str ==  "z" and constant_2ndd_str == "x":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
elif constant_1st_str ==  "z" and constant_2ndd_str == "y":
    adding_them = constant_1st_str + constant_2ndd_str
    print(ii+adding_them)
#if none of the constants match then this message is given.
else:
    print("Please Input your values and constants again.")
    print("*Remember there can't be more than one constant\nwith one number")
    print("constants should be small letter, no capital\nletter accepted.")
    