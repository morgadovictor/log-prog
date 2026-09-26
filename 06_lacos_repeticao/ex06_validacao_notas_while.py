"""Construa um programa que só aceite notas escolares entre zero e dez
(treinamento para controle de erros).
Use While"""

notas = []
i = 0

while True:
    # 1. Captura e validação do tipo de dado
    try:
        nota = float(input(f"Digite a {i + 1}º nota: "))
    except ValueError:
        print("\nEntrada inválida! Por favor, digite apenas números.\n")
        continue  # Volta para o início do loop sem cadastrar a nota
    # 2. Validação do intervalo da nota
    if 0 <= nota <= 10:
        notas.append(nota)
        i += 1
    else:
        print("\nA nota digitada não está entre 0 e 10.")
    # 3. Confirmação para continuar
    continuar = input("\nDeseja inserir mais notas? (S/N)").strip().lower()
    while continuar not in ["s", "n"]:
        continuar = (
            input("\nOpção inválida. Digite 'S' para Sim ou 'N' para Não: ")
            .strip()
            .lower()
        )
    if continuar == "n":
        break

print(f"\n{len(notas)} nota(s) escolare(s) inserida(s).\n")

for nota in notas:
    print(nota)
