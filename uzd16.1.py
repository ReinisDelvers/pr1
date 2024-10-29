"Print characters present at an even index number"
str = "PYnative"

for i in range(len(str)):
    if i%2 == 0:
        print(str[i])
    