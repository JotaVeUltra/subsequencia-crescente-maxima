from random import shuffle


def guloso(sequencia):
    subsequencia = []
    ultimo_valor = 0  # serão utilzadas sequências com valores positivo e não nulos
    for valor in sequencia:
        if valor > ultimo_valor:
            ultimo_valor = valor
            subsequencia.append(valor)
    return subsequencia


# Tentativa de fazer dinamico
# Melhor que a função gulosa
# Não garante o ótimo
# Falha em [4,5,1,2,3]
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


def recursivo(sequencia):
    subsequencia = []
    for i in range(len(sequencia)):
        if len(dinamico(sequencia[i:])) > len(subsequencia):
            subsequencia = dinamico(sequencia[i:])
    return subsequencia

# solução
# para cada

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
print([4, 5, 1, 2, 3])
print('ótimo [1, 2, 3]')
print(dinamico([4, 5, 1, 2, 3]))
print()

print('recursivo')
print(recursivo(sequencia_aleatoria))
print(recursivo([4, 5, 1, 2, 3]))

print()
a = [19, 1, 17, 18, 2, 15, 16, 3, 13, 14, 4]
print(guloso(a))
print(dinamico(a))
print(recursivo(a))


cache_otimo = [list() for i in sequencia_aleatoria]
# def otimo(sequencia):
    # for index, item in enumerate(sequencia):
        # if cache_otimo[index] != []:



    #para cada valor na sequencia:
    #    para todo os valores conseguintes maires que o valor
    #        o = otimo(seg_sequencia)

sequencia_aleatoria = a

# global sequencia_aleatoria

cache_otimo = dict()
def otimo(indice):
    if indice in cache_otimo.keys():
        return cache_otimo[indice]
    print(indice)
    valor_no_indice = sequencia_aleatoria[indice]
    subsequencia = []
    maior = float('inf')
    if indice < len(sequencia_aleatoria):
        for indice_proximo, proximo in enumerate(sequencia_aleatoria[indice+1:], start=indice+1):
            if proximo < maior and proximo >= valor_no_indice:
                maior = proximo
                subsequencia = max([subsequencia, otimo(indice_proximo)], key= lambda x: len(x))
    cache_otimo[indice] = [valor_no_indice] + subsequencia
    return cache_otimo[indice]


o = []
for index in range(len(sequencia_aleatoria)):
    otimo(index)

print(max(cache_otimo.values(), key= lambda x: len(x)))
