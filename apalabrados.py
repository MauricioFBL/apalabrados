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
            print(f'Rows inserted: {str(count)} number = {num} acumulated {(str)(acumullated)}')
            return (f'row inserted number = {num} acumulated {(str)(acumullated)}')
    except Exception as e:
        print('error: ', e)
        return e


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
            print(f'Rows inserted: {str(count)} {string} {initial} {final}')
            return f'Rows inserted: {str(count)} {string} {initial} {final}'
    except Exception as e:
        print('error: ', e)
        return e


def character(char_list: list) -> None:
    connection = db_connection.connection()
    try:
        with connection.cursor() as cursor:
            for char in char_list:
                count = cursor.execute("""
                    INSERT INTO CARACTER (CARACTER) VALUES (?)""",
                                       char).rowcount
            connection.commit()
            print('Rows inserted: ' + str(count))
            print(char_list)
            return char_list
    except Exception as e:
        print('error: ', e)
        return e


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


def get_numbers() -> tuple[list, list]:
    connection = db_connection.connection()
    try:
        with connection.cursor() as cursor:
            result_n = []
            result_a = []
            cursor.execute('SELECT NUMERO, ACUMULADO FROM NUMEROS;')
            rows = cursor.fetchall()
            for row in rows:
                # print(row.NUMERO, row.ACUMULADO)
                result_n.append(row.NUMERO)
                result_a.append(row.ACUMULADO)

            return result_n, result_a
    except Exception as e:
        print('error: ', e)
        return e, None


def get_text() -> tuple[list, list, list]:
    connection = db_connection.connection()
    try:
        with connection.cursor() as cursor:
            result_t = []
            result_i = []
            result_f = []
            cursor.execute('SELECT TEXTO, INICIAL, FINAL FROM TEXTO;')
            rows = cursor.fetchall()
            for row in rows:
                # print(row.TEXTO, row.INICIAL, row.FINAL)
                result_t.append(row.TEXTO)
                result_i.append(row.INICIAL)
                result_f.append(row.FINAL)

            return result_t, result_i, result_f
    except Exception as e:
        print('error: ', e)
        return e, None, None


def get_char() -> list:
    connection = db_connection.connection()
    try:
        with connection.cursor() as cursor:
            result_c = []
            cursor.execute('SELECT CARACTER FROM CARACTER;')
            rows = cursor.fetchall()
            for row in rows:
                # print(row.CARACTER)
                result_c.append(row.CARACTER)

            return result_c
    except Exception as e:
        print('error: ', e)
        return e


def eveluate(cadena = ''):
    input_v = cadena
    # input_v = input('algo: ')
    if len(cadena) > 0:
        if is_num(input_v):
            numero(input_v)
        else:
            specials = contains_special(input_v)
            texto(input_v)
            if len(specials) > 0:
                character(specials)
# get_numbers()
# eveluate()
# get_char()
