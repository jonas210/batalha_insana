import random
import time

def opcao(personagem):
    acoes = {
        "1": personagem.atacar,
        "2": personagem.defender,
        "3": personagem.magia
    }

    while True:
        print("[1] - ATACAR"), print("[2] - DEFENDER"), print("[3] - MAGIA")
        escolha = input("Escolha: ")
        if escolha in acoes:
            return acoes[escolha]
        print("Opção inválida")


def bot_opcao(personagem):
    acoes = [
        personagem.atacar,
        personagem.defender,
        personagem.magia
    ]
    
    return random.choice(acoes)



def batalhar(personagem1, personagem2):
    print(personagem1)
    print(personagem2)
    print()
    time.sleep(1)
    
    print("Começou a batalha! Escolha uma opção!")
    while personagem1.esta_vivo() and personagem2.esta_vivo():
    
        acao = opcao(personagem1)
        acao(personagem2)

        if not personagem2.esta_vivo():
            print(f'\n {personagem2.get_nome()} foi derrotado! {personagem1.get_nome()} foi o vencedor.')
            break

        acao = bot_opcao(personagem2)
        acao(personagem1)

        time.sleep(1)
        if not personagem1.esta_vivo():
            print(f'\n {personagem1.get_nome()} foi derrotado! {personagem2.get_nome()} foi o vencedor.')
            break
        time.sleep(1)
