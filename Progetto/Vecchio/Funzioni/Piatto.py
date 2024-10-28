class Piatto():
    def __init__(self, numero, nome, descrizione, prezzo):
        self.numero = numero
        self.nome = nome
        self.descrizione = descrizione
        self.prezzo = prezzo

    # stampa i dettagli del piatto
    def mostra_piatto(self):
        print (f"{self.numero}, {self.nome}, {self.descrizione}, {self.prezzo}")