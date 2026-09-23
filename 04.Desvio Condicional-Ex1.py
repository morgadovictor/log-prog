"""Construa um programa onde o usuário digitará duas notas escolares e o
programa irá calcular a média e, caso seja menor que 6, exibirá na tela:
“Aluno Reprovado”. Caso seja maior ou igual a 6 exibirá na tela: “Aluno
Aprovado”."""

nota1 = float(input("Digite a primeira nota escolar: "))
nota2 = float(input("Digite a segunda nota escolar: "))

if (nota1 + nota2) / 2 < 6:
    print("\nAluno Reprovado!")
else:
    print("\nAluno Aprovado.")
