from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *

# classe prenotazione ----------------------------
class Prenotazione:
    def __init__(self, nome, giorno, servizio, numero_persone, codice, tavoli_assegnati):
        self.nome = nome
        self.giorno = giorno
        self.servizio = servizio
        self.numero_persone = numero_persone
        self.codice = codice
        self.tavoli_assegnati = tavoli_assegnati


# classe tavolo ---------------------------------
class Tavolo:
    def __init__(self, nrTavolo):
        self.nrTavolo = nrTavolo
        self.occupato = False
        self.capacita = 4
        self.Prenotazione=None # Collegamento alla prenotazione che occupa il tavolo

        #self.cameriere = None
        #self.ordinazione = None


# classe calendario ------------------------------
class CalendarPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Ottieni la posizione del QLineEdit
        line_edit_pos = parent.lineEdit_giorno.pos()  # Ottieni la posizione del lineEdit
        # Sposta il popup alla stessa posizione del lineEdit
        self.move(line_edit_pos.x(), line_edit_pos.y() + parent.lineEdit_giorno.height())

        # Imposta lo stile per spigoli arrotondati
        self.setStyleSheet("""
            QDialog {
                border-radius: 15px;  /* Arrotonda gli spigoli */
                background-color: #F0F0F0;  /* Colore di sfondo */
            }
        """)

        # Crea il layout verticale
        layout = QVBoxLayout(self)

        # Crea il widget del calendario
        self.calendarWidget = QCalendarWidget(self)
        self.calendarWidget.setSelectedDate(QDate(2025, 6, 1))  # Data iniziale
        self.calendarWidget.setMinimumDate(QDate(2025, 6, 1))  # Data minima
        self.calendarWidget.setMaximumDate(QDate(2025, 9, 30))  # Data massima
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)  # Nascondi l'intestazione verticale

        # Aggiungi il calendario al layout
        layout.addWidget(self.calendarWidget)

        # Crea un pulsante per confermare la selezione
        confirm_button = QPushButton("Conferma", self)
        confirm_button.clicked.connect(self.seleziona_data)  # Collega il pulsante alla funzione di selezione
        layout.addWidget(confirm_button)

    def seleziona_data(self):
        date = self.calendarWidget.selectedDate()  # Ottieni la data selezionata
        selected_date = date.toPyDate()  # Converte QDate in datetime.date
        self.parent().lineEdit_giorno.setText(selected_date.strftime("%d/%m/%Y"))
        self.close()  # Chiudi il popup

# Funzione per creare tavoli
def creaTavoli():
    tavoli = []
    numero_tavoli = 20  # Si hanno 20 tavoli disponibili
    for i in range(1, numero_tavoli + 1):
        tavoli.append(Tavolo(nrTavolo=i))  # Crea un nuovo oggetto Tavolo e lo aggiunge alla lista
    return tavoli
