'''Leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda etc.), se digitar outro
valor deve aparecer valor inválido.'''

# ENTRADA
def main():
    dia = int(input('Digite um número de 1 a 7: '))
    day(dia)

# PROCESSAMENTO
def day(d):
    if 0 < d < 7:
        if d == 1:
            print('Domingo')
        elif d == 2:
            print('Segunda')
        elif d == 3:
            print('Terça')
        elif d == 4:
            print('Quarta')
        elif d == 5:
            print('Quinta')
        elif d == 6:
            print('Sexta')
        elif d == 7:
            print('Sábado')
    else:
        print('Valor Inválido!')

# SAÍDA
main()
