'''Leia 2 (duas) notas parciais de um aluno, calcule a média e escreva a mensagem:
o "Aprovado", se a média alcançada for maior ou igual a sete;
o "Reprovado", se a média for menor do que sete;
o "Aprovado com Distinção", se a média for igual a dez.'''

# ENTRADA
def main():
    nota1 = float(input('Primeira nota parcial: '))
    nota2 = float(input('Segunda nota parcial: '))
    
    media_arit(nota1, nota2)

# PROCESSAMENTO
def media_arit(nota1, nota2):
    
    media = (nota1 + nota2) / 2
    
    if media > 10:
        print('Valor excedido.')
    elif media == 10:
        print('Aprovado com Distinção!')
    elif media >= 7:
        print('Aprovado!')
    else:
        print('Reprovado!')

# SAÍDA
main()
