import pickle
from Tavolo import crea_tavoli
from Cameriere import Cameriere
from datetime import date, timedelta


class Database:
    def __init__(self):
        self.data_inizio = date(2025, 6, 1)
        self.data_fine = date(2025, 9, 30)
        self.dati_prenotazioni = {}
        self.dati_tavoli = {}

        # Gestione del personale
        c1 = Cameriere("c1")
        c2 = Cameriere("c2")
        c3 = Cameriere("c3")
        self.lista_camerieri = [c1, c2, c3]

    def crea_database(self):
        data_corrente = self.data_inizio
        while data_corrente <= self.data_fine:
            self.dati_prenotazioni[data_corrente] = {
                "pranzo": [],
                "cena": []
            }
            self.dati_tavoli[data_corrente] = {
                "pranzo": crea_tavoli(),
                "cena": crea_tavoli()
            }
            data_corrente += timedelta(days=1)

    def carica_dati(self):
        # Carica la lista delle prenotazioni dal file pickle
        try:
            with open("../Progetto/elenco_prenotazioni.pkl", "rb") as file:
                self.dati_prenotazioni, self.dati_tavoli = pickle.load(file)
        except FileNotFoundError:
            self.crea_database()
            return
            
    def salva_dati(self):
        with open("../Progetto/elenco_prenotazioni.pkl", "wb") as file:
            pickle.dump((self.dati_prenotazioni, self.dati_tavoli), file)


database = Database()
