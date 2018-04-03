import json
data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    else:
        return "This word doesn't exist"

userInput = 0
while userInput == 0:
    userInput = input("What word would you like to look up?:")
    print(translate(userInput))
    userInput = 0
