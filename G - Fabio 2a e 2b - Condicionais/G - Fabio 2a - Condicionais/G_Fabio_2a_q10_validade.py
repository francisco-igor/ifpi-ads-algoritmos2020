'''Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.'''

# ENTRADA
def main():
    dia = int(input('Que dia você nasceu? '))
    mes = int(input('Em que mês você nasceu? '))
    ano = int(input('Em que ano você nasceu? '))
    validade(dia, mes, ano)

# PROCESSAMENTO
def validade(d, m, a):
    if m == 2 and 0 < d < 28 and 0 < a:
        print('Essa data é válida.')
    elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if 0 < d < 31 and 0 < a:
            print('Essa data é válida.')
        else:
            print('Essa data não é válida.')
    elif m == 4 or m == 6 or m == 9:
        if 0 < d < 30 and 0 < a:
            print('Essa data é válida.')
        else:
            print('Essa data não é válida.')

# SAÍDA
main()
