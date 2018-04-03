import json
data = json.load(open("data.json"))

def translate(word):
    return data[word]

userInput = 0
while userInput == 0:
    userInput = input("What word would you like to look up?:")
    DataReturn = data[userInput]
    print(translate(userInput))
    userInput = 0
