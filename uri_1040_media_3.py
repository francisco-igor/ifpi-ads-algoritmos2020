def main():
    n1, n2, n3, n4 = input().split(' ')
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    n4 = float(n4)
    notas(n1, n2, n3, n4)

def notas(n1, n2, n3, n4):
    media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / (2 + 3 + 4 + 1)
    print('Media: {:.1f}'.format(media))

    if media >= 7:
        print('Aluno aprovado.')
    elif media < 5:
        print('Aluno reprovado.')
    else:
        print('Aluno em exame.')
        nota = float(input())
        print('Nota do exame: {}'.format(nota))
        media_final = (nota + media) / 2
    
        if media_final >= 5:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(media_final))

main()
