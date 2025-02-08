text = input("Write a sentence: ")
list = []
listreverse = []
 
list = text.split()

with open("10builtin.txt", "w") as f:
    f.write("")

for i in range(len(list)):
    listreverse.append(list[-i-1])
    with open("10builtin.txt", "a") as f:
        f.write(str(listreverse[i] + " " + list[i] + " "))

print(list)
print(listreverse)
print("====================")
with open("10builtin.txt", "r") as f:
    print(f.read())