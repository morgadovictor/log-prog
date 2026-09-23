"""Construa um programa onde o usuário digitará três números e o programa
exibirá, na tela, o maior entre eles."""

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 >= numero2 and numero1 >= numero3:
    print(f"\n{numero1} - é o maior.")
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"\n{numero2} - é o maior.")
else:
    print(f"\n{numero3} - é o maior.")
