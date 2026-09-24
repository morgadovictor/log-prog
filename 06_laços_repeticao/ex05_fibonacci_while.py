"""Construa um programa que exiba a sequência de Fibonacci de zero até dois
mil.
Use While"""

anterior = 0  # Número anterior
atual = 1  # Número atual

print(anterior)

while atual <= 2000:
    print(atual)
    anterior, atual = atual, anterior + atual
