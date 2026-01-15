import time
from methods.batalha import batalhar
from methods.nome_personagem import definir_personagem, definir_inimigo


def pvp():
    heroi1 = definir_personagem("Jogador 1")
    heroi2 = definir_personagem("Jogador 2")
    return heroi1, heroi2

def pve():
    heroi = definir_personagem("Jogador")
    inimigo = definir_inimigo()
    return heroi, inimigo

print("1 - Jogador vs Computador")
print("2 - Jogador vs Jogador")

modo = input("Escolha: ")

if modo == "1":

    heroi, inimigo = pve()

    while True:

        batalhar(heroi, inimigo)
        time.sleep(1)
        continuar = input("\n Quer tentar de novo?: ").lower()

        if continuar.startswith("s"):
            heroi, inimigo = pve()
            continue

        else:
            print("Encerrando o programa")
            time.sleep(1)
            break

elif modo == "2":
    
    heroi1, heroi2 = pvp()

    while True:

        batalhar(heroi1, heroi2)
        time.sleep(1)
        continuar = input("\n Quer tentar de novo?: ").lower()

        if continuar.startswith("s"):
            heroi1, heroi2 = pvp()
            continue

        else:
            print("Encerrando o programa")
            time.sleep(1)
            break

else:
    print("Opção inválida")

