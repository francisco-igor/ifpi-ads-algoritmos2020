'''Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) de uma pessoa, calcule e escreva
sua idade exata (em anos).'''

# ENTRADA
def main():
    dia1 = int(input('Que dia é hoje? '))
    mes1 = int(input('Que mês é este? '))
    ano1 = int(input('Em que ano estamos? '))

    dia2 = int(input('Digite o dia do nascimento: '))
    mes2 = int(input('Digite o mês do nascimento: '))
    ano2 = int(input('Digite o ano do nascimento: '))
    idade(dia1, mes1, ano1, dia2, mes2, ano2)

# PROCESSAMENTO
def idade(dia1, mes1, ano1, dia2, mes2, ano2):
    if 0 < dia1 <= 31 and 0 < dia2 <= 31 and 0 < mes1 <= 12 and 0 < mes2 <= 12 and 0 < ano1 and 0 < ano2:
        dias_total1 = ano1 * 365 + mes1 * 30 + dia1
        dias_total2 = ano2 * 365 + mes2 * 30 + dia2
        idade = (dias_total1 - dias_total2) // 365
        print(f'Sua idade atual é de {idade} anos.')
    else:
        print('Data inválida.')

# SAÍDA
main()
