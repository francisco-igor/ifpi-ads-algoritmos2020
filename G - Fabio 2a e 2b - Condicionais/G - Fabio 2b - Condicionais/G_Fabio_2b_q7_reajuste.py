'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
contrataram para desenvolver o programa que calculará os reajustes. Escreva um algoritmo que leia o
salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
o salários até R$ 280,00 (incluindo) : aumento de 20%
o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
· o salário antes do reajuste;
· o percentual de aumento aplicado;
· o valor do aumento;
· o novo salário, após o aumento.'''

# ENTRADA
def main():
    salario = float(input('Qual o seu salário atual? R$ '))
    print('-' * 33)
    reajuste(salario)

# PROCESSAMENTO
def reajuste(s):
    if 0 < s <= 280:
        a = (s * 20) / 100
        st = s + a
        print(f'Salário atual: R$ {s:.2f} \nPercentual de aumento: 20% \nValor do reajuste: R$ {a:.2f} \nNovo salário: R$ {st:.2f}')
    elif 280 < s <= 700:
        a = (s * 15) / 100
        st = s + a
        print(f'Salário atual: R$ {s:.2f} \nPercentual de aumento: 15% \nValor do reajuste: R$ {a:.2f} \nNovo salário: R$ {st:.2f}')
    elif 700 < s <= 1500:
        a = (s * 10) / 100
        st = s + a
        print(f'Salário atual: R$ {s:.2f} \nPercentual de aumento: 10% \nValor do reajuste: R$ {a:.2f} \nNovo salário: R$ {st:.2f}')
    elif s > 1500:
        a = (s * 5) / 100
        st = s + a
        print(f'Salário atual: R$ {s:.2f} \nPercentual de aumento: 5% \nValor do reajuste: R$ {a:.2f} \nNovo salário: R$ {st:.2f}')

# SAÍDA
main()
