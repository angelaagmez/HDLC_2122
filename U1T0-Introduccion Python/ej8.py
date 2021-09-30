# Calcula la multiplicación y la suma de dos números. Dados dos números enteros, 
# devuelve su producto sólo si el producto es mayor que 1000, de lo contrario, 
# devuelve su suma.

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

mult = num1*num2

if(mult>1000):
    print("El producto de la multiplicación es: ",mult)
else:
    suma = num1+num2
    print("El resultado de la suma es: ",suma)