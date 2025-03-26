from random import randrange
input = input("Heads or Tails: ")
x = randrange(2)
if x==0:
    if input=="Tails":
        print("Coin landed tails you won")
    else:
        print("Coin landed tails you lost")
else:
    if input=="Heads":
        print("Coin landed heads you won")
    else:
        print("Coin landed heads you lost")
