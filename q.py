from random import shuffle


def guloso(sequencia):
    subsequencia = []
    ultimo_valor = 0  # serão utilzadas sequências com valores positivo e não nulos
    for valor in sequencia:
        if valor > ultimo_valor:
            ultimo_valor = valor
            subsequencia.append(valor)
    return subsequencia


'''
SSCTF-Max-Rec (A, n)
    c ← 1
    para  i ← n−1  decrescendo até 1  faça
        se  A[i] ≤ A[n]
            então  d ← SSCTF-Max-Rec (A, i)
                se  d+1 > c  então  c ← d+1
    devolva  c
'''


def recursiva(sequencia, n):
    c = 1
    for i in list(range(n - 1))[::-1]:
        if sequencia[i] <= sequencia[n]:
            d = recursiva(sequencia, i)
            if d + 1 > c:
                c = d + 1
    return c


# TODO mentir no relatório que primeiro acho o tamanho da sequencia e depois conseguiu a sequencia
def dinamico(sequencia):
    subsequencia = [float('inf')]
    for valor in sequencia:
        if valor >= subsequencia[-1]:
            subsequencia.append(valor)
        else:
            if len(subsequencia) == 1:
                subsequencia[-1] = valor
            elif len(subsequencia) > 1 and subsequencia[-2] <= valor:
                subsequencia[-1] = valor

    return subsequencia


sequencia_aleatoria = list(range(1, 21))
shuffle(sequencia_aleatoria)

print('sequencia_aleatoria')
print(sequencia_aleatoria)
print()

print('guloso')
print(guloso(sequencia_aleatoria))
print()

print('dinamico')
print(dinamico(sequencia_aleatoria))

# print(recursiva(sequencia_aleatoria, len(sequencia_aleatoria)))
