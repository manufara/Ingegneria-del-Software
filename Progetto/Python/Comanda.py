# classe comanda -----------------------------------
class Comanda:
    def __init__(self): #, cameriere
        self.piatti = []
        self.totale = 0
        self.prezzi = []

        #self.cameriere = cameriere

    def genera_comanda(self, piatto, prezzo, quantita):
        self.piatti.append((piatto, quantita))
        self.prezzi.append(prezzo)
        self.totale += prezzo * quantita
