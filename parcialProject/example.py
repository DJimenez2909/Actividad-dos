
# Eje1 conversión de tipos de datos (Enteros, Decimales y Cadenas)
def conversion_tipos_datos():
    # El numero de comversion de Entero a Cadena
    num_entero =10
    str_entero = str(num_entero)
    print(f"Entero a cadena: {str_entero}")

    # el numero de conversion de Decimal a Cadena
    num_decimal =3.14
    str_decimal = str(num_decimal)
    print(f"Decimal a cadena: {str_decimal}")

    # el numero de conversion de Cadena a Entero
    cadena_entero ="25"
    entero = int(cadena_entero)
    print(f"Cadena a entero: {entero}")

    # Cadena a Decimal
    cadena_decimal = "19.99"
    decimal = float(cadena_decimal)
    print(f"Cadena a decimal: {decimal}")


# Eje2 para multilíneas de cadenas
def multilineas_cadenas():
    multilinea = """Esta es una cadena que tiene múltiples líneas, es decir, ocupa varias líneas en el código."""
    print(multilinea)



# Eje3  la exprecion y función len()
def longitud_cadena():
    cadena = "chanchito feliz"
    print(f"La longitud de la cadena es: {len(cadena)}")


# Eje4 la expresion de  subcadenas que la cual representa a medida de sus caracteres
def subcadenas():
    cadena = "Duban Jimenez"

    # Eje5 Obtener los primeros n caracteres
    n = 5
    print(f"Los primeros {n} caracteres son: {cadena[:n]}")

    # Obtener los caracteres de en medio
    inicio = 2
    final = 6
    print(f"Los caracteres del medio son: {cadena[inicio:final]}")

    # Obtener los últimos n caracteres
    n = 7
    print(f"Los últimos {n} caracteres son: {cadena[-n:]}")


# Eje5 la expresion y la  función upper()
def convertir_upper():
    cadena = "chanchito feliz"
    print(f"Cadena en mayúsculas: {cadena.upper()}")


# Eje5 L a exprecion y la  función lower()
def convertir_lower():
    cadena = "CHANCHITO FELIZ"
    print(f"Cadena en minúsculas: {cadena.lower()}")

#segunda parte de la actividad
# Actividad:
# Multilíneas de cadenas de caracteres
def multilineas_actividad():
    poema = """En el bosque profundo, donde el viento susurra. La luna refleja su luz, en la calma nocturna."""
    print(poema)


# Eje6 la exprecion y la función strip()
def funcion_strip():
    cadena_con_espacios = "   canchito , feliz   "
    print(f"Cadena sin espacios en los extremos: '{cadena_con_espacios.strip()}'")


# Eje7 la exprecion y la función replace()
def funcion_replace():
    cadena = "Duban jiemenz es divertido"
    nueva_cadena = cadena.replace("divertido", "fascinante")
    print(f"Cadena modificada: {nueva_cadena}")


# Eje8 la expreciom y su función split()
def funcion_split():
    cadena = "Juan, Ana, Yuli, Andres"
    lista_palabras = cadena.split(", ")
    print(f"Lista de palabras: {lista_palabras}")


# Ejemplo para Formato de cadenas F-String
def f_string():
    nombre = "Duban Jimenez"
    edad = 19
    print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")


# Llamadas a las funciones
conversion_tipos_datos()
multilineas_cadenas()
longitud_cadena()
subcadenas()
convertir_upper()
convertir_lower()

# Actividad
multilineas_actividad()
funcion_strip()
funcion_replace()
funcion_split()
f_string()
