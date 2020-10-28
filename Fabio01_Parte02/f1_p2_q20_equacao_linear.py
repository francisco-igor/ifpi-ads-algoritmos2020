# Um sistema de equações lineares do tipo ax + by = c e dx + ey = f, pode ser resolvido segundo mostrado abaixo:
# x = ce - bf    y = af - cd
#    ---------      ---------
#     ae - bd        ae - bd
#Escreva um algoritmo que leia os coeficientes a, b, c, d, e e f, calcule e escreva os valores de x e y.

# ENTRADA
a = float(input('Leia o coeficiente a: '))
b = float(input('Leia o coeficiente b: '))
c = float(input('Leia o coeficiente c: '))
d = float(input('Leia o coeficiente d: '))
e = float(input('Leia o coeficiente e: '))
f = float(input('Leia o coeficiente f: '))

# PROCESSAMENTO
x = (c * e - b * f) / (a * e - b * d)

y = (a * f - c * d) / (a * e - b * d)


# SAÍDA
print(f'Resultado: x = {x} e y = {y}')
