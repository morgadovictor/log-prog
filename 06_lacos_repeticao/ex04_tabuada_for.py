"""Construa um programa onde o usuário digitará um valor e o programa
mostrará, na tela, a tabuada de multiplicação deste número.
Use For"""

numero = float(input("Digite um número: "))

for i in range(11):
    print(f"{numero} * {i} = {numero*i}")
