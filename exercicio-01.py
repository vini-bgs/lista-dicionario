# Lista de números ao quadrado

numeros = list(range(1, 11))
numeros_quadrados = []

for n in numeros:
    quadrado = n ** 2
    numeros_quadrados.append(quadrado)

print(numeros_quadrados)