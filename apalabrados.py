import db_connection

def numero(num: float)-> None:
    pass


def texto(string: str)-> None:
    pass


def numero(character: str)-> None:
    pass


def is_num(value):
    try:
        value = (float)(value)
        return True
    except:
        return False


def eveluate():
    value = input("Digite algo")
    print(is_num(value))


eveluate()

