from random import shuffle


def guloso(sequencia):
    subsequencia = []
    ultimo_valor = 0  # somente sequências com valores positivo e não nulos
    for valor in sequencia:
        if valor > ultimo_valor:
            ultimo_valor = valor
            subsequencia.append(valor)
    return subsequencia


# Tentativa de fazer dinamico
# Melhor que a função gulosa
# Não garante o ótimo
# Falha com [4,5,1,2,3]
# Retorna [4,5]
# Ótimo [1,2,3]
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


# Melhor que o anterior
# Ainda não garante o ótimo
# Falha com [19, 1, 17, 18, 2, 15, 16, 3, 13, 14, 4]
def dinamico2(sequencia):
    subsequencia = []
    for i in range(len(sequencia)):
        if len(dinamico(sequencia[i:])) > len(subsequencia):
            subsequencia = dinamico(sequencia[i:])
    return subsequencia


# Garante o ótimo
# Usa memoização
def otimo(indice):
    if indice in cache_otimo.keys():
        return cache_otimo[indice]
    valor_no_indice = sequencia_aleatoria[indice]
    subsequencia = []
    maior = float('inf')
    if indice < len(sequencia_aleatoria):
        for indice_proximo, proximo in enumerate(sequencia_aleatoria[indice + 1:], start=indice + 1):
            if maior > proximo >= valor_no_indice:
                maior = proximo
                subsequencia = max([subsequencia, otimo(indice_proximo)], key=lambda x: len(x))
    cache_otimo[indice] = [valor_no_indice] + subsequencia
    return cache_otimo[indice]


# segunda iteração
# simplificada
# busca o resultado ótimo percorrendo a sequencia em ordem inversa
def otimo2(sequencia):
    otimos = dict()
    n = len(sequencia) - 1
    while n >= 0:
        valor = sequencia[n]
        subsequencia = [valor]
        for subsequencia_parcial in otimos.values():
            if valor < subsequencia_parcial[0]:
                subsequencia = max([subsequencia, [valor] + subsequencia_parcial], key=lambda x: len(x))
        otimos[n] = subsequencia
        n -= 1
    return max(otimos.values(), key=lambda x: len(x))


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
print()

print('dinamico2')
print(dinamico2(sequencia_aleatoria))
print()

print('otimo')
cache_otimo = dict()
for index in range(len(sequencia_aleatoria)):
    otimo(index)
print(max(cache_otimo.values(), key=lambda x: len(x)))
print()

print('otimo2')
print(otimo2(sequencia_aleatoria))
print()

sequencia_aleatoria = [19, 1, 17, 18, 2, 15, 16, 3, 13, 14, 4]
print(guloso(sequencia_aleatoria))
print(dinamico(sequencia_aleatoria))
print(dinamico2(sequencia_aleatoria))
cache_otimo = dict()
for index in range(len(sequencia_aleatoria)):
    otimo(index)
print(max(cache_otimo.values(), key=lambda x: len(x)))
print(otimo2(sequencia_aleatoria))
