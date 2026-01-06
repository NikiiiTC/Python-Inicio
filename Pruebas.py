texto = "  eeeee queme esptas contaniner      "
print(texto)
print(texto.strip())


texto = " eeee Que me Estás ContaIner  "
print(texto)
print(texto.strip().upper().replace(" ",".").lower())
print(texto.strip()).lower()
texto_normalizado = texto.strip().replace(" ","").lower()
print(texto_normalizado)