"""Escreva um programa em Python que receba três valores numéricos reais (a,
b e c) representando os comprimentos dos lados de um triângulo.
◆ O programa deve primeiro verificar a condição de existência geométrica:
a soma de dois lados quaisquer deve ser estritamente maior que o
terceiro lado.
◆ Caso a condição seja atendida, classifique o triângulo em Equilátero,
Isósceles ou Escaleno.
◆ Se as medidas não formarem um triângulo, exiba uma mensagem de
erro."""

a = float(input("Digite o lado A do triângulo: "))
b = float(input("Digite o lado B do triângulo: "))
c = float(input("Digite o lado C do triângulo: "))
if not a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0:
    print("\nErro\nAs medidas não formam um triângulo real.")
else:
    if a == b == c:
        print("\nTodos os lados são iguais.\nÉ um triângulo equilátero.")
    elif a == b or a == c or b == c:
        print("\nDois lados são iguais.\nÉ um triângulo isósceles.")
    else:
        print("\nTodos os lados são diferentes.\nÉ um triângulo escaleno.")
