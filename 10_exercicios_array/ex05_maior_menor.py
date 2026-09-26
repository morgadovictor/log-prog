"""Construa um programa onde o usuário digitará dez números inteiros.
O programa deve identificar qual é o maior e qual é o menor número
digitado, exibindo também a posição (índice)
em que cada um deles se encontra no vetor."""

numeros = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

maior = max(numeros)
indice_maior = numeros.index(maior)

menor = min(numeros)
indice_menor = numeros.index(menor)

print(
    f"\nMaior número: {maior}\nÍndice: {indice_maior}\n",
    f"\nMenor número: {menor}\nÍndice: {indice_menor}",
)
