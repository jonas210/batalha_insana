from models.personagem import Personagem
import random
import time

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=70, ataque=35, defesa=5)


    def atacar(self, outro):
        dano = self._ataque - outro._defesa
        if dano < 0:
            dano = 0
        if random.random() < 0.3:
            dano *= 2
            print(f'💥 Ataque crítico!')
        dano = random.randint(int(dano*0.8), int(dano*1.2))
        print(f'{self._nome} ataca {outro._nome} e causa {dano} de dano!')
        time.sleep(1)
        print()
        outro.receber_dano(dano)