
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

def run():
    text = ""#load text
    char_array = list(text.replace(' ','').lower())

    print (histogram(char_array))
    [ print( empiric_distribution( char_array, x) ) for x in range(2, 5)] 




if __name__ == "__main__":
    pass
