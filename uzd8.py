name = input("Ievadi vārdu: ")
x=0
y=0
letter = input("Ievadi vienu burtu: ")
while x<1:
    if len(letter) == 1:
        x=1
    else:
        letter = input("Ievadi vienu burtu: ")

for i in name:
    if i == letter:
        y += 1

print(f"Vārdā {name} ir {y} burtu")



