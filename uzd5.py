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
    x = input("Vai vēlies atkārtot šo programmu? y/n vai 1/0: ")
    if y=="y" or x=="1":
        call()
    elif y=="n" or x=="0":
        x=0
