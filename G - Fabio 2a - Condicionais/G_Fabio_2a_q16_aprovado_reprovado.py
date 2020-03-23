'''Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas for maior
ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcule a média
final. Se esta média for maior ou igual a 5,0, o programa deve escreva “Aprovado”, caso contrário deve
escreva “Reprovado. Escreva um algoritmo para ler um número e verificar se ele obedece a esta característica.”.'''

# ENTRADA
def main():
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    calcular_nota(nota1, nota2)

# PROCESSAMENTO
def calcular_nota(nota1, nota2):
    if (nota1 + nota2) / 2 >= 7.0:
        print('Aprovado!')
    else:
        print('Não foi aprovado! Compareça ao Exame Final.')
        nota_final = float(input('Nota final: '))
    if (nota_final + ((nota1 + nota2) / 2)) / 2 >= 5.0:
        print('Aprovado!')
    else:
        print('Reprovado!')

# SAÍDA
main()
