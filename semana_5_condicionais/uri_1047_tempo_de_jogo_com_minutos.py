def main():
    hi, mi, hf, mf = input().split()
    hi = int(hi)
    mi = int(mi)
    hf = int(hf)
    mf = int(mf)
    duracao(hi, mi, hf, mf)

def duracao(hi, mi, hf, mf):
    if hi < hf:
        h = hf - hi
        if mi < mf:
            m = mf - mi
        elif mi > mf:
            m = (60 - mi) + mf
            h = h - 1
        else:
            m = 0

    elif hi > hf:
        h = (24 - hi) + hf
        if mi < mf:
            m = mf - mi
        elif mi > mf:
            m = (60 - mi) + mf
            h = h - 1
        else:
            m = 0

    else:
        if mi < mf:
            m = mf - mi
            h = 0
        elif mi > mf:
            m = (60 - mi) + mf
            h = 23
        else:
            m = 0
            h = 24

    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h, m))

main()
