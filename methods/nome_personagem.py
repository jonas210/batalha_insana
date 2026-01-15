from models.personagem import Personagem
from models.guerreiro import Guerreiro
from models.mago import Mago
import time
import random

def definir_personagem(jogador):
    print(f'\n Criando o heroi de {jogador}')
    time.sleep(1)
    while True:
        heroi = input("Digite o nome do seu heroi: ").strip()
        if heroi.replace(" ", "").isalpha():
            break
        else:
            print("Digite um nome válido, apenas letras sao suportadas.")

    while True:
        print(f'\n Escolha uma classe')
        time.sleep(1)
        print(f"1 - Guerreiro (Vida: {Guerreiro.VIDA}, Ataque: {Guerreiro.ATAQUE}, Defesa: {Guerreiro.DEFESA}, Mana: {Guerreiro.MANA_MAX})")
        print(f"2 - Mago (Vida: {Mago.VIDA}, Ataque: {Mago.ATAQUE}, Defesa: {Mago.DEFESA}, Mana: {Mago.MANA_MAX})")
        time.sleep(1)
        escolha = input("Digite 1 ou 2: ")

        if escolha == "1":
            return Guerreiro(heroi)
        
        elif escolha == '2':
            return Mago(heroi)
        
        else:
            print("Opção invalida, tente novamente")


def definir_inimigo():
    inimigos = [
        Guerreiro("Orc"),
        Mago("Feiticeiro Sombrio")
    ]
    return random.choice(inimigos)



