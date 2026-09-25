"""Construa um programa que exiba a sequência de Fibonacci de zero até dois
mil.
Use For"""

anterior = 0  # Número anterior
atual = 1  # Número atual

print(anterior)

# Definimos um range generoso apenas para gerar as repetições do loop
for _ in range(2000):
    if atual > 2000:
        break  # Encerra o loop assim que passar de 2000
    print(atual)
    anterior, atual = atual, anterior + atual
