# Acepte tres cadenas cualquiera de una llamada input(). Escriba un programa para tomar tres 
# nombres como entrada de un usuario con una única llamada a función input().

cad1 = input("Introduce la 1º cadena: ")
cad2 = input("Introduce la 2º cadena: ")
cad3 = input("Introduce la 3º cadena: ")

print(cad1,cad2,cad3)

lista = []

for i in range(3):
    nombre = input("Introduce el nombre: ")
    lista.append(nombre)
    
print(lista)