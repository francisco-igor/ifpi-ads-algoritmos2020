'''Uma determinada empresa armazena para cada funcionário uma ficha contendo o código, o número de
horas trabalhadas e o seu no de dependentes. Considerando que a empresa paga R$ 12,00 por hora e R$
40,00 por dependentes e que sobre o salário são feitos descontos de 8,5% para o INSS e 5% para IR.
Escreva um algoritmo que leia o código, número de horas trabalhadas e número de dependentes de N
funcionários. Após a leitura de cada ficha, escreva os valores descontados para cada imposto e o salário
líquido do funcionário.'''

# ENTRADA
def main():
    f = int(input('Quantidade de fichas de funcionários: '))

    fichas(f)

# PROCESSAMENTO
def fichas(f):
    contador = 1
    valor_hora = 12
    valor_por_dependente = 40

    while contador <= f:
        print('-'*100)
        c = int(input('Código do funcionário: '))
        h = int(input('Quantidade de horas trabalhadas: '))
        d = int(input('Número de dependentes: '))

        contador = contador + 1

        salario_bruto = (valor_hora * h) + (valor_por_dependente * d)

        print('-'*100)
        print(f'Código do funcionário: {c}')
        print(f'Desconto do INSS: R$ {desconto_inss(salario_bruto):.2f}')
        print(f'Desconto do IR: R$ {desconto_ir(salario_bruto):.2f}')
        print(f'Salário Líquido: R$ {salario_liquido(salario_bruto, desconto_inss(salario_bruto), desconto_ir(salario_bruto)):.2f}')
        print('-'*100)

def salario_liquido(sb, d_inss, d_ir):
    salario = sb - d_inss - d_ir 
    return salario

def desconto_inss(sb):
    inss = (sb * 8.5) / 100
    return inss

def desconto_ir(sb):
    ir = (sb * 5) / 100
    return ir

# SAÍDA
main()
