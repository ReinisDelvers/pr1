import random

def sumwithoutpvn(sum, pvn=21):
    return sum-sum/100*pvn

def pvnvaluefromsum(sum, pvn=21):
    sum/100*pvn

def surveytextadder(name, hobby, currentschool, favoritesubject, futureprofesion):
    list = []
    list.append(f"Mani sauc {name}.")
    list.append(f"Man patīk {hobby}.")
    list.append(f"Es mācos {currentschool}.")
    list.append(f"Mana mīļākā stunda ir {favoritesubject}.")
    list.append(f"Es nākotnē strādāšu par {futureprofesion}.")
    return list

def eighteenplus():
    sisgads = 2024
    dzimsanasgads = int(input("Ievadi dzimšanas gadu: :"))
    if 18<=sisgads-dzimsanasgads:
        print("Ir vairāk par 18 gadiem")
    else:
        print("Ir mazāk par 18 gadiem")

def movement(wasd1, wasd2, wasd3, wasd4):
    if wasd1 == "w":
        print("Cilvēciņš dodas uz priekšu")
    elif wasd1 == "a":
        print("Cilvēciņš dodas pa kreisi")
    elif wasd1 == "s":
        print("Cilvēciņš dodas atpakaļ")
    elif wasd1 == "d":
        print("Cilvēciņš dodas pa labi")
    else:
        print("KĻūda!")
    if wasd2 == "w":
        print("Cilvēciņš dodas uz priekšu")
    elif wasd2 == "a":
        print("Cilvēciņš dodas pa kreisi")
    elif wasd2 == "s":
        print("Cilvēciņš dodas atpakaļ")
    elif wasd2 == "d":
        print("Cilvēciņš dodas pa labi")
    else:
        print("KĻūda!")
    if wasd3 == "w":
        print("Cilvēciņš dodas uz priekšu")
    elif wasd3 == "a":
        print("Cilvēciņš dodas pa kreisi")
    elif wasd3 == "s":
        print("Cilvēciņš dodas atpakaļ")
    elif wasd3 == "d":
        print("Cilvēciņš dodas pa labi")
    else:
        print("KĻūda!")
    if wasd4 == "w":
        print("Cilvēciņš dodas uz priekšu")
    elif wasd4 == "a":
        print("Cilvēciņš dodas pa kreisi")
    elif wasd4 == "s":
        print("Cilvēciņš dodas atpakaļ")
    elif wasd4 == "d":
        print("Cilvēciņš dodas pa labi")
    else:
        print("KĻūda!")

def functionrepeatingbasedoninput(function):
    x=1
    while x==1:
        y = input("Vai vēlies atkārtot šo programmu? y/n vai 1/0: ")
        if y=="y" or y=="1":
            function
            print("asdf")
        elif y=="n" or y=="0":
            print("asdf")
            x=0

def guesthenumber():
    pasleptaissakitlis = random.randrange(1, 11)
    minejums = int(input("Uzmini paslēpto skaitli: "))
    pasleptaissakitlis = random.randrange(1, 11)
    x=1
    while x==1:
        if pasleptaissakitlis == minejums:
            x=0
        elif pasleptaissakitlis > minejums:
            print("Lielāks")
            minejums = int(input("Uzmini paslēpto skaitli: "))
        elif pasleptaissakitlis < minejums:
            print("Mazāks")
            minejums = int(input("Uzmini paslēpto skaitli: "))

    return pasleptaissakitlis
print(guesthenumber())

def dividerfinder(number):
    x=1
    list = []
    while x!=number+1:
        y = number%x
        if y==0:
            list.append(x)
        x+=1
    return list

def numberletterfinderinaword(word, letter):
    y=0
    for i in word:
        if i == letter:
            y += 1
    return(y)

def sumofnumberwhhichcividesbr3or5(number):
    x=0
    y=0
    list = []
    while x<number:
        if x%3 == 0 or x%5 == 0:
            list.append(x)
        x += 1

    for i in range(len(list)):
        y += list[i]

    return y

def sumofevenfibonaccinumberstillmaxnumber(maxnumber):
    x=0
    y=0
    r=0
    a=1
    b=2
    list = [1,2]

    while y<1:
        if a<b:
            a += b
            x=a
            list.append(x)
            if maxnumber<x:
                y=1
                a = a - b
            
        elif b<a:
            b += a
            x=b
            list.append(x)
            if maxnumber<x:
                y=1
                b = b - a
        
    for i in range(len(list)):
        if list[i]%2 == 0:
            r += list[i]
    return r

def starprinter(number):
    list = []
    for i in range(1, number+1):
        6
        list.append("*"*i)
    return list

def allcombinationsoftwosymbols(symbols):
    list = []
    list2 = []
    for i in symbols:
        list.append(i)

    for i in list:
        for b in list:
            list2.append(f"{i}{b}")
    return list2


def twotothepowerofn(number):
    twotothepowerofn = 2
    for i in range(1, number):
        twotothepowerofn *= 2
    return twotothepowerofn

