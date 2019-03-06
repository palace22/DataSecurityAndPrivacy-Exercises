
def toArray26( text: str):
    array_char = list(text.replace(' ','').lower())    
    array_char = [ord(c)-97 for c in array_char]

    return array_char

def histogram( char_array:list ) -> dict:
    letters_dict = { x : char_array.count(x) for x in char_array }
    return letters_dict
    
def empiric_distribution( char_array:list, n_gram:int ) -> dict:
    n_gram_array = [ ''.join(x) for x in char_array[x:x+n_gram] for x in range(0, len(char_array), n_gram)]   
    n_gram_distribution = { x : n_gram_array.count(x)/len(x) for x in n_gram_array} 
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
