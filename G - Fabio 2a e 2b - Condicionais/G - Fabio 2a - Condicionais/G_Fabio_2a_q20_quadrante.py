'''Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante (primeiro, segundo, terceiro ou
quarto) em que o ângulo se localiza.'''

# ENTRADA
def main():
    angulo = int(input('Digite a medida de um ângulo: '))
    quadrante(angulo)

# PROCESSAMENTO
def quadrante(angulo):
    if 0 < angulo < 360:
        if 0 < angulo <= 90:
            print('O ângulo localiza-se no primeiro quadrante.')
        elif 90 < angulo <= 180:
            print('O ângulo localiza-se no segundo quadrante.')
        elif 180 < angulo <= 270:
            print('O ângulo localiza-se no terceiro quadrante.')
        else:
            print('O ângulo localiza-se no quarto quadrante.')
    else:
        print('O medida do ângulo limita-se até 360°.')

# SAÍDA
main()
