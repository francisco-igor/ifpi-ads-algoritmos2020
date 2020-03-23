'''Leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais
recente.'''

# ENTRADA
def main():
    dia1 = int(input('Um dia: '))
    mes1 = int(input('Um mês: '))
    ano1 = int(input('Um ano: '))

    dia2 = int(input('Outro dia: '))
    mes2 = int(input('Outro mês: '))
    ano2 = int(input('Outro ano: '))

    recente(dia1, mes1, ano1, dia2, mes2, ano2)

# PROCESSAMENTO
def recente(dia1, mes1, ano1, dia2, mes2, ano2):
    if ano1 > ano2:
        print(f'A data primeira é mais recente.')
    elif ano2 > ano1:
        print(f'A data segunda é mais recente.')

    elif mes1 > mes2:
        print(f'A data primeira é mais recente.')
    elif mes2 > mes1:
        print(f'A data segunda é mais recente.')

    elif dia1 > dia2:
        print(f'A data primeira é mais recente.')
    elif dia2 > dia1:
        print(f'A data segunda é mais recente.')
    else:
        print('As datas são iguais.')

# SAÍDA
main()
