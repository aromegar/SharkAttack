
import re

def sacar_mes(fecha):

    """
    sacamos el mes a partir de una fecha formato dd-mm-aaaa o dd.mm.aaaa o similares:
    arg(x)
    x: un string con puntos o guiones
    devuelve el penúltimo elemento
    """
    k=["0","0","0"]
    for s in ["-","."]:
        if type(fecha)==float:
            pass
        elif s in fecha:
            k=fecha.split(s)
            
    return k[-2]

def limpiar_mes(feo):

    """
    limpia los meses feos
    """
    meses=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    for i in meses:
        if i in feo:
            return i
    return "nulo"

def spec_only(strlargo):

    """
    coge un string y me devuelve la palabra shark y la inmediatamente anterior
    """

    if type(strlargo)==str:
        limpia=re.findall('\w+ .hark',strlargo)
    else:
        return "unknown"

    if len(limpia)>=1:
        return limpia[0].lower()
    else:
        return "unknown"