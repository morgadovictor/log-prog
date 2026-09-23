"""Construa um programa que o usuário digitará um número e a aplicação
completará o número digitado até completar cem.
Use While"""

numero = int(input("Digite um número entre 0 e 100: "))

if 0 <= numero <= 100:
    while numero <= 100:
        print(numero)
        numero += 1
