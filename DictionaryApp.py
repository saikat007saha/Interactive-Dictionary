import json
from difflib import get_close_matches

meaning = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in meaning:
        return meaning[word]
    elif word.title() in meaning:
        return meaning[word.title()]
    elif word.upper() in meaning:
        return meaning[word.upper()]
    elif len(get_close_matches(word,meaning.keys())) > 0:
        choice = input("Did you mean \"%s\" instead? Press Y for yes and N for no: " % get_close_matches(word,meaning.keys())[0])
        if choice.lower() == "y":
            return meaning[get_close_matches(word,meaning.keys())[0]]
        elif choice.lower() == "n":
            return "Word doesn't exist. Please double check word."
        else:
            return "Wrong input."
    else:
        return "Word doesn't exist. Please double check word."

word = input("Enter a word: ")

result = translate(word)
if(type(result) == list):
    for i in result:
        print(i)
else:
    print(result)
