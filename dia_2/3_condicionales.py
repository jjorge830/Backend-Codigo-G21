def resultado_final(nota, alumno):

    if 18 <= nota <= 20:
        print(alumno, "tiene felicitación pública")

    elif 15 <= nota <= 17:
        print(alumno, "aprobó y está exonerado de exposición final")

    elif 11 <= nota <= 14:
        print(alumno, "aprobó")

    else:
        print(alumno, "desaprobó")

resultado_final(19, "Jorge")
resultado_final(16, "Ana")
resultado_final(12, "Luis")
resultado_final(8, "Carlos")