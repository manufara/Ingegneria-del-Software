import Comanda

class Ordinazione:
    def __init__(self, tavolo, cameriere):
        self.tavolo = tavolo
        self.cameriere = cameriere
        self.comande = []
        self.totale = tavolo.Prenotazione.pax*2  # di base cè solo il coperto

    def aggiornaOrdinazione(self):
        self.mostra_ordinazione()
        comanda = Comanda.Comanda(self.cameriere)
        comanda.generaComanda()
        self.comande.append(comanda)
        self.totale += comanda.totale
        self.mostra_ordinazione()

    def mostra_ordinazione(self):
        print(f"Ordinazione per il tavolo {self.tavolo.nrTavolo}: ")
        for comanda in self.comande:
            for piatto in comanda.piatti:
                piatto.mostraPiatto()
        print(f"Totale: {self.totale} euro")