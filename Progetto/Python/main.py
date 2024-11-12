import os
from Database import database
from Menu import menu
from Calendario import CalendarPopup
from Prenotazione import Prenotazione
from Comanda import Comanda
from GestoreTavoli import GestoreTavoli
from GestorePrenotazioni import GestorePrenotazioni
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt
from datetime import datetime


# Classe per la finestra (home_page)
class HomePage(QMainWindow):
    def __init__(self):
        super(HomePage, self).__init__()
        # Carica la finestra home_page
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/home_page.ui")
        uic.loadUi(ui_file, self)

        database.carica_dati() # Carica i dati relativi alle prenotazioni e ai tavoli dal file pickle

        # Collega i pulsanti per aprire home_cliente e login
        self.findChild(QPushButton, 'pushButtonToHomeCliente').clicked.connect(self.open_home_cliente)
        self.findChild(QPushButton, 'pushButtonToLogin').clicked.connect(self.open_login)

        self.show()

    def open_home_cliente(self):
        self.cliente_window = HomeCliente(self)
        self.cliente_window.show()
        self.close()

    def open_login(self):
        self.login_window = Login(self)
        self.login_window.show()
        self.close()

# Classe per la finestra (home_cliente) ------------------------------------------------------------------------------
class HomeCliente(QMainWindow):
    def __init__(self, previous):
        super(HomeCliente, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/home_cliente.ui")
        uic.loadUi(ui_file, self)

        self.previous = previous # Memorizza la finestra precedente

        self.findChild(QPushButton, 'pushButtonToPrenotazioniCliente').clicked.connect(self.open_prenotazioni)
        self.findChild(QPushButton, 'pushButton_2').clicked.connect(self.open_menu)
        self.findChild(QPushButton, 'pushButton_3').clicked.connect(self.open_info)
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def open_prenotazioni(self):
        self.pren_cli_window = Prenotazoni(self)
        self.pren_cli_window.show()
        self.close()

    def open_menu(self):
        self.menu_window = Menu(self)
        self.menu_window.show()
        self.close()

    def open_info(self):
        self.info_window = Info(self)
        self.info_window.show()
        self.close()

    def open_indietro(self):
        # Mostra la finestra precedente
        self.previous.show()
        self.close()

# Classe per la finestra (prenotazioni) -------------------------------------------
class Prenotazoni(QMainWindow):
    def __init__(self, previous_window):
        super(Prenotazoni, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/prenotazioni.ui")
        uic.loadUi(ui_file, self)
        
        self.previous_window = previous_window

        self.findChild(QPushButton, 'pushButton').clicked.connect(self.open_crea_prenotazione)
        self.findChild(QPushButton, 'pushButton_2').clicked.connect(self.open_gestisci_prenotazione)
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def open_crea_prenotazione(self):
        self.prenota = CreaPrenotazione(self)
        self.prenota.show()
        self.close()

    def open_gestisci_prenotazione(self):
        self.gest_pren_cli = GestionePrenotazoni(self)
        self.gest_pren_cli.show()
        self.close()
    
    def open_indietro(self):
        self.previous_window.show()
        self.close()

# Classe per la finestra (crea_prenotazione) ---------------------
class CreaPrenotazione(QMainWindow):
    def __init__(self, previous_window):
        super(CreaPrenotazione, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/crea_prenotazione.ui")
        uic.loadUi(ui_file, self)

        self.nome_line.setFocus() # Imposta il focus sul campo username
        self.previous_window = previous_window

        # Crea un gruppo di pulsanti, aggiunge le checkbox al gruppo e rende il gruppo mutualmente esclusivo
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.pranzo_check)
        self.button_group.addButton(self.cena_check)
        self.button_group.setExclusive(True)

        self.findChild(QPushButton, 'calendario_but').clicked.connect(lambda: CalendarPopup.mostra_calendario(self))
        self.findChild(QPushButton, 'conferma_but').clicked.connect(lambda: GestorePrenotazioni.crea_prenotazione(self, False))
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def open_indietro(self):
        self.previous_window.show()
        self.close()

# Classe per la finestra (gestisci_prenotazione) -----------------
class GestionePrenotazoni(QMainWindow):
    def __init__(self, previous_window):
        super(GestionePrenotazoni, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/gestisci_prenotazione.ui")
        uic.loadUi(ui_file, self)

        self.previous_window = previous_window

        self.lineEdit.returnPressed.connect(self.but_enable) # Funziona premendo il tasto 'invio'
        self.findChild(QPushButton, 'but_conferma').clicked.connect(self.but_enable)
        self.findChild(QPushButton, 'but_visualizza').clicked.connect(lambda: Prenotazione.mostra_prenotazione(self.lineEdit.text()))
        self.findChild(QPushButton, 'but_modifica').clicked.connect(self.open_modifica)
        self.findChild(QPushButton, 'but_cancella').clicked.connect(lambda: GestorePrenotazioni.elimina_prenotazione(self, False))
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()
    
    def but_enable(self): # Sblocca i pulsanti se il codice prenotazione è valido
        # Itera attraverso le prenotazioni per ottenere i codici
        self.codici_prenotazioni = []
        for giorno, servizi in database.dati_prenotazioni.items():  # Itera per ogni data
            for servizio, prenotazioni in servizi.items():  # Itera per ogni servizio
                for prenotazione in prenotazioni:  # Itera sulle prenotazioni
                    if isinstance(prenotazione, Prenotazione):
                        self.codici_prenotazioni.append(prenotazione.codice)  # Aggiungi il codice alla lista

        codice_inserito = self.lineEdit.text()

        if codice_inserito in self.codici_prenotazioni:
            # Sblocca i pulsanti
            self.setStyleSheet("""
                QPushButton {
                    border: 2px solid #5A5A5A;
                    border-radius: 10px;
                    padding: 5px;
                    background-color: #D3CFC4;
                    color: black;
                    border: 1px solid black;  /* Bordo del pulsante */
                }
                QPushButton:hover {
                    background-color: lightgray;  /* Cambia colore al passaggio del mouse */
                }
            """)
            self.but_visualizza.setEnabled(True)
            self.but_modifica.setEnabled(True)
            self.but_cancella.setEnabled(True)
        else:
            self.setStyleSheet("""
                QPushButton {
                    border: 2px solid #5A5A5A;
                    border-radius: 10px;
                    padding: 5px;
                    color: black;
                    border: 1px solid black;  /* Bordo del pulsante */
                }
                QPushButton:hover {
                    background-color: lightgray;  /* Cambia colore al passaggio del mouse */
                }
            """)
            self.but_visualizza.setEnabled(False)
            self.but_modifica.setEnabled(False)
            self.but_cancella.setEnabled(False)

            message = QMessageBox()
            message.setText(f"Prenotazione {codice_inserito} non trovata")
            message.exec()
                    
    def open_modifica(self):
        self.mod_pren = ModificaPrenotazione(self)
        self.mod_pren.show()
        self.close()

    def open_indietro(self):
        self.previous_window.show()
        self.close()

# Classe per la finestra (modifica_prenotazione) --------
class ModificaPrenotazione(QMainWindow):
    def __init__(self, previous_window):
        super(ModificaPrenotazione, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/crea_prenotazione.ui")
        uic.loadUi(ui_file, self)

        self.previous_window = previous_window
        self.codice_inserito = previous_window.lineEdit.text() # Memorizza il codice prenotazione
        
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.pranzo_check)
        self.button_group.addButton(self.cena_check)
        self.button_group.setExclusive(True)

        self.inizializza_finestra() # Precompila la finestra con i dati della vecchia prenotazione

        self.findChild(QPushButton, 'calendario_but').clicked.connect(lambda: CalendarPopup.mostra_calendario(self))
        self.findChild(QPushButton, 'conferma_but').clicked.connect(lambda: GestorePrenotazioni.modifica_prenotazione(self))
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def inizializza_finestra(self):
        prenotazione = GestorePrenotazioni.cerca_prenotazione(self.codice_inserito)

        self.nome_line.setText(prenotazione.nome)
        self.nome_line.setEnabled(False)
        data_formattata = prenotazione.giorno.strftime("%d/%m/%Y")
        self.lineEdit_giorno.setText(data_formattata)
        if prenotazione.servizio == 'pranzo':
            self.pranzo_check.setChecked(True)
        else:
            self.cena_check.setChecked(True)
        self.persone_spin.setValue(prenotazione.numero_persone)
        return

    def open_indietro(self):
        self.previous_window.show()
        self.close()

# Classe per la finestra (menu) ---------------------------------------------------
class Menu(QMainWindow):
    def __init__(self, previous):
        super(Menu, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/menu.ui")
        uic.loadUi(ui_file, self)

        self.previous = previous

        # Imposta il QListWidget per non essere modificabile
        self.menu_list.setEditTriggers(QListWidget.NoEditTriggers)
        # Creazione del menu leggendo dal file di testo
        menu.leggi_menu_da_file('../Progetto/testo_menu.txt')  # Carica i piatti nel menu
        menu.mostra_menu(self.menu_list)  # Mostra il menu nella lista

        self.findChild(QPushButton, 'pushButton').clicked.connect(self.open_home_cliente)
                
        self.show()

    def open_home_cliente(self):
        self.previous.show()
        self.close()

# Classe per la finestra (info) ---------------------------------------------------
class Info(QMainWindow):
    def __init__(self, previous):
        super(Info, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/info.ui")
        uic.loadUi(ui_file, self)

        self.previous = previous

        # Carica il testo da 'testo_info.txt'
        self.load_text_from_file('../Progetto/testo_info.txt')

        self.findChild(QPushButton, 'pushButton').clicked.connect(self.open_home_cliente)

        self.show()

    def load_text_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            self.textEdit.setPlainText(content)

    def open_home_cliente(self):
        self.previous.show()
        self.close()

# Classe per la finestra (login) -------------------------------------------------------------------------------------
class Login(QMainWindow):
    def __init__(self, previous):
        super(Login, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/login.ui")
        uic.loadUi(ui_file, self)

        self.previous = previous
        self.username.setFocus() # Imposta il focus sul campo username
        self.password.setEchoMode(QLineEdit.Password) # Rende invisibile la password

        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.pranzo_check)
        self.button_group.addButton(self.cena_check)
        self.button_group.setExclusive(True)

        self.findChild(QPushButton, 'calendario_but').clicked.connect(lambda: CalendarPopup.mostra_calendario(self))
        self.password.returnPressed.connect(lambda: self.autenticazione(self.lineEdit_giorno.text(), "pranzo" if self.pranzo_check.isChecked() else ("cena" if self.cena_check.isChecked() else "")))
        self.findChild(QPushButton, 'pushButton').clicked.connect(lambda: self.autenticazione(self.lineEdit_giorno.text(), "pranzo" if self.pranzo_check.isChecked() else ("cena" if self.cena_check.isChecked() else "")))
        self.findChild(QPushButton, 'pushButton_2').clicked.connect(self.indietro)

        self.id_camerieri =[]
        for cameriere in database.lista_camerieri:
            self.id_camerieri.append(cameriere.id)
        
        self.show()

    def autenticazione(self, giorno, servizio):
        if not giorno or not servizio: # Controlla che tutti i campi siano riempiti
            message = QMessageBox()
            message.setText("Assicurati di compilare tutti i campi.")
            message.exec()
            return
            
        if self.username.text() == "admin" and self.password.text() == "EmiliaAdmin":
            self.admin_window = HomeAmministratore(self, giorno, servizio)
            self.admin_window.show()
            self.close()
        elif self.username.text() in self.id_camerieri and self.password.text() == "Emilia":
            self.cameriere_window = HomeCameriere(self, self.username.text(), giorno, servizio)
            self.cameriere_window.show()
            self.close()
        else:
            message = QMessageBox()
            message.setText("Username o Password non validi")
            message.exec()

    def showEvent(self, event):
        # Svuota i campi di input ogni volta che la finestra viene mostrata
        self.username.clear()
        self.password.clear()
        self.lineEdit_giorno.clear()

        self.button_group.setExclusive(False) # Disabilita temporaneamente l'esclusività e deseleziona le checkbox
        self.pranzo_check.setChecked(False)
        self.cena_check.setChecked(False)
        self.button_group.setExclusive(True)  # Riabilita l'esclusività

        self.username.setFocus()
        super(Login, self).showEvent(event)

    def indietro(self):
        self.previous.show()
        self.close()

# Classe per la finestra (home_cameriere)------------------------------------------
class HomeCameriere(QMainWindow):
    def __init__(self, previous, id_cameriere, giorno, servizio):
        super(HomeCameriere, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/home_cameriere.ui")
        uic.loadUi(ui_file, self)

        self.previous = previous
        self.cameriere = None
        for cameriere in database.lista_camerieri:
            if id_cameriere == cameriere.id:
                self.cameriere = cameriere

        self.findChild(QPushButton, 'visualizza_tavoli').clicked.connect(self.open_tavoli)
        self.findChild(QPushButton, 'assegna_cameriere').clicked.connect(lambda: self.open_ricerca('assegna', giorno, servizio, self.cameriere))
        self.findChild(QPushButton, 'ordinazioni').clicked.connect(lambda: self.open_ricerca('ordinazioni', giorno, servizio, self.cameriere))
        self.findChild(QPushButton, 'logout').clicked.connect(self.open_indietro)

        self.show()

    def open_tavoli(self):
        self.pren_cli_window = VisualizzaTavoli(self)
        self.pren_cli_window.show()
        self.close()

    def open_ricerca(self, action, giorno, servizio, cameriere):
        self.cliente_window = RicercaTavolo(self, action, giorno, servizio, cameriere)
        self.cliente_window.show()
        self.close()

    def open_indietro(self):
        self.previous.show()
        self.close()

# Classe per la finestra (ricerca_tavolo)--------------------------
class RicercaTavolo(QMainWindow):
    def __init__(self, previous, action, giorno, servizio, cameriere):
        super(RicercaTavolo, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/ricerca_tavolo.ui")
        uic.loadUi(ui_file, self)

        self.previous = previous
        self.cameriere = cameriere

        self.focus_spinbox()

        self.findChild(QPushButton, 'conferma_but').clicked.connect(lambda: self.open_conferma(action))
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.giorno_selezionato = datetime.strptime(giorno, "%d/%m/%Y").date()
        self.lista_tavoli = database.dati_tavoli[self.giorno_selezionato][servizio]

        self.show()

    def focus_spinbox(self):
        self.spinBox.lineEdit().setCursorPosition(len(self.spinBox.text())) # Imposta il cursore alla fine del testo

    def open_conferma(self, action):
        spin_value = self.spinBox.value() # Ottiene il valore dallo spinBox
        tavolo_selezionato = self.lista_tavoli[spin_value - 1]
        if action == 'assegna':
            self.cameriere.assegna_cameriere(tavolo_selezionato)
        elif action == 'ordinazioni':
            assegnato = False
            for tavolo in self.cameriere.tavoli:
                if tavolo.nrTavolo == tavolo_selezionato.nrTavolo:
                    assegnato = True
                    break

            if assegnato == True:
                self.cliente_window = OrdinazioneWindow(self, tavolo_selezionato)
                self.cliente_window.show()
                self.close()
            else:
                message = QMessageBox()
                message.setText(f"Devi essere assegnato al tavolo {tavolo_selezionato.nrTavolo} per poter prendere l'ordinazione.")
                message.exec()

    def open_indietro(self):
        self.previous.show()
        self.close()

# Classe per la finestra (crea_ordinazione)---------------
class OrdinazioneWindow(QMainWindow):
    def __init__(self, previous, tavolo_selezionato):
        super(OrdinazioneWindow, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/crea_ordinazione.ui")
        uic.loadUi(ui_file, self)

        self.previous = previous
        self.tavolo = tavolo_selezionato

        self.menu_list.setEditTriggers(QListWidget.NoEditTriggers)
        menu.leggi_menu_da_file('../Progetto/testo_menu.txt')
        menu.mostra_menu(self.menu_list)

        self.menu_dict = {} # Crea un dizionario per piatti e prezzi
        for piatto in menu.piatti: # Popola la lista con categorie e piatti
            self.menu_dict[piatto.nome] = float(piatto.prezzo) # Aggiorna il dizionario con il piatto e il prezzo

        self.comanda_corrente = Comanda() # Crea una nuova comanda per ogni nuova ordinazione
        
        self.findChild(QPushButton, 'but_aggiungi').clicked.connect(lambda: self.comanda_corrente.aggiungi_piatto(self))
        self.findChild(QPushButton, 'but_visualizza').clicked.connect(lambda: self.comanda_corrente.visualizza_comanda(self))
        self.findChild(QPushButton, 'but_conferma').clicked.connect(lambda: self.tavolo.ordinazione.conferma_ordinazione(self.tavolo, self.comanda_corrente))
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def open_indietro(self):
        self.previous.show()
        self.close()

# Classe per la finestra (home_amministratore)--------------------------------------
class HomeAmministratore(QMainWindow):
    def __init__(self, previous, giorno, servizio):
        super(HomeAmministratore, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/home_amministratore.ui")
        uic.loadUi(ui_file, self)

        self.previous = previous

        self.findChild(QPushButton, 'prenotazioni').clicked.connect(self.open_prenotazioni)
        self.findChild(QPushButton, 'tavoli').clicked.connect(self.open_tavoli)
        self.findChild(QPushButton, 'stampa').clicked.connect(lambda: self.open_stampa(giorno, servizio))
        self.findChild(QPushButton, 'modifica').clicked.connect(self.open_modifica)
        self.findChild(QPushButton, 'logout').clicked.connect(self.open_indietro)

        self.show()
        
    def open_prenotazioni(self):
        self.pren_cli_window = Prenotazoni(self)
        self.pren_cli_window.show()
        self.close()

    def open_tavoli(self):
        self.pren_cli_window = VisualizzaTavoli(self)
        self.pren_cli_window.show()
        self.close()

    def open_stampa(self, giorno, servizio):
        self.cliente_window = StampaConto(self, giorno, servizio)
        self.cliente_window.show()
        self.close()

    def open_modifica(self):
        self.cliente_window = Modifica(self)
        self.cliente_window.show()
        self.close()

    def open_indietro(self):
        self.previous.show()
        self.close()

# Classe per la finestra (visualizza_tavoli)------------------------
class VisualizzaTavoli(QMainWindow):
    def __init__(self, previous_window):
        super(VisualizzaTavoli, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/visualizza_tavoli.ui")
        uic.loadUi(ui_file, self)

        self.previous_window = previous_window
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.pranzo_check)
        self.button_group.addButton(self.cena_check)
        self.button_group.setExclusive(True)

        self.findChild(QPushButton, 'calendario_but').clicked.connect(lambda: CalendarPopup.mostra_calendario(self))
        self.findChild(QPushButton, 'conferma_but').clicked.connect(lambda: GestoreTavoli.visualizza_lista_tavoli(self.lineEdit_giorno.text(), "pranzo" if self.pranzo_check.isChecked() else ("cena" if self.cena_check.isChecked() else ""), self.tavoli_list))
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def open_indietro(self):
        self.previous_window.show()
        self.close()

# Classe per la finestra (stampa_conto)-------------------
class StampaConto(QMainWindow):
    def __init__(self, previous, giorno, servizio):
        super(StampaConto, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/stampa_conto.ui")
        uic.loadUi(ui_file, self)

        self.previous = previous
        self.focus_spinbox()

        self.findChild(QPushButton, 'pushButton').clicked.connect(self.open_conto)
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.giorno_selezionato = datetime.strptime(giorno, "%d/%m/%Y").date()
        self.lista_tavoli = database.dati_tavoli[self.giorno_selezionato][servizio]

        self.show()

    def focus_spinbox(self):
        self.spinBox.lineEdit().setCursorPosition(len(self.spinBox.text()))

    def open_conto(self):
        tavolo_selezionato = self.spinBox.value()
        tavolo = self.lista_tavoli[tavolo_selezionato - 1]
        if tavolo.ordinazione is None:
            message = QMessageBox()
            message.setText("Nessuna ordinazione per il tavolo selezionato.")
            message.exec()
        else:
            da_visualizzare = tavolo.ordinazione.mostra_ordinazione()
            message = QMessageBox()
            message.setText(da_visualizzare)
            message.exec()

    def open_indietro(self):
        self.previous.show()
        self.close()

# Classe per la finestra (modifica)-----------------------
class Modifica(QMainWindow):
    def __init__(self, previous):
        super(Modifica, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/modifica.ui")
        uic.loadUi(ui_file, self)

        self.previous = previous

        self.findChild(QPushButton, 'menu').clicked.connect(self.open_modifica_menu)
        self.findChild(QPushButton, 'info').clicked.connect(self.open_modifica_info)
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def open_modifica_menu(self):
        self.menu_window = ModificaMenu(self)
        self.menu_window.show()
        self.close()

    def open_modifica_info(self):
        self.info_window = ModificaInfo(self)
        self.info_window.show()
        self.close()

    def open_indietro(self):
        self.previous.show()
        self.close()

# Classe per la finestra (modifica_menu)
class ModificaMenu(QMainWindow):
    def __init__(self, previous):
        super(ModificaMenu, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/menu.ui")
        uic.loadUi(ui_file, self)

        self.previous = previous

        menu.leggi_menu_da_file('../Progetto/testo_menu.txt')
        menu.mostra_menu(self.menu_list)

        # Rende modificabile il testo e visibile il pulsante salva
        self.menu_list.setEnabled(True)
        self.salva.setGeometry(80, 380, 101, 31)

        self.findChild(QPushButton, 'salva').clicked.connect(self.salva_modifiche_al_file)
        self.findChild(QPushButton, 'pushButton').clicked.connect(self.indietro)

        self.list_widget = self.findChild(QListWidget, 'menu_list') # Crea una variabile per il QListWidget
        # Aggiungi il menu contestuale (clic destro)
        self.list_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.list_widget.customContextMenuRequested.connect(self.show_context_menu)

        self.show()

    def show_context_menu(self, position): # Funzione per aprire il menu contestuale
        menu_contestuale = QtWidgets.QMenu()

        # Imposta il foglio di stile
        menu_contestuale.setStyleSheet("""
            QMenu {
                background-color: #F0F0F0;
                border: 2px solid #5A5A5A;
                border-radius: 10px;
                padding: 5px;
                margin: 0;  /* Aggiunto per evitare margini */
            }
            QMenu::item {
                background-color: transparent;
                color: #5A5A5A;
                padding: 5px 20px;
                border-radius: 5px;
            }
            QMenu::item:selected {
                background-color: #D3D3D3;
            }
            QMenu::item:pressed {
                background-color: #A9A9A9;
            }
        """)

        add_action = menu_contestuale.addAction("Aggiungi Piatto")
        edit_action = menu_contestuale.addAction("Modifica Piatto")
        delete_action = menu_contestuale.addAction("Elimina Piatto")

        action = menu_contestuale.exec_(self.list_widget.viewport().mapToGlobal(position))
        
        if action == add_action:
            menu.modifica_menu(self.list_widget, 'aggiungi')
        elif action == edit_action:
            menu.modifica_menu(self.list_widget, 'modifica')
        elif action == delete_action:
            menu.modifica_menu(self.list_widget, 'elimina')

    def salva_modifiche_al_file(self):
        with open('../Progetto/testo_menu.txt', 'w') as file:
            categoria_corrente = None
            for i in range(self.list_widget.count()):
                item = self.list_widget.item(i).text()
                
                # Controlla se è una categoria
                if not (":" in item and "€" in item):  # Se non contiene il formato piatto: descrizione - prezzo€
                    categoria_corrente = item.strip()
                    file.write(categoria_corrente + '\n')  # Scrivi la categoria nel file
                else:
                    # Se è un piatto, riconverti al formato originale
                    piatto, resto = item.split(": ")
                    descrizione, prezzo = resto.split(" - ")
                    prezzo = prezzo.replace("€", "")  # Rimuovi il simbolo dell'euro
                    file.write(f"{piatto}, {descrizione}, {prezzo}\n")

            message = QMessageBox()
            message.setText("Modifiche salvate con successo.")
            message.exec()

    def indietro(self):
        self.previous.show()
        self.close()

# Classe per la finestra (modifica_info)
class ModificaInfo(QMainWindow):
    def __init__(self, previous):
        super(ModificaInfo, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/info.ui")
        uic.loadUi(ui_file, self)

        self.previous = previous
        self.textEdit.setEnabled(True)
        self.salva.setGeometry(70, 380, 101, 32)

        self.load_text_from_file('../Progetto/testo_info.txt')

        self.findChild(QPushButton, 'pushButton').clicked.connect(self.open_modifica)
        self.findChild(QPushButton, 'salva').clicked.connect(self.salva_modifiche_al_file)

        self.show()

    def salva_modifiche_al_file(self):
        contenuto = self.textEdit.toPlainText()  # Ottiene il testo dal QTextEdit
        with open('../Progetto/testo_info.txt', 'w', encoding='utf-8') as file:
            file.write(contenuto)

            message = QMessageBox()
            message.setText("Modifiche salvate con successo.")
            message.exec()

    def load_text_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            self.textEdit.setPlainText(content)

    def open_modifica(self):
        self.previous.show()
        self.close()


# Funzione principale
def main():
    app = QApplication([])
    window = HomePage() # Avvia la prima finestra (home_page)
    app.exec()

if __name__ == '__main__':
    main()
