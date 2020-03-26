'''Leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a
sua média. A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento Conceito
Entre 9.0 e 10.0 A
Entre 7.5 e 9.0 B
Entre 6.0 e 7.5 C
Entre 4.0 e 6.0 D
Entre 4.0 e zero E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''

# ENTRADA
def main():
    nota1 = float(input('Primeira nota parcial: '))
    nota2 = float(input('Segunda nota parcial: '))
    media(nota1, nota2)

# PROCESSAMENTO
def media(n1, n2):
    m = (n1 + n2) / 2
    if 9 <= m <= 10:
        print(f'Nota 1: {n1} \nNota 2: {n2} \nMédia: {m} \nConceito: A \nAPROVADO')
    elif 7.5 <= m < 9:
        print(f'Nota 1: {n1} \nNota 2: {n2} \nMédia: {m} \nConceito: B \nAPROVADO')
    elif 6 <= m < 7.5:
        print(f'Nota 1: {n1} \nNota 2: {n2} \nMédia: {m} \nConceito: C \nAPROVADO')
    elif 4 <= m < 6:
        print(f'Nota 1: {n1} \nNota 2: {n2} \nMédia: {m} \nConceito: D \nREPROVADO')
    elif 0 <= m < 4:
        print(f'Nota 1: {n1} \nNota 2: {n2} \nMédia: {m} \nConceito: E \nREPROVADO')
    else:
        print('Valor Inválido!')

# SAÍDA
main()
