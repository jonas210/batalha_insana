import random
import time

class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self._nome = nome
        self._vida = vida
        self._ataque = ataque
        self._defesa = defesa

    def atacar(self, outro):
        dano = self._ataque - outro._defesa
        if dano < 0:
            dano = 0
        dano = random.randint(int(dano*0.8), int(dano*1.2))
        time.sleep(1)
        print(f'{self._nome} ataca {outro._nome} e causa {dano} de dano!')
        outro.receber_dano(dano)

    def receber_dano(self, valor):
        self._vida -= valor
        if self._vida < 0:
            self._vida = 0
        print(f"Agora, {self._nome} tem {self._vida} pontos de vida")
        print()


    def esta_vivo(self):
        return self._vida > 0

    def __str__(self):
        tipo = type(self).__name__
        return f'{self._nome} ({tipo}) - Vida: {self._vida}, Ataque: {self._ataque}, Defesa: {self._defesa}'
        