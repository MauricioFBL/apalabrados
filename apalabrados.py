from typing import final
import db_connection


def numero(num: float) -> None:
    pass


def texto(string: str) -> None:
    arr = list(string)
    initial = arr[0]
    final = arr[len(string)-1]


def character(char_list: list) -> None:
    pass


def is_num(value):
    try:
        value = (float)(value)
        return True
    except:
        return False


def contains_special(input_v):
    specials = []
    arr = list(input_v)
    char = ''
    for x in range(len(input_v)):
        if (ord(arr[x]) > 31 and ord(arr[x]) < 48) or (ord(arr[x]) > 57 and ord(arr[x]) < 65) or (ord(arr[x]) > 90 and ord(arr[x]) < 97) or (ord(arr[x]) > 122 and ord(arr[x]) < 256):
            char = arr[x]
            specials.append(char)
    return specials


def eveluate():
    input_v = input("Digite algo: ")
    if is_num(input_v):
        numero()
    else:
        specials = contains_special(input_v)
        if len(specials) > 0:
            character(specials)
        texto(input_v)


eveluate()
