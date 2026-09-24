"""Construa um programa onde o usuário digitará um número e o programa
completará o número digitado até 0, apenas com números pares.
Use While"""

numero = int(input("Digite um número menor que 0: "))

if numero > 0:
    print("\nO número digitado é maior do que 0.")
    exit()

if numero % 2 != 0:
    numero += 1

while numero <= 0:
    print(numero)
    numero += 2
