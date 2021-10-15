from typing import final
import db_connection


def numero(num: float) -> None:
    connection = db_connection.connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT SUM(NUMERO) FROM NUMEROS;')
            acumullated = (float)(cursor.fetchone()[0]) + (float)(num)
            count = cursor.execute("""
                INSERT INTO NUMEROS (NUMERO, ACUMULADO) VALUES (?,?)""", 
                    (float)(num), acumullated).rowcount
            connection.commit()
            print('Rows inserted: ' + str(count))
    except Exception as e:
        print('error: ', e)


def texto(string: str) -> None:
    arr = list(string)
    initial = arr[0]
    final = arr[len(string)-1]
    connection = db_connection.connection()
    try:
        with connection.cursor() as cursor:
            count = cursor.execute("""
                INSERT INTO TEXTO (TEXTO,INICIAL, FINAL) VALUES (?,?,?)""", 
                    string, initial, final).rowcount
            connection.commit()
            print('Rows inserted: ' + str(count))
    except Exception as e:
        print('error: ', e)

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
        numero(input_v)
    else:
        specials = contains_special(input_v)
        if len(specials) > 0:
            character(specials)
        texto(input_v)


eveluate()
