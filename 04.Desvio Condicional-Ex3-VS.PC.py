"""Construa um jogo de pedra, papel e tesoura.
VS computador"""

import random

computador = random.choice(["pedra", "papel", "tesoura"])

jogador = input("Escolha: pedra, papel ou tesoura? ").lower()

if jogador == computador:
    print("\nE é um empate senhores")
elif (
    jogador == "pedra"
    and computador == "tesoura"
    or jogador == "papel"
    and computador == "pedra"
    or jogador == "tesoura"
    and computador == "papel"
):
    print("\nO jogador venceu!")
elif (
    computador == "pedra"
    and jogador == "tesoura"
    or computador == "papel"
    and jogador == "pedra"
    or computador == "tesoura"
    and jogador == "papel"
):
    print("\nO computador venceu!")
