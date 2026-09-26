"""Construa um programa onde o usuário digitará o nome e a média de dez
alunos e o programa escreverá, na tela, o nome de todos com a média acima
ou igual a seis."""

alunos = []

for i in range(10):
    alunos.append(
        [
            input(f"Digite o nome do {i + 1}º aluno: "),
            float(input(f"Digite a média do {i + 1}º aluno: ")),
        ]
    )
    print()

for aluno in alunos:
    if aluno[1] >= 6:
        print(aluno[0])
