#classe baralho
from carta import Carta
class Baralho:
    def __init__(self):
        self.cartas = [Carta(naipe, valor) for naipe in Carta.naipes for valor in Carta.valores]
        random.shuffle(self.cartas)
        
    
    def distribuir(self):
        return self.cartas.pop()
    
    def distribuir_cartas(jogadores, baralho, num_cartas=2):
        for _ in range(num_cartas):
            for jogador in jogadores:
                jogador.receber_carta(baralho.distribuir())
    
