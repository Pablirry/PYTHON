def sms_revival(cadena:str)->str:

    result = ""
    for cad in cadena:
        if cad.lower() not in 'aeiou':
            result +=cad
    return result

    """
    Ejercicio 1 (1.66 puntos)
    Escribe una función llamada "sms_revival" que, dada una cadena de texto
    (palabra o frase) devuelva una copia que no tenga ninguna vocal (mayúscula o
    minúscula). Para simplificar, no es necesario considerar el caso de que las
    vocales tengan tilde.

    param cadena una cadena de texto
    return otra cadena sin vocales (mayúsculas ni minúsculas)
    """

def texto_a_morse(cadena:str)->str:

    morse_dict = {
        'A' : '·-', 'B' : '-···', 'C' : '-·-·',  'D' : '-··', 'E' : '·',
        'F' : '··-·',  'G' : '--·',   'H' : '····',  'I' : '··',    'J' : '·---',
        'K' : '-·-',   'L' : '·-···', 'M' : '·-··',  'N' : '--',    'Ñ' : '--·--',
        'O' : '---',   'P' : '·--·',  'Q' : '--.-',  'R' : '·-·',   'S' : '···',
        'T' : '-',     'U' : '··-',   'V' : '···-',  'W' : '·--',   'X' : '-··--',
        'Y' : '-·--',  'Z' : '--··'
    }
    resultado = ""
    for c in cadena:
        resultado += morse_dict.get(c.upper(), c) + " "
    return resultado.strip()

    """
    Ejercicio 2 (1.66 puntos)
    Dada una cadena de texto (palabra o frase) la devuelve convertida a
    código morse. La relación de conversiones entre las letras (los caracteres)
    y el código es el siguiente:
    'A' -> '·-';    'B' -> '-···';  'C' -> '-·-·';  'D' -> '-··';   'E' -> '·';
    'F' -> '··-·';  'G' -> '--·';   'H' -> '····';  'I' -> '··';    'J' -> '·---';
    'K' -> '-·-';   'L' -> '·-···'; 'M' -> '·-··';  'N' -> '--';    'Ñ' -> '--·--';
    'O' -> '---';   'P' -> '·--·';  'Q' -> '--.-';  'R' -> '·-·';   'S' -> '···';
    'T' -> '-';     'U' -> '··-';   'V' -> '···-';  'W' -> '·--';   'X' -> '-··--';
    'Y' -> '-·--';  'Z' -> '--··'
    Aquellos caracteres que no estén en la relación dada (por ejemplo, números)
    se tienen que mantener como están en lugar de convertirlos

    param cadena una cadena de texto
    return otra cadena con las letras convertidas a morse
    """
    ...

def limpia_notas(notas:list)->list:

    resultado = []
    for n in notas:
        if 0 <= n <= 10:
            resultado.append(n)
    return resultado

    """
    Ejercicio 3 (1.66 puntos)
    Escribe la función "limpia_notas" que reciba como argumento una lista de
    números (enteros o reales) y devuelva otra lista con aquellos números que
    puedan ser notas reales de un examen, es decir, en el rango de 0 a 10.
    Este ejercicio se puede resolver creando una lista nueva (más fácil) o
    eliminando los datos incorrectos de la lista original (más complejo)

    param notas una lista con valores reales
    return otra lista con los valores válidos como nota (rango 0 a 10)
    """
    ...

from numbers import Number
def emula_sum(lista:list)->Number:
    total = 0
    for num in lista:
        total += num
    return total

    print(total)
    """
    Ejercicio 4 (1.66 puntos)
    Escribe una función llamada "emula_sum" que reciba como parámetro una lista
    de números (enteros o reales) y devuelva la suma de dichos números.
    Nota: evidentemente no se puede usar sum ni ninguna otra función propia de
    Python para resolver este ejercicio.

    param lista una lista de números enteros o reales
    return la suma de los números de la lista
    """
    ...

def dias_del_mes(mes:str)->int:
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mes = mes.lower()
    if mes in meses:
        return dias[meses.index(mes)]
    return -1



    """
    Ejercicio 5 (1.66 puntos)
    Dada una cadena de texto (en mayúsculas, minúsculas o cualquier combinación)
    indicando el mes del año, devuelva cuántos días tiene ese mes o -1 si se
    introduce un mes que no existe. Por simplicidad, febrero tiene 28 días.
    Nota: hay una forma sencilla de hacerlo a partir de los contenidos dados en
    clase que no se basa en el uso de condicionales. Esa es la única forma válida
    admitida.

    param una cadena de texto indicando un mes
    return el número de días del mes o -1 si no es un mes real
    """
    ...

def enlista(cadena:str)->list:

    numeros = cadena.split('/')
    resultado = []
    for num in numeros:
        resultado.append(int(num))
    return resultado


    """
    Ejercicio 6 (1.66 puntos)
    Recibe como parámetro una cadena de texto del tipo "n1/n2/n3/n4/…" y
    devuelve una lista de enteros formada por los números n1, n2, n3, n4...
    Por simplificación, la cadena siempre contendrá una "/" entre dos números

    param cadena una cadena de texto con al menos una "/" entre dos números
    return la lista de los números separados por "/"
    """
    ...

def cita_con_estilo(tu:int, cita:int)->int:

    if tu <= 2 or cita <= 2:
        return 0
    elif tu >= 8 or cita >= 8:
        return 2
    else:
        return 1


    """
    Ejercicio 7 (0.67 puntos)
    Tú y tu cita estáis intentando conseguir una mesa en un restaurante. El parámetro "tu”
    es la elegancia de tu ropa en el rango de 0…10 y el parámetro "cita” es la elegancia de
    la ropa de tu cita. El resultado de conseguir una mesa se codifica como un entero con los
    valores 0=no, 1=quizás, 2=sí. Si alguno de los es muy estiloso, 8 o superior, entonces el
    resultado es 2 (sí). Con la excepción de que si alguno de los dos tiene un estilo de 2 o
    menor, entonces el resultado es 0 (no). En otro caso el resultado es 1 (quizás)
    Escribe una función llamada "cita_con_estilo” que reciba como parámetros dos enteros
    representando tu estilo y el de tu cita y devuelva el resultado codificado como se indica (0, 1 ó 2).

    param tu entero indicando la elegancia de tu ropa (entre 0 y 10)
    param cita entero indicando la elegancia de la ropa de tu cita (entre 0 y 10)
    return un entero indicando si conseguiréis mesa en el restaurante
    """
    ...

def test(f, m):
    """Prueba de cada función"""
    c = 0
    for i, o in m:
        if isinstance(i, tuple):
            p = f(*i)
        else:
            p = f(i)
        print('Probando %s: %s'%(i, p))
        print('¿Salida exitosa?', p==o, (p!=o)*(" (Se esperaba %s)"%o))
        if p==o:
            c+=1

    if c==len(m):
        print('\t-> ¡Todas las pruebas son correctas!')
    else:
        print('\t-> %d/%d correctas'%(c, len(m)))


def pruebas(ans:int)->None:
    """Pruebas de todo"""

    if ans == 1:
        datos =  [['Hola mundo!', 'Hl mnd!']]
        datos += [['AAAAAAAH!', 'H!']]
        datos += [["Espayderman", "spydrmn"]]
        datos += [["voy al 1A", "vy l 1"]]
        datos += [['Whisky bueno: ¡excitad mi frágil pequeña vejez!', 'Whsky bn: ¡xctd m frágl pqñ vjz!']]
        test(sms_revival, datos)

    elif ans == 2:
        datos =  [['Hola mundo!', '····---·-····- ·-····----··---!']]
        datos += [['1 2 3', '1 2 3']]
        datos += [['Whisky bueno: ¡excitad mi fragil pequeña vejez!', '·--·········-·--·-- -·····-·-----: ¡·-··---·-···-·--·· ·-···· ··-··-··---····-··· ·--··--.-··-·--·--·- ···-··---·--··!']]
        datos += [['SGEM', '···--···-··']]
        datos += [['Gustavo', '--···-···-·-···----']]
        datos += [['27 de febrero de 2025', '27 -··· ··-··-····-···-·--- -··· 2025']]
        test(texto_a_morse, datos)

    elif ans == 3:
        datos =  [[[-2, 3, 12],[3]]]
        datos += [[[],[]]]
        datos += [[[2, 3, 10], [2, 3, 10]]]
        datos += [[[-2, 23, 12], []]]
        test(limpia_notas, datos)

    elif ans == 4:
        datos =  [[[1, 4, -2, 1], 4]]
        datos += [[[], 0]]
        datos += [[[1, -1, 2, -2], 0]]
        datos += [[[0, 0, 0], 0]]
        datos += [[[-1, -2], -3]]
        datos += [[[.3, .7], 1.0]]
        test(emula_sum, datos)

    elif ans == 5:
        datos =  [["Enero", 31]]
        datos += [["feBrero", 28]]
        datos += [["juliembre", -1]]
        datos += [["lunes", -1]]
        datos += [["lunes 27 de febrero", -1]]
        datos += [["DiCiEmBrE", 31]]
        datos += [["oCTuBRe", 31]]
        test(dias_del_mes, datos)

    elif ans == 6:
        datos =  [["1/2/3" ,[1, 2, 3]]]
        datos += [["13/15", [13, 15]]]
        datos += [["27/02/2023", [27, 2, 2023]]]
        datos += [["237/02/2022", [237, 2, 2022]]]
        datos += [["23/13/2022",  [23, 13, 2022]]]
        datos += [["05/02/22", [5, 2, 22]]]
        datos += [["15/02/20223", [15, 2, 20223]]]
        datos += [["16/12/22/21", [16, 12, 22, 21]]]
        test(enlista, datos)

    else:
        datos =  [[(5, 10), 2]]
        datos += [[(5, 2), 0]]
        datos += [[(5, 5), 1]]
        datos += [[(3, 3), 1]]
        datos += [[(10, 2), 0]]
        datos += [[(2, 9), 0]]
        datos += [[(9, 9), 2]]
        datos += [[(10, 5), 2]]
        datos += [[(2, 2), 0]]
        datos += [[(3, 7), 1]]
        datos += [[(2, 7), 0]]
        datos += [[(6, 2), 0]]

        test(cita_con_estilo, datos)


def menu()->None:
    """Menu básico del examen"""
    prompt = '¿Qué quieres probar?\n'
    prompt += '1) Ejercicio 1 (sms_revival)\n'
    prompt += '2) Ejercicio 2 (texto_a_morse)\n'
    prompt += '3) Ejercicio 3 (limpia_notas)\n'
    prompt += '4) Ejercicio 4 (emula_sum)\n'
    prompt += '5) Ejercicio 5 (dias_del_mes)\n'
    prompt += '6) Ejercicio 6 (enlista)\n'
    prompt += '7) Ejercicio 7 (cita_con_estilo)\n'
    prompt += '8) Salir\n'
    ans = '' # Respuesta dada

    while ans not in [str(i+1) for i in range(len(prompt.split('\n'))-2)]:
        ans = input(prompt)

    ans = int(ans)
    if ans != 8:
        pruebas(ans)

        print('Volviendo al menu principal...\n')
        menu()

    else:
        input('Gracias por venir')

def arranque():
    """try/except para el programa principal"""
    try:
        menu()
    except Exception as error:
        print('\nError de tipo %s: %s\n'%(type(error).__name__, error.args))
        import traceback
        print('Traza de error: %s'%traceback.format_exc())
        print('\nReiniciando.\n')
        arranque()
    finally:
        pass

if __name__ == '__main__':
    arranque()