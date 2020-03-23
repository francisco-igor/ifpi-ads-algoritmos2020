'''Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva
se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180o). Se formam,
verifique se formam um triângulo acutângulo (3 ângulos < 90o), retângulo (1 ângulo = 90o) ou
obtusângulo (1 ângulo > 90o). Não existe ângulo com tamanho 0o (zero grau).'''

# ENTRADA
ang1 = int(input('Digite um ângulo: '))
ang2 = int(input('Digite outro ângulo: '))
ang3 = int(input('Digite mais um ângulo: '))

# PROCESSAMENTO
if ang1 == 0 or ang2 == 0 or ang3 == 0:
    print('Não existe ângulo de 0º.')

elif ang1 + ang2 + ang3 != 180:
    print('As medidas escolhidas não formam um triângulo.')

elif ang1 < 90 and ang2 < 90 and ang3 < 90:
    print('As medidas escolhidas formam um triângulo acutângulo.')

elif ang1 == 90 or ang2 == 90 or ang3 == 90:
    print('As medidas escolhidas formam um triângulo retângulo.')

elif ang1 > 90 or ang2 > 90 or ang3 > 90:
    print('As medidas escolhidas formam um triângulo obtusângulo.')
