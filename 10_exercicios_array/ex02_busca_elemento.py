"""Construa um programa que peça ao usuário para digitar oito números
e os guarde em um vetor. Depois, o programa deve pedir um número adicional
e informar se esse número está presente no vetor. Se estiver, informe
em qual posição (índice) ele foi encontrado pela primeira vez."""

numeros = []

for i in range(3):
    # Laço para pedir oito números ao usuário e os guardar em um vetor.
    numeros.append(float(input(f"Digite o {i + 1}º número: ")))

numero_adicional = float(input(f"\nAgora digite o {i + 2}º número: "))

if numero_adicional in numeros:
    print(
        f"\nO número {numero_adicional} foi encontrado",
        f"na {numeros.index(numero_adicional) + 1}º posição.",
    )
else:
    print(f"\nO número {numero_adicional} não foi encontrado na lista.")
