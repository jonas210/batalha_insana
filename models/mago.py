from models.personagem import Personagem
import random
import time

class Mago(Personagem):
    VIDA = 70
    ATAQUE = 25
    DEFESA = 5
    MANA_MAX = 15

    def __init__(self, nome):
        super().__init__(nome, self.VIDA, self.ATAQUE, self.DEFESA, self.MANA_MAX)
        self._mana = self.MANA_MAX


    def magia(self, outro):
        if self._mana < 5:
            print(f'{self._nome} tentou conjurar uma magia, mas estava sem mana!')
            return

        self._mana -= 5
        dano_base = max(10, self._ataque - outro._defesa)
        dano = random.randint(int(dano_base*1.6), int(dano_base*2.0))
        print(f'{self._nome} conjurou uma bola de fogo gigante e causou {dano} de dano!')
        time.sleep(1)
        print(f'{self._nome} gastou 5 de mana!')
        print(f'Mana: {self._mana}')
        time.sleep(1)
        outro.receber_dano(dano)

    def receber_dano(self, valor):
        if self._defendendo:
            valor = int(valor * 0.6)
            self._defendendo = False
            print(f'{self._nome} criou uma barreira mágica!')
            time.sleep(1)

        super().receber_dano(valor)



