maxnumber = int(input("Ievadi ciparu: "))

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


    


print(a)
print(b)
print(list)
print(r)