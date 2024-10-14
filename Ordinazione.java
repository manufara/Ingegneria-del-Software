import Comanda

class Ordinazione:
    def __init__(self, tavolo, cameriere):
        self.tavolo = tavolo
        self.cameriere = cameriere
        self.comande = []
        self.totale = tavolo.Prenotazione.pax*2  # di base cè solo il coperto

    def aggiorna_ordinazione(self):
        self.mostra_ordinazione()
        # genera comanda da popolare
        comanda = Comanda.Comanda(self.cameriere)
        comanda.genera_comanda()
        # aggiorna ordinazione
        self.comande.append(comanda)
        self.totale += comanda.totale
        self.mostra_ordinazione()

    def mostra_ordinazione(self):
        print(f"Ordinazione per il tavolo {self.tavolo.nrTavolo}: ")
        for comanda in self.comande:
            for piatto in comanda.piatti:
                piatto.mostra_piatto()
        print(f"Totale: {self.totale} euro")