# Dadas dos cadenas, s1 y s2 devuelven una nueva cadena compuesta por el primer, el medio y el último 
# carácter de cada cadena de entrada

# Dado :

# s1 = "Chema"
# s2 = "Duran"

# Resultado:
# CDeran

s1 = "Chema"
s2 = "Duran"

primer1 = s1[0]
medio1 = s1[int(len(s1)/2)]
ultimo1 = s1[int(len(s1)-1)]

primer2 = s2[0]
medio2 = s2[int(len(s2)/2)]
ultimo2 = s2[int(len(s2)-1)]

total = primer1+primer2+medio1+medio2+ultimo1+ultimo2

print(total)