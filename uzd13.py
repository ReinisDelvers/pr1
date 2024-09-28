import random

def sumwithoutpvn(sum, pvn=21):
    return sum-sum/100*pvn

def pvnvaluefromsum(sum, pvn=21):
    return sum/100*pvn

def surveytextadder(name, hobby, currentschool, favoritesubject, futureprofesion):
    list = []
    list.append(f"Mani sauc {name}.")
    list.append(f"Man patīk {hobby}.")
    list.append(f"Es mācos {currentschool}.")
    list.append(f"Mana mīļākā stunda ir {favoritesubject}.")
    list.append(f"Es nākotnē strādāšu par {futureprofesion}.")
    return list

def eighteenplus(birthyear):
    thisyear = 2024
    if 18<=thisyear-birthyear:
        return 1
    else:
        return 0

def movement(howmanytimes):
    list = []
    for i in range(howmanytimes):
        wasd = input("Input direction wasd: ")
        if wasd == "w":
            list.append("Cilvēciņš dodas uz priekšu")
        elif wasd == "a":
            list.append("Cilvēciņš dodas pa kreisi")
        elif wasd == "s":
            list.append("Cilvēciņš dodas atpakaļ")
        elif wasd == "d":
            list.append("Cilvēciņš dodas pa labi")
        else:
            list.append("KĻūda!")
    return list

def functionrepeaterwithonevariable(function):
    x=1
    y=0
    list = []
    while x==1:
        y = input("Vai vēlies atkārtot šo programmu? y/n vai 1/0: ")
        if y=="y" or y=="1":
            variable = int(input("Input variable: "))
            list.append(function(variable))
        elif y=="n" or y=="0":
            x=0
    return list

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

def dividerfinder(number):
    x=1
    list = []
    while x!=number+1:
        y = number%x
        if y==0:
            list.append(x)
        x+=1
    return list

def numberoflettersfinderinaword(word, letter):
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
        list.append("*"*i)
    return list

def allcombinationsoftwosymbols(symbols):
    list = []
    for i in (symbols):
        for b in (symbols):
            list.append(f"{i}" + f"{b}")
    return list

def twotothepowerofn(number):
    twotothepowerofn = 2
    for i in range(1, number):
        twotothepowerofn *= 2
    return twotothepowerofn

def biggestnumberinalist(list):
    return(max(list))

def listofnumberssquaredtillvariable(num):
    list = []
    for i in range(1, num+1):
        list.append(i*i)
    return list
