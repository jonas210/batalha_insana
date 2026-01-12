from models.guerreiro import Guerreiro
from models.mago import Mago
from methods.batalha import batalhar

guerreiro = Guerreiro("Jonas")
mago = Mago("Sponge")

batalhar(guerreiro, mago)