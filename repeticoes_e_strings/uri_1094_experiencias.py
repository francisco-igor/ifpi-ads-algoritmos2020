def main():
    n =int(input())
    
    cont = 0
    qtd_coelhos = 0
    qtd_ratos = 0
    qtd_sapos = 0
    while cont < n:
        q, t = input().split()
        q = int(q)

        if 1 <= q <= 15:
            if t == 'C':
                qtd_coelhos = qtd_coelhos + q
            elif t == 'R':
                qtd_ratos = qtd_ratos + q
            elif t == 'S':
                qtd_sapos = qtd_sapos + q
        cont += 1

    total = qtd_coelhos + qtd_ratos + qtd_sapos
    percentual_coelhos = (qtd_coelhos * 100) / total
    percentual_ratos = (qtd_ratos * 100) / total
    percentual_sapos = (qtd_sapos * 100) / total

    print(f'Total: {total} cobaias')
    print(f'Total de coelhos: {qtd_coelhos}')
    print(f'Total de ratos: {qtd_ratos}')
    print(f'Total de sapos: {qtd_sapos}')
    print(f'Percentual de coelhos: {percentual_coelhos:.2f} %')
    print(f'Percentual de ratos: {percentual_ratos:.2f} %')
    print(f'Percentual de sapos: {percentual_sapos:.2f} %')
main()
