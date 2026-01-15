from models.personagem import Personagem
import random
import time

class Guerreiro(Personagem):
    VIDA = 100
    ATAQUE = 10
    DEFESA = 15
    MANA_MAX = 10

    def __init__(self, nome):
        super().__init__(nome, self.VIDA, self.ATAQUE, self.DEFESA, self.MANA_MAX)
        self._mana = self.MANA_MAX

    def magia(self, outro):
        if self._mana < 5:
            print(f'{self.nome} tentou conjurar uma magia, mas estava sem mana!')
            return

        self._mana -= 5
        dano_base = max(8, self._ataque - outro._defesa)
        dano = random.randint(int(dano_base*1.2), int(dano_base*1.4))
        print(f'{self._nome} bateu com o seu escudo no chão fazendo um grande estrondo, causando {dano} de dano!')
        time.sleep(1)
        print(f'{self._nome} gastou 5 de mana!')
        print(f'Mana: {self._mana}')
        time.sleep(1)
        outro.receber_dano(dano)

    def receber_dano(self, valor):
        if self._defendendo:
            valor = int(valor * 0.3)
            self._defendendo = False
            print(f"{self._nome} ergue seu grande escudo!")
            time.sleep(1)

        super().receber_dano(valor)