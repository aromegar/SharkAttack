
import re

def sacar_mes(fecha):

    """
    sacamos el mes a partir de una fecha formato dd-mm-aaaa o dd.mm.aaaa o similares:
    argumentos:
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
    limpia los meses "feos"
    busca el nombre de un mes en un string que le pasamos
    argumentos:
        feo: un string que no es exactamente el nombre de un mes, pero podría contenerlo
    devuelve el nombre de un mes, si aparece, en formato 3 letras
    """
    meses=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    for i in meses:
        if i in feo:
            return i
    return "nulo"

def spec_only(strlargo):

    """
    busca la especie en un string 
    argumentos:
        strlargo: un string en el que puede que aparezca la palabra "shark" o "Shark"
     devuelve la palabra shark y la inmediatamente anterior
    """

    if type(strlargo)==str:
        limpia=re.findall('\w+ .hark',strlargo)
    else:
        return "unknown"

    if len(limpia)>=1:
        return limpia[0].lower()
    else:
        return "unknown"


def verano(h,m):
    """
    devuelve un valor numérico para el verano
    argumentos:
        h: string, representa el hemisferio, puede ser "norte", "sur" o "-"
        m: string, mes en formato 3 letras, tambien puede ser "nulo"
    devuelve un valor numérico comprendido entre el 1 y el 6
    """

    ver_nor={"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":6,"Aug":5,"Sep":4,"Oct":3,"Nov":2,"Dec":1,"nulo":"-"}
    ver_sur={"Jan":6,"Feb":5,"Mar":4,"Apr":3,"May":2,"Jun":1,"Jul":1,"Aug":2,"Sep":3,"Oct":4,"Nov":5,"Dec":6,"nulo":"-"}
    if h=="norte":
        v=ver_nor[m]
    elif h=="sur":
        v=ver_sur[m]
    else:
        v="-"
    
    return v
