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