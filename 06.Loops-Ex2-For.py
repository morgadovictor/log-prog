"""Construa um programa que o usuário digitará um número e a aplicação
completará o número digitado até completar cem.
Use For"""

numero = int(input("Digite um número entre 0 e 100: "))

if 0 <= numero <= 100:
    for i in range(numero, 101):
        print(i)
