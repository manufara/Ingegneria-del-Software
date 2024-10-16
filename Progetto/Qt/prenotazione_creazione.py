import random, string
import pickle
import os
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
        # Collega il pulsante per visualizzare le prenotazioni
        self.findChild(QPushButton, 'da_eliminare').clicked.connect(self.visualizza_prenotazioni)
        # Collega il pulsante per cancellare le prenotazioni
        self.da_eliminare_2.setGeometry(80, 380, 0, 0)
        # self.findChild(QPushButton, 'da_eliminare_2').clicked.connect(self.cancella_prenotazione)
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
        # Verifica che il giorno selezionato esista nel dizionario
        try:
            tavoli_disponibili = tavoliservizio[giorno_selezionato][servizio]
        except KeyError:
            message = QMessageBox()
            message.setText("Assicurati di selezionare un giorno valido.")
            message.exec()
            return

        tavoli_assegnati = []
        persone_da_sistemare = numero_persone
        # Genera un codice univoco di 6 caratteri, composto da lettere maiuscole e cifre
        codice = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        for tavolo in tavoli_disponibili:
            if not tavolo.occupato:
                tavolo.occupato = True
                tavolo.prenotazione = codice #self.nome_line.text()  # Collega il tavolo alla prenotazione
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
        message.setText(f"Prenotazione confermata a nome {nome} per il {giorno} a {servizio}. \nCodice: {prenotazione.codice}")
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

    
    def visualizza_prenotazioni(self): #---
        lista_prenotazioni = []
        for giorno, servizi in prenotazioniservizio.items():
            for servizio, prenotazioni in servizi.items():
                for prenotazione in prenotazioni:
                    # Usa strftime per formattare la data correttamente
                    giorno_formattato = giorno.strftime('%d/%m/%Y')
                    dettaglio = f"Giorno: {giorno_formattato}, Servizio: {servizio}, Nome: {prenotazione.nome}, Persone: {prenotazione.numero_persone}, Tavoli: {', '.join(str(t.nrTavolo) for t in prenotazione.tavoli_assegnati)}, Codice: {prenotazione.codice}"
                    lista_prenotazioni.append(dettaglio)

        # Visualizza le prenotazioni in un QMessageBox o in una ListView/TextEdit
        if lista_prenotazioni:
            message = QMessageBox()
            message.setText("\n".join(lista_prenotazioni))
            message.exec()
        else:
            message = QMessageBox()
            message.setText("Nessuna prenotazione trovata.")
            message.exec()

#---
    """def cancella_prenotazione(self, codice_prenotazione, giorno, servizio):
        giorno_selezionato = self.converti_giorno_in_data(giorno)

        # Trova e rimuovi la prenotazione
        prenotazioni = prenotazioniservizio[giorno_selezionato][servizio]
        prenotazione_da_rimuovere = None

        for prenotazione in prenotazioni:
            if prenotazione.codice == codice_prenotazione:
                prenotazione_da_rimuovere = prenotazione
                break

        if prenotazione_da_rimuovere:
            prenotazioni.remove(prenotazione_da_rimuovere)
            tavoli_assegnati = prenotazione_da_rimuovere.tavoli_assegnati

            # Reinserisci i tavoli liberati e compattali
            tavoliservizio[giorno_selezionato][servizio].extend(tavoli_assegnati)
            tavoliservizio[giorno_selezionato][servizio].sort()  # Riordina i tavoli in ordine crescente
            QtWidgets.QMessageBox.information(self, "Conferma", f"Prenotazione {codice_prenotazione} cancellata con successo.")
        else:
            QtWidgets.QMessageBox.warning(self, "Errore", "Prenotazione non trovata.")"""