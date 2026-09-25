"""Construa um programa onde o usuário digitará um valor e o programa
mostrará, na tela, a tabuada de multiplicação deste número.
Use While"""

numero = float(input("Digite um número: "))
i = 0

while i <= 10:
    print(f"{numero} * {i} = {numero*i}")
    i += 1
