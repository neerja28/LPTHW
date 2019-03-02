def break_words(stuff):
    """This function will break stuff for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """This function will sort words for us"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print (word)

def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1)
    print (word)

def sort_sentence(sentence):
    words  = break_words(sentence)
    return sort_words(words)

def print_first_and_last_sentence(sentence):
    """Prints the first and the last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_words(sentence):
    """Sorts the words and prints the first and last words"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
