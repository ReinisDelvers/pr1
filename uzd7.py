ievadskaitlis = int(input("Ievadīt skaitli kam gribat atrast dalītājus: "))
x=1
while x!=ievadskaitlis+1:
    y = ievadskaitlis%x
    if y==0:
        print(x)
    x+=1