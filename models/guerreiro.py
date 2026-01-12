from models.personagem import Personagem
import random
import time

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=100, ataque=20, defesa=15)

    def atacar(self, outro):
        dano = self._ataque - outro._defesa
        if dano < 0:
            dano = 0
        dano = random.randint(int(dano*0.8), int(dano*1.2))
        time.sleep(1)
        print(f'{self._nome} ataca {outro._nome} e causa {dano} de dano!')
        print()
        outro.receber_dano(dano)