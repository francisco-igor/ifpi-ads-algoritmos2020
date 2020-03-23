'''Leia 3 (três) números (cada número corresponde a um lado do triângulo), verifique e escreva se os 3
(três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). Se
formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou
escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero).'''

# ENTRADA
lado1 = int(input('Digite uma medida: '))
lado2 = int(input('Digite outra medida: '))
lado3 = int(input('Digite mais uma medida: '))

# PROCESSAMENTO
if lado1 == 0 or lado2 == 0 or lado3 == 0:
    print('Não existe lado com tamanho 0.')

elif lado1 + lado2 < lado3 or lado1 + lado3 < lado2 or lado2 + lado3 < lado1:
    print('A soma de dois lados não pode ser menor que o terceiro lado.')

elif lado1 == lado2 == lado3:
    print('As medidas escolhidas formam um triângulo equilátero.')

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('As medidas escolhidas formam um triângulo isósceles.')

elif lado1 != lado2 != lado3:
    print('As medidas escolhidas formam um triângulo escaleno.')
