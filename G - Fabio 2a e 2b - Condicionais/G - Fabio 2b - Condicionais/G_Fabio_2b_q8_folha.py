'''Para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
11% do salário bruto, mas não é descontado (é a empresa que deposita). O salário líquido corresponde
ao salário bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a
quantidade de horas trabalhadas no mês.
Desconto do IR:
o Salário Bruto até R$ 900,00 (inclusive) - isento
o Salário Bruto até R$ 1.500,00 (inclusive) - desconto de 5%
o Salário Bruto até R$ 2.500,00 (inclusive) - desconto de 10%
o Salário Bruto acima de R$ 2.500,00 - desconto de 20%
Escreva na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e
a quantidade de hora é 220.
Salário Bruto: (5 * 220) : R$ 1100,00
(-) IR (5%) : R$ 55,00
(-) INSS ( 10%) : R$ 110,00
FGTS (11%) : R$ 121,00
Total de descontos : R$ 165,00
Salário Liquido : R$ 935,00'''

# ENTRADA
def main():
    valor_hora = float(input('Quanto vale a hora de trabalho? R$ '))
    hora_mes = float(input('Quantas horas trabalhou por mês? R$ '))
    print('-'*40)
    sl(valor_hora, hora_mes)

# PROCESSAMENTO
def sl(v, h):
    if v > 0 and 0 < h <= 720:
        sb = v * h
        inss = (sb * 10) / 100
        fgts = (sb * 11) / 100
        if 0 < sb <= 900:
            ir = 0
            td = ir + inss
            slt = sb - td
            print(f'Salário Bruto: ({v:.2f} * {h:.2f}) : R$ {sb:.2f}')
            print(f'(-) IR (0%) : R$ {ir:.2f}')
            print(f'(-) INSS (10%) : R$ {inss:.2f}')
            print(f'FGTS (11%) : R$ {fgts:.2f}')
            print(f'Total de descontos : R$ {td:.2f}')
            print(f'Salário Liquido : R$ {slt:.2f}')
        elif 900 < sb <= 1500:
            ir = (sb * 5) / 100
            td = ir + inss
            slt = sb - td
            print(f'Salário Bruto: ({v:.2f} * {h:.2f}) : R$ {sb:.2f}')
            print(f'(-) IR (5%) : R$ {ir:.2f}')
            print(f'(-) INSS (10%) : R$ {inss:.2f}')
            print(f'FGTS (11%) : R$ {fgts:.2f}')
            print(f'Total de descontos : R$ {td:.2f}')
            print(f'Salário Liquido : R$ {slt:.2f}')
        elif 1500 < sb <= 2500:
            ir = (sb * 10) / 100
            td = ir + inss
            slt = sb - td
            print(f'Salário Bruto: ({v:.2f} * {h:.2f}) : R$ {sb:.2f}')
            print(f'(-) IR (10%) : R$ {ir:.2f}')
            print(f'(-) INSS (10%) : R$ {inss:.2f}')
            print(f'FGTS (11%) : R$ {fgts:.2f}')
            print(f'Total de descontos : R$ {td:.2f}')
            print(f'Salário Liquido : R$ {slt:.2f}')
        elif sb > 2500:
            ir = (sb * 20) / 100
            td = ir + inss
            slt = sb - td
            print(f'Salário Bruto: ({v:.2f} * {h:.2f}) : R$ {sb:.2f}')
            print(f'(-) IR (20%) : R$ {ir:.2f}')
            print(f'(-) INSS (10%) : R$ {inss:.2f}')
            print(f'FGTS (11%) : R$ {fgts:.2f}')
            print(f'Total de descontos : R$ {td:.2f}')
            print(f'Salário Liquido : R$ {slt:.2f}')
    elif v > 0 and h <= 0:
        print('Vai trabalhar!')
    elif v <= 0 and h > 0:
        print('Tá trabalhando de graça!')
    elif v <= 0 and h <= 0:
        print('Vai arranjar trabalho!')

# SAÍDA
main()
