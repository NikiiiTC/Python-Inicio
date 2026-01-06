# SLICING

texto = "PROGRAMACION" # CADA ESPACIO ES UN NÚMERO, EMPEZANDO POR EL 0, TAMBIÉN EN NEGATIVO A LA INVERSA.

print(texto[0:4])

print(texto[:4])

print(texto[8:])

print(texto[-4:])

print(texto[::-1])

print(texto[::-2])

# Funcion .replace() Encuentra las coincidencias de un texto. Buscar una cadena dentro de otra.
# Cambiar lo viejo por lo nuevo de manera automática. No modifica cadena, crea una nueva. Podemos limpiar simbolos raros, errores, o cambiar una palabra o caracter.
# Por ejemplo podemos buscar {nombre} y sustituir por un nombre de Usuario.
# texto .replace("viejo, "nuevo") y si le añadimos un número al final, será las veces que lo replace. .replace("viejo", "nuevo",2)
print()
frase = "Es salado"
frase.replace("salado","dulce")
print(frase.replace("salado","dulce"))
mensaje = "Hola, soy Nikita y estoy estudiando programacion. Programacion para programacion y programar"
nuevo_mensaje = mensaje.replace("programacion", "programasao")
print(nuevo_mensaje)

nuevo_mensaje1 = mensaje.replace("programacion", "programasaaaao",1)
print(nuevo_mensaje1)
print()
# Multiplicación de cadenas: 3*5=15 "Go"*3="GoGoGo"
mensaje = "Go"
print(mensaje*3)
mensaje1 = "-"
print(mensaje1*20)
mensaje2 = " "
print(mensaje2*5+"codigo")
mensaje3 = " "+"-"+"codigo morse"
print(mensaje3*5)
print()

#Buscar subcadenas en Python. find()
cadena = "Hola mundo"
posicion = cadena.find("mundo")
print(posicion)
# Nos dice en que índice está el primer caracter del nombre buscado.

cadena = "Mi carro me lo robaron"
posicion = cadena.find("lo")
print(posicion)
# O bien para más completo podemos hacer:
print(f"El indice de la subcadena lo: {posicion}")
# Va a darte el índice de la primera ocurrencia.

texto = "Iba por el monte, lo vi, me vio, me lo robaron, mi carro me lo robaron"
primera = texto.find("lo")

segunda = texto.find("lo", primera + 1)
print(f"primera aparición: {primera}")
print(f"segunda aparición: {segunda}")
print()

# Generador de Email
print("***Generador de Email***")
nombre_normalizado = " Nikita Chervonnyy "
print(f"Nombre usuario: {nombre_normalizado}")
# Normalizar nombre usuario, limpiar espacios en blanco
nombre_normalizado = nombre_normalizado.strip()
# Vamos a reemplazar espacios en blanco por .
nombre_normalizado = nombre_normalizado.replace(" ", ".")
print(f"Nombre usuario: {nombre_normalizado}")
# Convertirmos todo a minisculas
nombre_normalizado = nombre_normalizado.lower()
# control+r para cambiar todos los nombres de un tipo por otro diferente a la vez
print(f"Nombre usuario normalizado: {nombre_normalizado}")

nombre_empresa = " Caiman Minimarket "
print(f"\nNombre empresa: {nombre_empresa}")
extension_dominio = ".com.es"
print(f"Extension dominio: {extension_dominio}")

# Quitamos espacios en blanco y convertimos a mayus

nombre_empresa_normalizado = nombre_empresa.replace(" ","").lower()#podemos poner el .lower() después pues es una función así no hay que estar haciendo nuevamente el proceso.
#Este es otro método para quitar los espacios en blanco, replazando el " " por ""
print(f"Nombre empresa normalizado: {nombre_empresa_normalizado}")
dominio_email = f"{nombre_empresa_normalizado}{extension_dominio}"
print(F"Dominio del email normalizado: {dominio_email}")
email = f"{nombre_empresa_normalizado}{extension_dominio}"
print(f"\nEmail final generado: {email}")



