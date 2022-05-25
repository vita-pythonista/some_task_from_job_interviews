import string

punctuation = string.punctuation


def is_pangram(frase: str) -> bool:
    if frase is False:
        return False
    set_unique = set(frase.lower())
    for symbol in set_unique:
        if symbol not in punctuation:
            if frase.count(symbol) == 1:
                return True
            else:
                return False
