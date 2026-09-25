"""Construa um jogo de pedra, papel e tesoura.
VS jogador"""

jogador1 = input("Jogador 1 - Escolha: pedra, papel ou tesoura? ").lower()
jogador2 = input("Jogador 2 - Escolha: pedra, papel ou tesoura? ").lower()

if jogador1 == jogador2:
    print("\nE é um empate senhores.")
elif (
    jogador1 == "pedra"
    and jogador2 == "tesoura"
    or jogador1 == "papel"
    and jogador2 == "pedra"
    or jogador1 == "tesoura"
    and jogador2 == "papel"
):
    print("\nO player 01 venceu!")
elif (
    jogador1 == "pedra"
    and jogador2 == "papel"
    or jogador1 == "papel"
    and jogador2 == "tesoura"
    or jogador1 == "tesoura"
    and jogador2 == "pedra"
):
    print("\nO player 02 venceu!")
