number = int(input("Ievadi skaitli: "))
x=0
y=0
list = []
while x<number:
    if x%3 == 0 or x%5 == 0:
        list.append(x)
    x += 1

for i in range(len(list)):
    y += list[i]

print(y)