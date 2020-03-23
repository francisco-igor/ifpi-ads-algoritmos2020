'''Determine a idade de uma pessoa, em anos, meses e dias, dadas a data (dia, mês e ano) do seu
nascimento e a data (dia, mês e ano) atual.'''

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
        
        
        print(f'Sua idade atual exata é de {anos} anos, {meses} meses e {dias} dias.')
        
# SAÍDA
main()
