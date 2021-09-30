# Dadas dos cadenas, s1 y s2, cree una nueva cadena agregando s2 en medio de s1

# Dado :
# s1 = "Hola"
# s2 = "Adios"

# Resultado:
# HoAdiosla

s1 = "Hola"
s2 = "Adios"

primera = s1[:len(s1)//2]
segunda = s1[len(s1)//2:]

union = primera+s2+segunda
print(union)