"""
Existen diferentes tipos de datos.

"""


def tiposdedatos():
    print("1 tipos de datos STRING")
    mi_nombre = "Nala"
    print(f"Mascota => {mi_nombre} tipo de dato = {type(mi_nombre)}")
    mi_nombre = 'Nalita'
    print(f"Mascota => {mi_nombre} tipo de dato = {type(mi_nombre)}")

    """Vamos ahora a realizar la revision de los tipos de datos que se manejan en las
    variables."""

    print("2. Tipos de datos ENTEROS")
    edad = 4
    print(f"Edad = {edad} tipo de dato = {type(edad)}")

    print("3. Tipos de datos FLOTANTES")
    edad2 = 4.5
    print(f"La edad con meses es {edad2} tipo de dato = {type(edad2)}")

    print("4. Tipos de datos BOOLEANOS")
    es_blanca = True
    es_negra = False
    print(f"5. Es de color blanca = {es_blanca} y negra ={es_negra} tipo de dato = {type(es_negra)}")

    """
    Tenemos que tener en cuenta que cada vez que utilizamos un input estos valores 
    por defecto son de tipo string, por ende si tenemos que solicitar un valor de algun
    tipo especifico tenemos que realizar la asignacion correspondiente.
    """
    edad = input("Ingrese la edad = ")
    print(f"La edad {edad} ingresada es de tipo {type(edad)}")

    # para que sea completamente entero tendremos que indicar el tipo de dato en el input

    edad2 = int(input("Ingrese la nueva edad = "))
    print(f"La edad ahora es {edad2} y el tipo de dato es {type(edad2)}")
