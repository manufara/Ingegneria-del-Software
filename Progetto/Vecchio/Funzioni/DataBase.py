from datetime import date, timedelta
import time
import Cameriere
import Tavolo
import pickle
import Menu


class DataBase:
    # struttura del DataBase: Due dizionari
    def __init__(self):
        self.dati_prenotazioni = {}
        self.dati_tavoli = {}
        self.data_inizio = date(2024, 6, 1)
        self.data_fine = date(2024, 9, 30)
        self.lista_camerieri = {}
        self.menu = Menu.Menu

    # creazione dei dizionari
    def crea_database(self):
        data_corrente = self.data_inizio
        while data_corrente <= self.data_fine:
            # DB prenotazioni
            self.dati_prenotazioni[data_corrente] = {
                "pranzo": [],  # Lista per le prenotazioni di pranzo
                "cena": []     # Lista per le prenotazioni di cena
            }
            # DB tavoli
            self.dati_tavoli[data_corrente] = {
                "pranzo": [Tavolo.Tavolo(i + 1) for i in range(20)],
                "cena": [Tavolo.Tavolo(i + 1) for i in range(20)]
            }
            # Incrementa la data di un giorno
            data_corrente += timedelta(days=1)
            # gestione personale
            c1 = Cameriere.Cameriere("c1")
            c2 = Cameriere.Cameriere("c2")
            c3 = Cameriere.Cameriere("c3")
            c4 = Cameriere.Cameriere("c4")
            c5 = Cameriere.Cameriere("c5")
            self.lista_camerieri = [c1, c2, c3, c4, c5]

            # DB menu
            menu = Menu.menu


    # salvataggio dati su file DB
    def salva_dati(self, file_path):
        with open(file_path, 'wb') as file:
            # Salva i dati dei dizionari su file
            pickle.dump((self.dati_prenotazioni, self.dati_tavoli), file)

        print(f"\n---Dati salvati correttamente su {file_path}---\n")

    # recupero dati da file DB
    def carica_dati(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                # Carica i dati dal file
                self.dati_prenotazioni, self.dati_tavoli = pickle.load(file)
            print(f"Dati caricati correttamente da {file_path}")
        except FileNotFoundError:
            print(f"File {file_path} non trovato. Creazione di nuovi dati.")
            # Se il file non esiste, continua con i dati di default
            self.crea_database()

    # back up automatico
    def esegui_backup_automatico(self, file_path, intervallo_secondi):
        while True:
            # Esegue il backup
            self.salva_dati(file_path)
            # Attende per l'intervallo specificato
            time.sleep(intervallo_secondi)

# istanza di DataBase
DB = DataBase()