"""Construa um programa onde o usuário digitará cinco números
para preencher um vetor. O programa deve criar um segundo vetor
que contenha os mesmos elementos do primeiro, porém na ordem inversa,
e exibir o novo vetor na tela."""

numeros = []

for i in range(5):
    numeros.append(input(f"Digite o {i + 1}º número: "))

numeros_reverso = numeros.copy()
numeros_reverso.reverse()

print(numeros_reverso)
