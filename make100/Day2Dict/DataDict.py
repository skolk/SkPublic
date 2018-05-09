import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=.8)) > 0:
        return("Did you mean %s instead") % get_close_matches(word,data.keys())[0]
    else:
       return "This word doesn't exist"

userInput = 0
while userInput == 0:
    userInput = input("What word would you like to look up?:")
    output = translate(userInput)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    userInput = 0
