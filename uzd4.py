def call(): 
    summa = int(input("Ievadi summu: "))
    pvn = 21
    summabezpvn = summa-summa/100*pvn
    pvnvertiba = summa/100*pvn
    print(summabezpvn)
    print(pvnvertiba)
call()
x=1
while x==4121:
    x = input("Vai vēlies atkārtot šo programmu? y/n vai 1/0: ")
    if x=="y" or x=="1":
        call()
    elif x=="n" or x=="0":
        x=0
