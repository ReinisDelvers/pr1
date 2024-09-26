def call(): 
    summa = int(input("Ievadi summu: "))
    pvn = 21
    summabezpvn = summa-summa/100*pvn
    pvnvertiba = summa/100*pvn
    print(summabezpvn)
    print(pvnvertiba)

x=1
y=0
while x==1:
    y = input("Vai vēlies atkārtot šo programmu? y/n vai 1/0: ")
    if y=="y" or y=="1":
        call()
        print("asdf")
    elif y=="n" or y=="0":
        print("asdf")
        x=0
        
