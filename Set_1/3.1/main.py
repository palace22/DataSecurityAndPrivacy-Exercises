import string
import os
import matplotlib.pyplot as plot

def toArray26( text: str):
    array_char = list(text.replace(' ','').lower())    
    array_char = [ord(c)-97 for c in array_char]

    return array_char
    
def n_gram_histogram( char_array:list, n_gram:int = 3, occurrence: int = 3, plot_hist: bool  = False ) -> dict:
    n_gram_array = [ ''.join(char_array[x:x+n_gram]) for x in range(0, len(char_array), n_gram)]   #create a an array of n_gram size element
    n_gram_distribution = { x : n_gram_array.count(x) for x in n_gram_array if n_gram_array.count(x) > occurrence} #calculate occurrences and select them accorder to occurrence argument
    if plot_hist:
        plot.bar(n_gram_distribution.keys(), n_gram_distribution.values())
        plot.show()
    return n_gram_distribution

def empirical_distribution( char_array:list, n_gram:int ) -> dict:
    alphabet_size = 26**n_gram
    n_gram_array = [char_array[x:x+n_gram] for x in range(0, len(char_array), n_gram)]   #create a structure of arrays of n_gram elements
    n_gram_array = [ ''.join(x) for x in n_gram_array] #transform structure of arrays in an array of n_gram size string element
    n_gram_distribution = { x : n_gram_array.count(x)/alphabet_size for x in n_gram_array} #calculate occurrences distribution
    return n_gram_distribution

def n_gram_frequency( char_array:list, n_gram:int ) -> dict:
    alphabet_size = len(char_array)/n_gram
    n_gram_array = [char_array[x:x+n_gram] for x in range(0, len(char_array), n_gram)]   #create a structure of arrays of n_gram elements
    n_gram_array = [ ''.join(x) for x in n_gram_array] #transform structure of arrays in an array of n_gram size string element
    n_gram_distribution = { x : n_gram_array.count(x)/alphabet_size for x in n_gram_array} #calculate occurrences distribution
    return n_gram_distribution

def coincidence_index( hist: dict, text_len:int)->float:
    denom = text_len*(text_len-1)
    c_index = [ ((x*(x-1))/denom) for _,x in hist.items() ]
    return sum(c_index)

def run():
    with open("d:/Unifi/Data security and Privacy/Data security and privacy - programming exercises/Set_1/MobiDickCap1.txt", 'r') as myfile:
        text=myfile.read().replace('\n', '')
    
    char_array = list(filter(str.isalpha, text.replace(' ','').lower()))
    char_array = [s.translate(str.maketrans('', '', string.punctuation)) for s in char_array]

    hist = histogram(char_array)
    c_index = coincidence_index( hist, len(char_array))
    e_dist = empirical_distribution( char_array, 2)['ig'] 




if __name__ == "__main__":
    run()
