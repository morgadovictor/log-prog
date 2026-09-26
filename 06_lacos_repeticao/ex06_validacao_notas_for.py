"""Construa um programa que só aceite notas escolares entre zero e dez
(treinamento para controle de erros).
Use For"""

notas = []
# 1. Pergunta quantas notas serão inseridas
# (garante que seja um número inteiro positivo)
while True:
    try:
        qtd_notas = int(input("Quantas notas deseja inserir: "))
    except ValueError:
        print("\nEntrada inválida! Por favor, digite apenas números.\n")
        continue
    if qtd_notas > 0:
        break
# 2. O FOR define a quantidade exata de notas que precisam ser cadastradas
for i in range(qtd_notas):
    # O WHILE garante que o programa insista
    # até receber uma nota válida para a posição 'i'
    while True:
        # 1. Captura e validação do tipo de dado
        try:
            nota = float(input(f"Digite a {i + 1}º nota: "))
        except ValueError:
            print("\nEntrada inválida! Por favor, digite apenas números.\n")
            continue  # Volta para o início do WHILE (mesma nota)
        # 2. Validação do intervalo da nota
        if 0 <= nota <= 10:
            notas.append(nota)
            break  # Sair do WHILE e avançar para o próximo 'i' do FOR
        else:
            print("\nA nota digitada não está entre 0 e 10.")
            # O WHILE se repete até o usuário digitar uma nota válida

print(f"\n{len(notas)} nota(s) escolare(s) inserida(s).\n")

for nota in notas:
    print(nota)
