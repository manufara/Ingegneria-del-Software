import os, random, string, pickle
from prenotazione_class import Prenotazione, CalendarPopup, creaTavoli
from PyQt5.QtCore import QDate
from PyQt5 import uic
from PyQt5.QtWidgets import *
from datetime import date, timedelta, datetime


# Classe per la finestra (crea_prenotazione) ---------------------
class CreaPrenotazione(QMainWindow):
    def __init__(self, previous_window):
        super(CreaPrenotazione, self).__init__()
        # Carica la finestra crea_prenotazione
        ui_file = os.path.join(os.path.dirname(__file__), "crea_prenotazione.ui")
        uic.loadUi(ui_file, self)

        # Memorizza la finestra precedente
        self.previous_window = previous_window
        # Crea un gruppo di pulsanti, aggiunge le checkbox al gruppo e rende il gruppo mutualmente esclusivo
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.pranzo_check)
        self.button_group.addButton(self.cena_check)
        self.button_group.setExclusive(True)

        # Collegamento del pulsante con la finestra popup
        self.findChild(QPushButton, 'calendario_but').clicked.connect(self.mostra_calendario)
        # Collega il pulsante di conferma prenotazione
        self.findChild(QPushButton, 'conferma_but').clicked.connect(self.crea_prenotazione)
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()
        self.carica_prenotazioni()  # Carica le prenotazioni all'avvio

    def open_indietro(self):
        # Mostra la finestra precedente
        self.previous_window.show()
        self.close()

    def carica_prenotazioni(self):
        global prenotazioniservizio, tavoliservizio
        try:
            with open("Progetto/elenco_prenotazioni.pkl", "rb") as file:
                prenotazioniservizio, tavoliservizio = pickle.load(file)
        except FileNotFoundError:
            # Se non esiste un file salvato, inizializza il dizionario
            self.inizializza_prenotazioni()

    def inizializza_prenotazioni(self):
        global prenotazioniservizio, tavoliservizio
        data_inizio = date(2025, 6, 1)
        data_fine = date(2025, 9, 30)
        prenotazioniservizio = {}
        tavoliservizio = {}

        data_corrente = data_inizio
        while data_corrente <= data_fine:
            prenotazioniservizio[data_corrente] = {
                "pranzo": [],
                "cena": []
            }
            tavoliservizio[data_corrente] = {
                "pranzo": creaTavoli(),
                "cena": creaTavoli()
            }
            data_corrente += timedelta(days=1)

    def mostra_calendario(self):
        self.calendario_popup = CalendarPopup(self)
        self.calendario_popup.exec_()  # Mostra il popup in modo modale

    def genera_codice_univoco(self, prenotazioni_salvate):
        codici_esistenti = set()
        
        # Estrarre i codici dalle prenotazioni salvate
        for data, servizi in prenotazioni_salvate.items():
            for servizio, lista_prenotazioni in servizi.items():
                for prenotazione in lista_prenotazioni:
                    codici_esistenti.add(prenotazione.codice)
        
        # Genera un codice finché non è univoco
        while True:
            nuovo_codice = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            if nuovo_codice not in codici_esistenti:
                return nuovo_codice

    def crea_prenotazione(self):
        nome = self.nome_line.text().strip()
        giorno = self.lineEdit_giorno.text()
        servizio = "pranzo" if self.pranzo_check.isChecked() else ("cena" if self.cena_check.isChecked() else "")
        numero_persone = self.persone_spin.value()

        # Controlla che tutti i campi siano riempiti
        if not nome or not giorno or not servizio:
            message = QMessageBox()
            message.setText("Assicurati di specificare nome, giorno e servizio.")
            message.exec()
            return

        # Converte la stringa 'giorno' in oggetto datetime.date
        giorno_selezionato = datetime.strptime(giorno, "%d/%m/%Y").date()
        # Genera un codice univoco di 6 caratteri, composto da lettere maiuscole e cifre
        codice = self.genera_codice_univoco(prenotazioniservizio)
        
        # Verifica che il giorno selezionato esista nel dizionario
        # (non necessario perché il calendario permette di selezionare solo date valide)
        try:
            tavoli_disponibili = tavoliservizio[giorno_selezionato][servizio]
        except KeyError:
            message = QMessageBox()
            message.setText("Assicurati di selezionare un giorno valido.")
            message.exec()
            return

        tavoli_assegnati = []
        persone_da_sistemare = numero_persone

        for tavolo in tavoli_disponibili:
            if not tavolo.occupato:
                tavolo.occupato = True
                tavolo.prenotazione = codice # Collega il tavolo alla prenotazione tramite il codice
                tavoli_assegnati.append(tavolo)
                persone_da_sistemare -= tavolo.capacita
                if persone_da_sistemare <= 0:
                    break

        if persone_da_sistemare > 0:
            message = QMessageBox()
            message.setText("Non ci sono abbastanza tavoli disponibili per la tua prenotazione.")
            message.exec()

        # Crea l'oggetto prenotazione e salvalo
        prenotazione = Prenotazione(nome, giorno_selezionato, servizio, numero_persone, codice, tavoli_assegnati)
        prenotazioniservizio[giorno_selezionato][servizio].append(prenotazione)
        self.salva_prenotazioni()

        # Conferma della prenotazione
        message = QMessageBox()
        message.setText(f"Prenotazione confermata per {nome} il {giorno} a {servizio}. \nCodice: {prenotazione.codice}")
        message.exec()

    def calcola_tavoli_necessari(self, numero_persone):
        # Ogni tavolo può ospitare fino a 4 persone
        if numero_persone <= 4:
            return 1
        elif numero_persone <= 8:
            return 2
        else:
            return 3

    def converti_giorno_in_data(self, giorno):
        # Ottieni la data selezionata dal calendario e convertila in datetime.date
        data_selezionata = QDate.fromString(giorno, 'dd/MM/yyyy')
        return data_selezionata.toPyDate()  # Converte in datetime.date
    
    def salva_prenotazioni(self):
        global prenotazioniservizio, tavoliservizio
        with open("Progetto/elenco_prenotazioni.pkl", "wb") as file:
            pickle.dump((prenotazioniservizio, tavoliservizio), file)
