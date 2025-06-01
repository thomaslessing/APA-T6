import re

def normalizahoras(fileIn, fileOut):
    """
    Codigo que sirve para leer lo que contiene fileIn y escribirlo en fileOut
    """
    rehm = r"(?P<hh>\d\d?)[hH]((?P<mm>\d\d?)[mM])?"
    rehh_en_punto = r'(?P<hh_en_punto>\d\d?) en punto'
    rehh_y_media = r'(?P<hh_y_media>\d\d?) y media'
    rehh_menos_cuarto = r'(?P<hh_menos_cuarto>\d\d?) menos cuarto'
    rehh_y_cuarto = r'(?P<hh_y_cuarto>\d\d?) y cuarto'
    rehh_12 = r'(?P<hh_12>\d\d?) de la noche'
    renum = r'(?P<num>\d)\s+(?P<texto>[a-zA-ZàÀéÉèÈóÓòÒíÍúÚçÇñ\s]+)'

    with open(fileIn, "rt") as fpIn, open(fileOut, "wt") as fpOut:
        for linea in fpIn:
            while (match := re.search(rehm, linea)):
                fpOut.write(linea[: match.start()])
                if match.group("mm", "hh"):
                    hora = int(match["hh"])
                    min = int(match["mm"]) if match["mm"] else 0
                    if min > 60:
                        hora += 1
                        min -= 60
                fpOut.write(f'{hora:02d}:{min:02d}')
                linea = linea[match.end():]
                
            while (match := re.search(rehh_en_punto, linea)):
                fpOut.write(linea[: match.start()])
                if match.group("hh_en_punto"):
                    hora = int(match["hh_en_punto"])
                    min = 0
                # d-> Identificador de tipo entero
                fpOut.write(f'{hora:02d}:{min:02d}')
                linea = linea[match.end():]
                
            while (match := re.search(rehh_y_media, linea)):
                fpOut.write(linea[: match.start()])
                if match.group("hh_y_media"):
                    hora = int(match["hh_y_media"])
                    min = 30
                fpOut.write(f'{hora:02d}:{min:02d}')
                linea = linea[match.end():]
                
            while (match := re.search(rehh_menos_cuarto, linea)):
                fpOut.write(linea[: match.start()])
                if match.group("hh_menos_cuarto"):
                    hora = int(match["hh_menos_cuarto"]) - 1
                    min = 45
                fpOut.write(f'{hora:02d}:{min:02d}')
                linea = linea[match.end():]
                
            while (match := re.search(rehh_y_cuarto, linea)):
                fpOut.write(linea[: match.start()])
                if match.group("hh_y_cuarto"):
                    hora = int(match["hh_y_cuarto"])
                    min = 15
                fpOut.write(f'{hora:02d}:{min:02d}')
                linea = linea[match.end():]
                
            while (match := re.search(rehh_12, linea)):
                fpOut.write(linea[: match.start()])
                if match.group("hh_12"):
                    hora = int(match["hh_12"]) - 12
                    min = 0
                fpOut.write(f'{hora:02d}:{min:02d}')
                linea = linea[match.end():]
                
            while (match := re.search(renum, linea)):
                fpOut.write(linea[: match.start()])
                if match.group("num"):
                    num = int(match["num"])
                    texto = match["texto"]
                    if num == 7:
                        num = str("siete")
                fpOut.write(f'{num} {texto}')
                linea = linea[match.end():]
                
                
            fpOut.write(linea)
