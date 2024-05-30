# classe jogador
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def receber_carta(self, carta):
        self.mao.append(carta)

    def mostrar_mao(self):
        return ', '.join(map(str, self.mao))

    def distribuir_cartas(jogadores, baralho, num_cartas=2):
        for _ in range(num_cartas):
            for jogador in jogadores:
                jogador.receber_carta(baralho.distribuir())

