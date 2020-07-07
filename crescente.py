from random import shuffle


def guloso(sequencia):
    subsequencia = []
    ultimo_valor = 0  # somente sequências com valores positivo e não nulos
    for valor in sequencia:
        if valor > ultimo_valor:
            ultimo_valor = valor
            subsequencia.append(valor)
    return subsequencia


# Tentativa de usar programação dinamica
# Melhor que a função gulosa
# Não garante o ótimo
# Falha com [4,5,1,2,3]
# Retorna [4,5]
# Ótimo [1,2,3]
def nao_otimo_1(sequencia):
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
def nao_otimo_2(sequencia):
    subsequencia = []
    for i in range(len(sequencia)):
        if len(nao_otimo_1(sequencia[i:])) > len(subsequencia):
            subsequencia = nao_otimo_1(sequencia[i:])
    return subsequencia


# Garante o ótimo
# Usa memoização
def otimo_1(sequencia):
    def subf_f(indice):
        if indice in cache_otimo.keys():
            return cache_otimo[indice]
        valor_no_indice = sequencia[indice]
        subsequencia = []
        maior = float('inf')
        if indice < len(sequencia):
            for indice_proximo, proximo in enumerate(sequencia[indice + 1:], start=indice + 1):
                if maior > proximo >= valor_no_indice:
                    maior = proximo
                    subsequencia = max([subsequencia, subf_f(indice_proximo)], key=lambda x: len(x))
        cache_otimo[indice] = [valor_no_indice] + subsequencia
        return cache_otimo[indice]
    cache_otimo = dict()
    for index in range(len(sequencia)):
        subf_f(index)
    return max(cache_otimo.values(), key=lambda x: len(x))


# segunda iteração
# simplificada
# busca o resultado ótimo percorrendo a sequência em ordem inversa e obtem o ótimo para todos os indices
def otimo_2(sequencia):
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

print('nao_otimo_1')
print(nao_otimo_1(sequencia_aleatoria))
print()

print('nao_otimo_2')
print(nao_otimo_2(sequencia_aleatoria))
print()

print('otimo_1')
print(otimo_1(sequencia_aleatoria))
print()

print('otimo_2')
print(otimo_2(sequencia_aleatoria))
print()

sequencia_fixa = [19, 1, 17, 18, 2, 15, 16, 3, 13, 14, 4]
print(guloso(sequencia_fixa))
print(nao_otimo_1(sequencia_fixa))
print(nao_otimo_2(sequencia_fixa))
print(otimo_1(sequencia_fixa))
print(otimo_2(sequencia_fixa))
