'''A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e
número de filhos. Escreva um algoritmo que leia o salário e o número de filhos de N habitantes e
escreva:
a) média de salário da população;
b) média de número de filhos;
c) percentual de pessoas com salário de até R$ 1.000,00.'''

# ENTRADA
def main():
    num = int(input('Número de habitantes: '))
    print('-' * 30)

    pesquisa(num)

# PROCESSAMENTO

def pesquisa(num):
    salario_anterior = 0
    qtd_filhos = 0
    porcentagem = 0
    contador = 1
    
    while contador <= num:
        salario = float(input('Salário do habitante: '))
        filhos = int(input('Número de filhos: '))
        print('-' * 30)

        if salario <= 1000:
            porcentagem = porcentagem + 1

        soma_salarios = salario_anterior + salario
        soma_filhos = qtd_filhos + filhos

        salario_anterior = soma_salarios
        qtd_filhos = soma_filhos

        contador = contador + 1

    media_salarios = soma_salarios / num
    media_filhos = soma_filhos // num

    percentual = porcentagem * 100 / num

    print('-' * 42)
    print(f'Média de salário da população: R$ {media_salarios:.2f}')
    print(f'Média de filhos: {media_filhos}')
    print(f'Percentual de pessoas com salário de até R$ 1000.00: {percentual:.0f} %')
    print('-' * 57)

# SAÍDA
main()
