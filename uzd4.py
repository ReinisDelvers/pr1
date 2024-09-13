for i in range(4):
    wasd = input("Ievadīt kustības virzienu w,a,s,d: ")
    if wasd == "w":
        print("Cilvēciņš dodas uz priekšu")
    elif wasd == "a":
        print("Cilvēciņš dodas pa kreisi")
    elif wasd == "s":
        print("Cilvēciņš dodas atpakaļ")
    elif wasd == "d":
        print("Cilvēciņš dodas pa labi")
    else:
        print("KĻūda!")
