'''Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um.
Escreva na tela qual dos professores tem salário total maior.'''

# ENTRADA
def main():
    horas_aula1 = int(input('Qual a duração da aula do primeiro professor? '))
    valor1 = float(input('Qual o seu valor recebido por hora? R$ '))
    
    horas_aula2 = int(input('Qual a duração da aula do segundo professor? '))
    valor2 = float(input('Qual o seu valor recebido por hora? R$ '))
    
    salario_total(horas_aula1, valor1, horas_aula2, valor2)

# PROCESSAMENTO
def salario_total(h1, v1, h2, v2):
    h1 / 60
    h2 / 60
    if h1 * v1 > h2 * v2:
        print(f'O primeiro porfessor tem o salário total maior.')
    else:
        print(f'O segundo professor tem o salário total maior.')

# SAÍDA
main()
