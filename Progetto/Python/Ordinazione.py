# classe ordinazione ------------------------------
class Ordinazione:
    def __init__(self, tavolo):
        self.tavolo = tavolo # viene passato il tavolo come intero, uguale quindi all'attributo nrTavolo della classe Tavolo
        self.comande = []
        self.totale = 0 #inizialmente c'è il coperto -> tavolo.prenotazione.numero_persone * 2

    def aggiorna_ordinazione(self, comanda):
        self.comande.append(comanda)
        self.totale += comanda.totale

    def mostra_ordinazione(self):
        descrizione = f"Descrizione - Tavolo {self.tavolo} \n"
        for comanda in self.comande:
            cont = 0
            for piatto, quantita in comanda.piatti:
                descrizione += f"{piatto} - {quantita}x {comanda.prezzi[cont]} \n"
                cont = cont + 1
        descrizione += f"\nTotale - €{self.totale:.2f} \n"
        return descrizione
