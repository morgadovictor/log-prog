"""Um sistema de controle de maquinário pesado deve autorizar a operação
com base em: cargo (string: "operador" ou "supervisor"), hora_atual (inteiro
de 0 a 23) e chave_emergencia (booleano). O acesso deve ser concedido se:
◆ A chave_emergencia estiver ativa (True), independentemente de
qualquer outra variável; OU
◆ O usuário for "supervisor"; OU
◆ O usuário for "operador" E a hora_atual estiver entre 8 e 17 (inclusive).
◆ Caso contrário, o sistema deve exibir "Acesso Bloqueado"."""

import random

hora_atual = random.randint(0, 23)
chave_emergencia = random.choice([True, False])

print(f"Hora atual: {hora_atual:02d}:{random.randint(0, 59):02d}")

cargo = input("Digite o seu cargo: ").lower()

if chave_emergencia:
    print(
        "\nA chave de emegência está ativada.",
        f"\nCargo: {cargo}\nAcesso concedido.",
    )
elif cargo == "supervisor":
    print(
        "\nA chave de emergência está desativada.",
        f"\nCargo: {cargo}\nAcesso concedido.",
    )
elif cargo == "operador" and 8 <= hora_atual <= 17:
    print(
        "\nA chave de emergência está desativada.",
        f"\nCargo: {cargo}\nAcesso concedido.",
    )
else:
    print(
        "\nA chave de emergência está desativada.",
        f"\nCargo: {cargo}\nAcesso bloqueado.",
    )
