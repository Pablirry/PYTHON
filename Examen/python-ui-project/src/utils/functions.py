def sms_revival(cadena: str) -> str:
    result = ""
    for cad in cadena:
        if cad.lower() not in 'aeiou':
            result += cad
    return result

def texto_a_morse(cadena: str) -> str:
    morse_dict = {
        'A': '·-', 'B': '-···', 'C': '-·-·', 'D': '-··', 'E': '·',
        'F': '··-·', 'G': '--·', 'H': '····', 'I': '··', 'J': '·---',
        'K': '-·-', 'L': '·-···', 'M': '·-··', 'N': '--', 'Ñ': '--·--',
        'O': '---', 'P': '·--·', 'Q': '--.-', 'R': '·-·', 'S': '···',
        'T': '-', 'U': '··-', 'V': '···-', 'W': '·--', 'X': '-··--',
        'Y': '-·--', 'Z': '--··'
    }
    resultado = ""
    for c in cadena:
        resultado += morse_dict.get(c.upper(), c) + " "
    return resultado.strip()

def limpia_notas(notas: list) -> list:
    resultado = []
    for n in notas:
        if 0 <= n <= 10:
            resultado.append(n)
    return resultado

def emula_sum(lista: list) -> float:
    total = 0
    for num in lista:
        total += num
    return total

def dias_del_mes(mes: str) -> int:
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mes = mes.lower()
    if mes in meses:
        return dias[meses.index(mes)]
    return -1

def enlista(cadena: str) -> list:
    numeros = cadena.split('/')
    resultado = []
    for num in numeros:
        resultado.append(int(num))
    return resultado

def cita_con_estilo(tu: int, cita: int) -> int:
    if tu <= 2 or cita <= 2:
        return 0
    elif tu >= 8 or cita >= 8:
        return 2
    else:
        return 1