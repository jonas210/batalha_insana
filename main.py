import time
from methods.batalha import batalhar
from methods.nome_personagem import definir_personagem


heroi1 = definir_personagem("Jogador 1")
heroi2 = definir_personagem("Jogador 2")

while True:
    batalhar(heroi1, heroi2)
    time.sleep(1)
    continuar = input("Quer tentar de novo?: ").lower()

    if continuar.startswith("s") and continuar.isalpha():
        continue

    else:
        print("Encerrando o programa")
        break
