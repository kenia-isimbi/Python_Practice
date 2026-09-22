import re

def split_words_and_separators(text: str):
    merged = re.split(r"([ ,]+)", text)
    
    words = merged[::2]

    separators = merged[1::2]
    
    if words and words[0] == "":
        words.pop(0)
    if words and words[-1] == "":
        words.pop()
        
    return words, separators

sample_text = "Python, Exercises,   and   More."
words_list, separators_list = split_words_and_separators(sample_text)

print("Original String:", repr(sample_text))
print("Words List:     ", words_list)
print("Separators List:", separators_list)
