import twl

def get_words(letters: str):
    '''Returns all words that consist only of these letters.'''
    letters = letters.lower()
    words = set(twl.iterator())
    return [word for word in words if set(word).union(set(letters)) == set(letters)]

def filter_words(words, contains: str, starts_with: str, length: int = None) -> list:
    '''
    Accepts a str containing allowed letters, letters to start with and letters that must be contained.
    Optionally, accepts an int of length to filter by length.
    Returns set of words that fit filter criteria.
    If no length provided, all lengths are included.
    '''
    options = []

    for word in words:
        if len(word) >= 4 and contains in word and word.startswith(starts_with):
            options.append(word)

    if length:
        options = [o for o in options if len(o) == length]

    return options