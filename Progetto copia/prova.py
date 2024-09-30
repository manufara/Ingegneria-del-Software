# classe piatto ----------------------------------
class Piatto():
    def __init__(self, nome, descrizione, prezzo):
        self.nome = nome
        self.descrizione = descrizione
        self.prezzo = prezzo

    def mostraPiatto(self):
        return f"{self.nome}: {self.descrizione} - {self.prezzo}€"

# classe menu -------------------------------------
class MenuClass():
    def __init__(self, piatti):
        self.piatti = piatti

    def mostraMenu(self):
        print([piatto.mostraPiatto() for piatto in self.piatti])
