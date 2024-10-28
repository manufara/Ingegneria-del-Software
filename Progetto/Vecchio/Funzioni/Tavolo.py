class Tavolo:
    def __init__(self, nrTavolo):
        self.nrTavolo = nrTavolo

        self.occupato = False
        self.capacita = 4

        self.cameriere = None
        self.ordinazione = None
        self.Prenotazione = None
