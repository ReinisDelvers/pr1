from random import randrange
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = ""
for i in range(100):
    temp = ""
    lenght = randrange(1,21)
    for b in range(lenght):
        letter = randrange(26)
        temp = temp + alphabet[letter]
    text = text + temp + " "

print(text)
