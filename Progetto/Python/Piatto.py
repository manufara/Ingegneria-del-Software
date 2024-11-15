# classe piatto -----------------------------------
class Piatto():
    def __init__(self, categoria, nome, descrizione, prezzo):
        self.categoria = categoria
        self.nome = nome
        self.descrizione = descrizione
        self.prezzo = prezzo

    def mostraPiatto(self):
        return f"{self.nome}: {self.descrizione} - {self.prezzo}€"
