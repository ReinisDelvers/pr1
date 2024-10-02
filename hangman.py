import random
hangmanpictures = [
"""
   +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========
""","""
   +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========
""","""
   +---+
    |   |
    O   |
   /|\  |
        |
        |
=========
""","""
   +---+
    |   |
    O   |
   /|   |
        |
        |
=========
""","""
   +---+
    |   |
    O   |
   /    |
        |
        |
=========
""","""
   +---+
    |   |
    O   |
        |
        |
        |
=========
""","""
   +---+
    |   |
        |
        |
        |
        |
=========
"""]

words = ["apple", "boat", "cloud", "dance", "electric", "garden", "happiness", "island", "journey", "kitten", 
         "laughter", "mountain", "orange", "puzzle", "question", "rainbow", "science", "tiger", "umbrella", 
         "voice", "water", "xylophone", "yogurt", "zebra", "bread", "chocolate", "discovery", "energy", 
         "flower", "gift", "home", "ice", "joy", "key", "light", "memory", "night", "ocean", "pencil", 
         "quiet", "river", "star", "time", "universe", "vacation", "wind", "x-ray", "youth", "zip", 
         "adventure", "balance", "creativity", "destiny", "explore", "freedom", "gratitude", "happiness", 
         "inspiration", "kindness", "love", "music", "nature", "optimism", "peace", "quest", "respect", 
         "serenity", "travel", "unity", "vision", "wonder", "ambition", "bravery", "confidence", 
         "determination", "empathy", "friendship", "growth", "hope", "intelligence", "joyfulness", 
         "knowledge", "loyalty", "mindfulness", "novelty", "openness", "resilience", "strength", 
         "teamwork", "understanding", "vitality", "wisdom", "zest", "achievement", "beauty", 
         "curiosity", "dedication", "excellence", "fun", "generosity"]

x=1
y=0
t=1

while x==1:
    y = input("Do you want to play hangman yes/no: ")
    if y=="yes":
        m = input("Do you want a random word input r or if you want a selected word input s: ")
        if m == "r":
            selectedword = words.random
        selectedword = words[int(input("Select word by choosing a number 0-99: "))]
        while t==1:
            remainingattempts = 6
            if remainingattempts > 0:
                guessedletter = input("Guess a letter: ")
                guessedletterlist = []
                guessedletterlist += guessedletter

                print(hangmanpictures[remainingattempts])
                print(f"Remaining attempts {remainingattempts}")

            elif remainingattempts == 0:
                print(hangmanpictures[remainingattempts])
                print(f"Remaining attempts {remainingattempts}")
                print("Game over")
                t=0
    elif y=="no":
        x=0