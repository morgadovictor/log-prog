"""Construa um programa onde o usuário digitará seis notas (números reais).
O programa deve calcular a média dessas notas e, em seguida, exibir quantas
e quais notas ficaram estritamente acima da média calculada."""

notas = []

for i in range(6):
    notas.append(float(input(f"Digite a {i + 1}º nota: ")))

media = sum(notas) / len(notas)
print(f"\nMédia: {media:.2f}")
acima_media = [nota for nota in notas if nota > media]
print(f"Quantidade de notas acima da média: {len(acima_media)}\n")

for nota in acima_media:
    print(nota)
