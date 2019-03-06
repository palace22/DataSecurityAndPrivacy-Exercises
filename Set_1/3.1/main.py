
def toArray26( text: str):
    array_char = list(text.replace(' ','').lower())    
    array_char = [ord(c)-97 for c in array_char]

    return array_char

def histogram( char_array:list ) -> dict:
    letters_dict = { x : char_array.count(x) for x in char_array }
    return letters_dict
    
def empirical_distribution( char_array:list, n_gram:int ) -> dict:
    alphabet_size = 26**n_gram
    n_gram_array = [char_array[x:x+n_gram] for x in range(0, len(char_array), n_gram)]   #create a structure of arrays of n_gram elements
    n_gram_array = [ ''.join(x) for x in n_gram_array] #transform structure of arrays in an array of n_gram size string element
    n_gram_distribution = { x : n_gram_array.count(x)/alphabet_size for x in n_gram_array} #calculate occurrences distribution
    return n_gram_distribution

def coincidence_index( hist: dict, text_len:int)->float:
    denom = text_len*(text_len-1)
    c_index = [ ((x*(x-1))/denom) for _,x in hist.items() ]
    return sum(c_index)

def run():
    text = ""#load text
    char_array = list(text.replace(' ','').lower())

    print (histogram(char_array))
    c_index = coincidence_index( hist, len(char_array))




if __name__ == "__main__":
    pass
