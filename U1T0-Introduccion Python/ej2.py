# Aplicar formato a las variables mediante el método string.format(). Escriba un programa 
# para usar el método string.format() para formatear las siguientes tres variables según 
# la salida esperada.

# Dado:

# totalMoney = 1000
# quantity = 3
# price = 450

# Resultado: Tengo 1000 euros para comprar 3 tarjetas gráficas por 450,00 dólares.

totalMoney = 1000
quantity = 3
price = 450

frase = "Tengo {totalMoney} euros para comprar {quantity} tarjetas graficas por {price} dolares"

print(frase.format(totalMoney = 1000, quantity = 3, price = 450))

