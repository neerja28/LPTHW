import random
from urllib.request import urlopen
import sys


WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {

"class X(Y)" :" Make a class named X that is-a Y",

"class X(object):def __init__(self, J)" : " class X has-a __init__ that takes a self and J parameters",

"class X(object): def M(self, J)" : "class X has-a M function that takes a self and J parameters",

"foo = X()" : "set foo to an instance of X",

"foo.M(J)" : "From foo get the M function and call it with parameters self and J",

"foo.K = Q" : " from foo get the K attribute and set it to Q"

}

if len(sys.argv) == 2 and sys.argv[1] == 'english':
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding = "utf-8"))

def convert (snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randit(1,3)
        param_names.append(", ".join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        for word in class_names:
            result = result.replace("%%%", word, 1)

        for word in other_names:
            result = result.replace("***", word, 1)

        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results







try:
    while True:
        snippets = list(PHRASES.keys()) # ["class X(Y)","class X(object):def __init__(self, J)" ]
        random.shuffle(snippets)

        for x in snippets:
            phrase = PHRASES[x]
            question, answer = convert(x,phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
                print (question)
                input("> ")
                print (f"Answer {answer}\n\n")

except EOFError:
    print ("Bye")
