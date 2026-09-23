"""Crie um script que avalie a concessão de empréstimo com base em três
variáveis: renda_mensal (float), score (inteiro de 0 a 1000) e possui_restricao
(booleano).
◆ Aprovado: score maior ou igual a 700, renda_mensal a partir de 4000.00
e sem restrições cadastrais.
◆ Análise Manual: Se não for aprovado diretamente, mas a renda_mensal
for de pelo menos 2500.00, sem restrições, e (score maior ou igual a 500
ou renda_mensal superior a 6000.00).
◆ Recusado: Qualquer outro caso."""

import random

renda_mensal = float(input("Digte sua renda mensal: "))
score = random.randint(0, 1000)
possui_restricao = random.choice([True, False])

if possui_restricao:
    print(f"\nSeu score é {score}, e você possui restrição de crédito.")
else:
    print(f"\nSeu score é {score}, e você não possui restrição de crédito.")

if score >= 700 and renda_mensal >= 4000 and possui_restricao:
    print("\nAprovado.")
elif score >= 500 and renda_mensal >= 2500 and not possui_restricao:
    print("\nEncaminhado para a análise manual.")
else:
    print("\nRecusado.")
