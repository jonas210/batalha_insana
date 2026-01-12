from models.personagem import Personagem
import random

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=70, ataque=25, defesa=5)


    def atacar(self, outro):
        dano = self._ataque - outro._defesa
        if dano < 0:
            dano = 0
        dano = random.randint(int(dano*0.8), int(dano*1.2))
        print(f'{self._nome} ataca {outro._nome} e causa {dano} de dano!')
        print()
        outro.receber_dano(dano)