"""
    Las variables se utilizan con la finalidad de tener una organizacion en el desarrollo de software, estas variables
    tienen que ser nombradas acorde a los que nos encontremos desarrollando.

"""


def variables():
    """ Como nombre de variable le asignamos mascota y como valor le decimos PANDA e imprimimos la informacion
    estas son de tipo string o str """

    mascota = "PANDA"
    print(f"El resultado de mascota = {mascota} el tipo de variables es = {type(mascota)}")

    """ Ahora miraremos las variables tipo numericas, estas pueden ser enteros o con decimales 
        para ello realizaremos la asignacion del nombre del panda, su edad en entero y con decimales
        para poder ver su diferencia de variables.
    """
    nombremascota = 'Tommy' # Variables tipo STR (String)
    edadmascota = 12 # variable tipo INT (Entero)
    edadmascota2 = 12.6 # variables tipo FLOAT (Flotante)

    print(f''' El {mascota} se llama {nombremascota} y tiene {edadmascota} meses, para ser exactos {edadmascota2} meses.
    Sus tipos de variables son = nombre: {type(nombremascota)}, edadmascota: {type(edadmascota)}, edadmascota2: {type(edadmascota2)} 
    ''')

    # Vamos a solicitar por consola que se ingrese un valor.
    # Esto se realizara mediante la funcion Input.

    nombremascota = str(input("Cual es el nombre de tu mascota?: "))
    edadmascota = int(input(f"Cual es la edad de {nombremascota}: "))
    print(f"El nombre de tu mascota es {nombremascota} y tiene la edad de {edadmascota} anos")


