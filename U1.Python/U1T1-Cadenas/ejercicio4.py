# Dada una cadena de entrada con la combinación de mayúsculas y minúsculas,organice los caracteres de 
# tal manera que todas las letras minúsculas deben ir primero.

# Dado :

# str1 = ChEmaDUraN

# Resultado:

# hmaraCEDUN

str1 = "ChEmaDUraN"
minus = ""
mayus = ""

for i in str1:
    if i.islower():
        minus = minus+i
    else:
        mayus = mayus+i

print(minus+mayus)