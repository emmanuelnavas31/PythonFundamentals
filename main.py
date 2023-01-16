from strings import strings
from tiposdatos import tiposdedatos
from variables import variables
from impresiones import impresionSencilla


def main(num):
    if num == 1:
        impresionSencilla()
    elif num == 2:
        variables()
    elif num == 3:
        variables()
    elif num == 4:
        tiposdedatos()
    elif num == 5:
        strings()
    else:
        print("Opcion invalida")


if __name__ == '__main__':
    opciones = int(input(f''' Por favor seleccione una opcion: 
        1. Impresiones.
        2. Variables.
        3. Operaciones.
        4. Tipos de datos.
        5. Strings.
    -------> '''))
    main(opciones)
