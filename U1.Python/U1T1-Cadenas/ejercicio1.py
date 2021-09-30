# Dada una cadena de longitud impar mayor que 7, devuelva 
# una nueva cadena formada por los tres caracteres del medio de una cadena determinada

# str1 = "ChemTioaDur"
# str2 = "ChQueem"

cadena = str(input("Introduce una cadena: "))

if(len(cadena)>7 & len(cadena)%2!=0):
    primeraLetra = int(len(cadena)/2-1)
    ultimaLetra = int(len(cadena)/2+2)
    cadenaMedio = cadena[primeraLetra:ultimaLetra]
    
print(cadenaMedio)

