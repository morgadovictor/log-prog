"""Escreva um programa em Python que receba três valores numéricos reais (a,
b e c) representando os comprimentos dos lados de um triângulo.
◆ O programa deve primeiro verificar a condição de existência geométrica:
a soma de dois lados quaisquer deve ser estritamente maior que o
terceiro lado.
◆ Caso a condição seja atendida, classifique o triângulo em Equilátero,
Isósceles ou Escaleno.
◆ Se as medidas não formarem um triângulo, exiba uma mensagem de
erro."""

lado_a = float(input("Digite o lado A do triângulo: "))
lado_b = float(input("Digite o lado B do triângulo: "))
lado_c = float(input("Digite o lado C do triângulo: "))

if (
    not lado_a + lado_b > lado_c
    and lado_a + lado_c > lado_b
    and lado_b + lado_c > lado_a
    and lado_a > 0
    and lado_b > 0
    and lado_c > 0
):
    print("\nErro\nAs medidas não formam um triângulo real.")
else:
    if lado_a == lado_b == lado_c:
        print("\nTodos os lados são iguais.\nÉ um triângulo equilátero.")
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print("\nDois lados são iguais.\nÉ um triângulo isósceles.")
    else:
        print("\nTodos os lados são diferentes.\nÉ um triângulo escaleno.")
