from models.guerreiro import Guerreiro
from models.mago import Mago
import time

def definir_personagem(jogador):
    print(f'\n Criando o heroi de {jogador}')
    heroi = input("Digite o nome do seu heroi: ")

    while True:
        print(f'\n Escolha uma classe')
        time.sleep(2)
        print("1 - Guerreiro (Vida: 100, Ataque: 20, Defesa: 10)")
        print("2 - Mago (Vida: 70, Ataque: 25, Defesa: 5)")
        time.sleep(2)
        escolha = input("Digite 1 ou 2: ")

        if escolha == "1":
            return Guerreiro(heroi)
        
        elif escolha == '2':
            return Mago(heroi)
        
        else:
            print("Opção invalida, tente novamente")


