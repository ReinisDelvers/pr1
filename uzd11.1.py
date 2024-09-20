alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list = []
for i in alphabet:
    list.append(i)
print(list)
for i in list:
    for b in list:
        print(f"{i}{b}")