import string
import os
from math import log
import matplotlib.pyplot as plot
from english_distribution import en_frequency


def n_gram_histogram(char_array: list, n_gram: int = 3, occurrence: int = 3, plot_hist: bool = False) -> dict:
    n_gram_array = ["".join(char_array[x : x + n_gram]) for x in range(0, len(char_array), n_gram)]  # create a an array of n_gram size element
    n_gram_distribution = {x: n_gram_array.count(x) for x in n_gram_array if n_gram_array.count(x) > occurrence }  # calculate occurrences and select them accorder to occurrence argument
    
    if plot_hist:
        plot.bar(n_gram_distribution.keys(), n_gram_distribution.values())
        [plot.text(a, b, b, horizontalalignment="center") for a, b in n_gram_distribution.items()]
        plot.show()
    return n_gram_distribution


def empirical_distribution(char_array: list, n_gram: int) -> dict:
    alphabet_size = 26 ** n_gram
    n_gram_array = ["".join(char_array[x : x + n_gram]) for x in range(0, len(char_array), n_gram)]  # create a structure of arrays of n_gram elements
    n_gram_distribution = {x: n_gram_array.count(x) / alphabet_size for x in n_gram_array}  # calculate occurrences distribution
    return n_gram_distribution

def n_gram_frequency(char_array: list, n_gram: int) -> dict:
    alphabet_size = len(char_array) / n_gram
    n_gram_array = ["".join(char_array[x : x + n_gram]) for x in range(0, len(char_array), n_gram)]  # create a structure of arrays of n_gram elements
    n_gram_distribution = {x: n_gram_array.count(x) / alphabet_size for x in n_gram_array}  # calculate occurrences distribution
    return n_gram_distribution

def text_entropy(hist: dict, text_len: int) -> int:
    char_array_prob, entropy = {k : v/text_len for k, v in hist.items()}, 0 #from occurrence to probrabilities
    for c in char_array_prob: entropy += char_array_prob[c]*log(char_array_prob[c], 2) #calculate entropy
    return entropy

def text_entropy_en_leanguage() -> int:
    entropy = 0
    for c,_ in en_frequency.items(): entropy += en_frequency[c]*log(en_frequency[c]*26, 2) #calculate entropy
    return entropy

def coincidence_index(hist: dict, text_len: int) -> float:
    denom = text_len * (text_len - 1)
    c_index = [((x * (x - 1)) / denom) for _, x in hist.items()]
    return sum(c_index)


def run():
    with open(os.path.dirname(__file__) + ".." + os.sep + ".." + os.sep + "MobiDickCap1.txt","r") as myfile:
        text = myfile.read().replace("\n", "")

    char_array = list(filter(str.isalpha, text.replace(" ", "").lower()))
    char_array = [s.translate(str.maketrans("", "", string.punctuation)) for s in char_array]
    
    n_gram_hist = n_gram_histogram(char_array, 3, 7, True)
    e_dist = empirical_distribution( char_array, 3)
    c_index = coincidence_index(n_gram_histogram(char_array, 1, 0), len(char_array))
    e = text_entropy( n_gram_histogram(char_array,1,0), len(char_array))


if __name__ == "__main__":
    run()
