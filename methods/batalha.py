
import time



def batalhar(personagem1, personagem2):
    print(personagem1)
    print(personagem2)
    print()
    time.sleep(1)

    while personagem1.esta_vivo() and personagem2.esta_vivo():
        personagem1.atacar(personagem2)
        time.sleep(2)
        if not personagem2.esta_vivo():
            print(f'\n {personagem2._nome} foi derrotado! {personagem1._nome} foi o vencedor.')
            break
        personagem2.atacar(personagem1)
        time.sleep(2)
        if not personagem1.esta_vivo():
            print(f'\n {personagem1._nome} foi derrotado! {personagem2._nome} foi o vencedor.')
            break
        print()
        time.sleep(1)
