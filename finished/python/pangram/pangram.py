def is_pangram(sentence: str):
    letters = [letter for letter in sentence.lower() if letter.isalpha()]
    return len(set(letters)) == 26
