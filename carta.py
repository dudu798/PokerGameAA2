#classe carta
class Carta:
    naipes = ['Copas', 'Ouros', 'Espadas', 'Paus']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor
    
    def __repr__(self):
        return f"{self.valor} de {self.naipe}"
