import json
from difflib import  get_close_matches

data= json.load(open("data.json"))

def meaning(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif w.upper() in data:
        return data[w.upper()]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("did you mean %s if yes press Y if no press N" % get_close_matches(w,data.keys())[0])
        if yn== "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N":
            return "double check your word"
        else:
            return "we dont understand your query"
    else:
        return "check you word"

word = input("enter your word")
output=meaning(word)
if type(output)==list:
    for i in output:
            print(i)
else:
    print(type(output))
    print(output)
