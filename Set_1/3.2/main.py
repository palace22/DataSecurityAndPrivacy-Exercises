import numpy as np
import random
from itertools import combinations
from sympy import Matrix


def from_char_to_array_mod26(text: str) -> list:
    """delete not alphabetical letter and convert the text in array on number: a = 0, b = 1, etc."""
    array = [
        ord(c) - 97 for c in list(filter(str.isalpha, text.replace(" ", "").lower()))
    ]
    return array


def from_array_mod_26_to_char(array: list) -> str:
    """convert number in text: 0 = a, 1 = b, etc. and join them"""
    char_array = [[chr(c + 97) for c in r] for r in array]
    text = "".join(["".join(r) for r in char_array])
    return text


def mcd(a, b):
    while b:
        a, b = b, a % b
    return a


def create_array(array: list, block_size: int) -> list:
    """create array of block size element"""
    return [array[x : x + block_size] for x in range(0, len(array), block_size)]


def generate_key(size: int):
    print("... Generating key ...\n")
    while True:
        tmp_key = np.random.randint(0, 25, (size, size))
        if mcd(np.linalg.det(tmp_key), 26) == 1:
            return tmp_key
        else:
            continue


def encript(plain_text: str, key: list, block_size: int = 2) -> list:
    print("... Encripting ...\n")
    plain_text_array = from_char_to_array_mod26(plain_text)
    print("Text len: \n", len(plain_text_array))
    plain_text_array = create_array(plain_text_array, block_size)
    plain_text_array = np.transpose(np.array(plain_text_array))
    cipher_text = np.dot(key, plain_text_array) % 26  # compute K x PT
    cipher_text = from_array_mod_26_to_char(cipher_text)
    return cipher_text


def decript(cipher_text: str, key: list, block_size: int = 2) -> list:
    print("... Decripting ...\n")
    block_size = int(len(cipher_text) / block_size)
    cipher_text = from_char_to_array_mod26(cipher_text)
    cipher_text = create_array(cipher_text, block_size)
    inverse_key = Matrix(key).inv_mod(26)
    plain_text = np.transpose(
        np.dot(inverse_key, cipher_text) % 26
    )  # compute K^-1 x CT
    plain_text = from_array_mod_26_to_char(plain_text)
    return plain_text


def attack(plain_text: str, cipher_text: str, block_size: int = 2):
    def search_plain_text_inverse(
        plain_text_array: list, block_size: int
    ) -> (list, list):
        print("... Setting possible combinations ...\n")
        col = len(plain_text_array[0])
        row = len(plain_text_array)
        enum = [e for e in range(0, row)]
        print("... Finding invertible plain text square ...\n")
        for indexes in combinations(enum, col):
            tmp = [plain_text_array[i] for i in indexes]

            if mcd(int(round(np.linalg.det(tmp) % 26)), 26) == 1:
                tmp = np.transpose(
                    np.array(Matrix(tmp).inv_mod(26))
                )  # invert the invertible SquarePT
                return tmp, indexes
        print("Invertible plain text square don't find!!\n")

    block_size_cipher_text = int(len(cipher_text) / block_size)
    plain_text_array = from_char_to_array_mod26(plain_text)
    cipher_text_array = from_char_to_array_mod26(cipher_text)
    plain_text_array = np.array(create_array(plain_text_array, block_size))
    cipher_text_array = np.transpose(
        create_array(cipher_text_array, block_size_cipher_text)
    )
    square_plain_text_inverse, indexes = search_plain_text_inverse(
        plain_text_array, block_size
    )
    square_cipher_text = np.transpose(
        np.array([cipher_text_array[i] for i in indexes])
    )  # select CT's columns according to invertible square PT matrix
    key = np.array(
        np.dot(square_cipher_text, square_plain_text_inverse) % 26
    )  # compute SquareCT x SquarePTinverse
    return key


def main():
    block_size = 10
    plain_text = "Call me Ishmael. Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off—then, I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the feelings towards the ocean with me."
    plain_text = plain_text.replace("\n", "")
    key = generate_key(block_size)
    cipher_text = encript(plain_text, key, block_size)
    decripted_cipher_text = decript(cipher_text, key, block_size)

    print("KEY: \n", key)
    # print("PT: \n", plain_text)
    # print("CT: \n", cipher_text)
    # print("DECRIPTED PT: \n", decripted_cipher_text)
    """ATTACK"""
    key_hacked = attack(plain_text, cipher_text, block_size)
    print("KEY HACKED: \n", key_hacked)


if __name__ == "__main__":
    main()
