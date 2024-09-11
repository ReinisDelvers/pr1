import random
minejums = int(input("Uzmini paslēpto skaitli: "))
pasleptaissakitlis = random.randrange(1, 11)
x=1
while x==1:
    if pasleptaissakitlis == minejums:
        print("Tu uzminēji")
        x=0
    elif pasleptaissakitlis > minejums:
        print("Lielāks")
        minejums = int(input("Uzmini paslēpto skaitli: "))
    elif pasleptaissakitlis < minejums:
        print("Mazāks")
        minejums = int(input("Uzmini paslēpto skaitli: "))