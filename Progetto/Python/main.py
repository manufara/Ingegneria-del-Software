import os
from Database import database
from Menu import menu
from Tavolo import crea_tavoli
from Calendario import CalendarPopup
from Ordinazione import Ordinazione
from Prenotazione import Prenotazione
from GestoreTavoli import GestoreTavoli
from GestorePrenotazioni import GestorePrenotazioni
from Comanda import Comanda
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt


# Classe per la prima finestra (home_page)
class HomePage(QMainWindow):
    def __init__(self):
        super(HomePage, self).__init__()
        # Carica la finestra home_page
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/home_page.ui")
        uic.loadUi(ui_file, self)

        # Collega i pulsanti per aprire home_cliente e login
        self.findChild(QPushButton, 'pushButtonToHomeCliente').clicked.connect(self.open_home_cliente)
        self.findChild(QPushButton, 'pushButtonToLogin').clicked.connect(self.open_login)

        self.show()

    def open_home_cliente(self):
        self.cliente_window = HomeCliente()
        self.cliente_window.show()
        self.close()

    def open_login(self):
        self.login_window = Login()
        self.login_window.show()
        self.close()

# Classe per la finestra (home_cliente) ------------------------------------------------------------------------------
class HomeCliente(QMainWindow):
    def __init__(self):
        super(HomeCliente, self).__init__()
        # Carica la finestra home_cliente
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/home_cliente.ui")
        uic.loadUi(ui_file, self)

        # Collega il pulsante per aprire prenotazioni
        self.findChild(QPushButton, 'pushButtonToPrenotazioniCliente').clicked.connect(self.open_prenotazioni)
        # Collega il pulsante per aprire menu
        self.findChild(QPushButton, 'pushButton_2').clicked.connect(self.open_menu)
        # Collega il pulsante per aprire info
        self.findChild(QPushButton, 'pushButton_3').clicked.connect(self.open_info)
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def open_prenotazioni(self):
        self.pren_cli_window = Prenotazoni(self)
        self.pren_cli_window.show()
        self.close()

    def open_menu(self):
        self.menu_window = Menu()
        self.menu_window.show()
        self.close()

    def open_info(self):
        self.info_window = Info()
        self.info_window.show()
        self.close()

    def open_indietro(self):
        self.cliente_window = HomePage()
        self.cliente_window.show()
        self.close()

# Classe per la finestra (prenotazioni) -----------------------------------
class Prenotazoni(QMainWindow):
    def __init__(self, previous_window):
        super(Prenotazoni, self).__init__()
        # Carica la finestra prenotazioni
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/prenotazioni.ui")
        uic.loadUi(ui_file, self)
        
        # Memorizza la finestra precedente
        self.previous_window = previous_window

        # Collega il pulsante per aprire prenota_cli
        self.findChild(QPushButton, 'pushButton').clicked.connect(self.open_crea_prenotazione)
        # Collega il pulsante per aprire gestisci_prenotazione
        self.findChild(QPushButton, 'pushButton_2').clicked.connect(self.open_gestisci_prenotazione)
        # Collega il pulsante per tornare indietro
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
        # Mostra la finestra precedente
        self.previous_window.show()
        self.close()

# Classe per la finestra (crea_prenotazione) ---------------------
class CreaPrenotazione(QMainWindow):
    def __init__(self, previous_window):
        super(CreaPrenotazione, self).__init__()
        # Carica la finestra crea_prenotazione
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/crea_prenotazione.ui")
        uic.loadUi(ui_file, self)

        # Imposta il focus sul campo username
        self.nome_line.setFocus()

        # Memorizza la finestra precedente
        self.previous_window = previous_window
        # Crea un gruppo di pulsanti, aggiunge le checkbox al gruppo e rende il gruppo mutualmente esclusivo
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.pranzo_check)
        self.button_group.addButton(self.cena_check)
        self.button_group.setExclusive(True)

        database.carica_dati()  # Carica le prenotazioni all'avvio

        # Collegamento del pulsante con la finestra popup
        self.findChild(QPushButton, 'calendario_but').clicked.connect(lambda: CalendarPopup.mostra_calendario(self))
        # Collega il pulsante di conferma prenotazione
        self.findChild(QPushButton, 'conferma_but').clicked.connect(lambda: GestorePrenotazioni.crea_prenotazione(self, False))
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def open_indietro(self):
        # Mostra la finestra precedente
        self.previous_window.show()
        self.close()

# Classe per la finestra (gestisci_prenotazione) -----------------
class GestionePrenotazoni(QMainWindow):
    def __init__(self, previous_window):
        super(GestionePrenotazoni, self).__init__()
        # Carica la finestra gestisci_prenotazione
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/gestisci_prenotazione.ui")
        uic.loadUi(ui_file, self)

        # Memorizza la finestra precedente
        self.previous_window = previous_window
        # Carica le prenotazioni salvate dal file pickle
        database.carica_dati()

        # Collega il pulsante per abilitare le funzioni
        self.lineEdit.returnPressed.connect(self.but_enable)
        self.findChild(QPushButton, 'but_conferma').clicked.connect(self.but_enable)
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)
        # Collega il pulsante per visualizzare la prenotazione
        self.findChild(QPushButton, 'but_visualizza').clicked.connect(lambda: Prenotazione.mostra_prenotazione(self.lineEdit.text()))
        # Collega il pulsante per modificare la prenotazione
        self.findChild(QPushButton, 'but_modifica').clicked.connect(self.open_modifica)
        # Collega il pulsante per cancellare la prenotazione
        self.findChild(QPushButton, 'but_cancella').clicked.connect(lambda: GestorePrenotazioni.elimina_prenotazione(self, False))

        self.show()
    
    def but_enable(self): # Sblocca i pulsanti se il codice prenotazione è valido
        # Itera attraverso le prenotazioni per ottenere i codici
        self.codici_prenotazioni = []
        for giorno, servizi in database.dati_prenotazioni.items():  # Itera per ogni data
            for servizio, prenotazioni in servizi.items():  # Itera per ogni servizio (pranzo/cena)
                for prenotazione in prenotazioni:  # Itera sulle prenotazioni
                    if isinstance(prenotazione, Prenotazione):
                        self.codici_prenotazioni.append(prenotazione.codice)  # Aggiungi il codice alla lista

        codice_inserito = self.lineEdit.text()

        if codice_inserito in self.codici_prenotazioni:
            # Imposta lo stile per spigoli arrotondati e sblocca i pulsanti
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

    def open_indietro(self):
        # Mostra la finestra precedente
        self.previous_window.show()
        self.close()
                    
    def open_modifica(self):
        codice_inserito = self.lineEdit.text()
        self.mod_pren = ModificaPrenotazione(self)
        self.mod_pren.show()
        self.close()

# Classe per la finestra (modifica_prenotazione) --------
class ModificaPrenotazione(QMainWindow):
    def __init__(self, previous_window):
        super(ModificaPrenotazione, self).__init__()
        # Carica la finestra modifica_prenotazione
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/crea_prenotazione.ui")
        uic.loadUi(ui_file, self)

        # Memorizza la finestra precedente e il codice prenotazione
        self.previous_window = previous_window
        self.codice_inserito = previous_window.lineEdit.text()
        # Crea un gruppo di pulsanti, aggiunge le checkbox al gruppo e rende il gruppo mutualmente esclusivo
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.pranzo_check)
        self.button_group.addButton(self.cena_check)
        self.button_group.setExclusive(True)

        database.carica_dati()
        self.inizializza_finestra() # Precompila la finestra con i dati della vecchia prenotazione

        # Collegamento del pulsante con la finestra popup
        self.findChild(QPushButton, 'calendario_but').clicked.connect(lambda: CalendarPopup.mostra_calendario(self))
        # Collega il pulsante di conferma prenotazione
        self.findChild(QPushButton, 'conferma_but').clicked.connect(lambda: GestorePrenotazioni.modifica_prenotazione(self))
        # Collega il pulsante per tornare indietro
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
        # Mostra la finestra precedente
        self.previous_window.show()
        self.close()

# Classe per la finestra (menu) ---------------------------------------------------
class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        # Carica la finestra menu
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/menu.ui")
        uic.loadUi(ui_file, self)

        # Imposta il QListWidget per non essere modificabile
        self.menu_list.setEditTriggers(QListWidget.NoEditTriggers)
        # Creazione del menu leggendo dal file di testo
        menu.leggi_menu_da_file('../Progetto/testo_menu.txt')  # Carica i piatti nel menu
        menu.mostra_menu(self.menu_list)  # Mostra il menu nella lista

        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'pushButton').clicked.connect(self.open_home_cliente)
                
        self.show()

    def open_home_cliente(self):
        self.cliente_window = HomeCliente()
        self.cliente_window.show()
        self.close()

# Classe per la finestra (info) ----------------------------------------------------
class Info(QMainWindow):
    def __init__(self):
        super(Info, self).__init__()
        # Carica la finestra info
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/info.ui")
        uic.loadUi(ui_file, self)

        # Carica il testo da 'testo_info.txt' all'avvio
        self.load_text_from_file('../Progetto/testo_info.txt')

        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'pushButton').clicked.connect(self.open_home_cliente)

        self.show()

    def open_home_cliente(self):
        self.cliente_window = HomeCliente()
        self.cliente_window.show()
        self.close()

    def load_text_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            self.textEdit.setPlainText(content)

# Classe per la finestra (login) --------------------------------------------------------------------------------------
class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        # Carica la finestra login
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/login.ui")
        uic.loadUi(ui_file, self)

        # Imposta il focus sul campo username
        self.username.setFocus()
        # per rendere invisibile la password
        self.password.setEchoMode(QLineEdit.Password)

        # Collega il pulsante login e indietro
        self.password.returnPressed.connect(self.autenticazione)
        self.findChild(QPushButton, 'pushButton').clicked.connect(self.autenticazione)
        self.findChild(QPushButton, 'pushButton_2').clicked.connect(self.indietro)

        self.show()

    def autenticazione(self):
        if self.username.text() == "user" and self.password.text() == "pass":
            self.cameriere_window = HomeCameriere()
            self.cameriere_window.show()
            self.close()
        elif self.username.text() == "admin" and self.password.text() == "EmiliaAdmin":
            self.admin_window = HomeAmministratore()
            self.admin_window.show()
            self.close()
        else:
            message = QMessageBox()
            message.setText("Username o Password non validi")
            message.exec()

    def indietro(self):
        self.last_window = HomePage()
        self.last_window.show()
        self.close()

# Classe per la finestra (home_cameriere)--------------------------------------------
class HomeCameriere(QMainWindow):
    def __init__(self):
        super(HomeCameriere, self).__init__()
        # Carica la finestra home_cameriere
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/home_cameriere.ui")
        uic.loadUi(ui_file, self)

        # Collega il pulsante prenotazioni
        self.findChild(QPushButton, 'visualizza_tavoli').clicked.connect(self.open_tavoli)
        # Collega il pulsante nuovo_ordine
        self.findChild(QPushButton, 'nuovo_ordine').clicked.connect(self.open_ricerca)
        # Collega il pulsante aggiorna_ordine
        self.findChild(QPushButton, 'aggiorna_ordine').clicked.connect(self.open_ricerca)
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'logout').clicked.connect(self.open_indietro)

        self.show()

    def open_tavoli(self):
        self.pren_cli_window = VisualizzaTavoli(self)
        self.pren_cli_window.show()
        self.close()

    def open_ricerca(self):
        self.cliente_window = RicercaTavolo()
        self.cliente_window.show()
        self.close()

    def open_indietro(self):
        self.cliente_window = Login()
        self.cliente_window.show()
        self.close()

# Classe per la finestra (ricerca_tavolo)------------------
class RicercaTavolo(QMainWindow):
    def __init__(self):
        super(RicercaTavolo, self).__init__()
        # Carica la finestra ricerca_tavolo
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/ricerca_tavolo.ui")
        uic.loadUi(ui_file, self)

        self.focus_spinbox()

        # Collega il pulsante conferma
        self.findChild(QPushButton, 'pushButton').clicked.connect(self.open_conferma)
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def focus_spinbox(self):
        # Imposta il cursore alla fine del testo
        self.spinBox.lineEdit().setCursorPosition(len(self.spinBox.text()))

    def open_conferma(self):
        # Ottieni il valore dallo spinBox
        spin_value = self.spinBox.value()
        self.cliente_window = OrdinazioneWindow(spin_value)
        self.cliente_window.show()
        self.close()

    def open_indietro(self):
        self.cliente_window = HomeCameriere()
        self.cliente_window.show()
        self.close()

# Classe per la finestra (ordinazione)
class OrdinazioneWindow(QMainWindow):
    # Attributo di classe per tenere traccia della lista tavoli
    lista_tavoli = None

    def __init__(self, tavolo_selezionato):
        super(OrdinazioneWindow, self).__init__()
        # Carica la finestra ordinazione
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/crea_ordinazione.ui")
        uic.loadUi(ui_file, self)

        # Imposta il QListWidget per non essere modificabile
        self.menu_list.setEditTriggers(QListWidget.NoEditTriggers)
        # Creazione del menu leggendo dal file di testo
        menu.leggi_menu_da_file('../Progetto/testo_menu.txt')  # Carica i piatti nel menu
        menu.mostra_menu(self.menu_list)  # Mostra il menu nella lista

        self.menu_dict = {}  # Dizionario per piatti e prezzi
        # Popola la lista con categorie e piatti
        for piatto in menu.piatti:
            # Aggiorna il dizionario con il piatto e il prezzo
            self.menu_dict[piatto.nome] = float(piatto.prezzo)
        
        # Collega il pulsante 'aggiungi''
        self.findChild(QPushButton, 'but_aggiungi').clicked.connect(self.aggiungi_piatto)
        # Collega il pulsante 'visualizza' per visualizzare la comanda
        self.findChild(QPushButton, 'but_visualizza').clicked.connect(self.visualizza_comanda)
        # Collega il pulsante 'conferma'
        self.findChild(QPushButton, 'but_conferma').clicked.connect(self.conferma_ordine)
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)
        
        # Verifica se i tavoli sono già stati creati
        if OrdinazioneWindow.lista_tavoli is None:
            # Creazione dei tavoli solo la prima volta
            OrdinazioneWindow.lista_tavoli = crea_tavoli()

        # Imposta il tavolo selezionato
        self.lista_tavoli = OrdinazioneWindow.lista_tavoli
        self.tavolo = self.lista_tavoli[tavolo_selezionato - 1]  # Seleziona il tavolo dalla lista (indice base 0)

        # Verifica se esiste già un'ordinazione per questo tavolo
        if self.tavolo.ordinazione is None:
            # Crea una nuova ordinazione solo se non esiste
            self.tavolo.ordinazione = Ordinazione(tavolo_selezionato)

        # Crea una nuova comanda per ogni nuovo ordine
        self.comanda_corrente = Comanda()

        self.show()

    def open_indietro(self):
        self.cliente_window = RicercaTavolo()
        self.cliente_window.show()
        self.close()

    def aggiungi_piatto(self):
        item_selezionato = self.menu_list.currentItem()  # Ottieni l'elemento selezionato
        if item_selezionato:
            piatto_selezionato = item_selezionato.text()
            # Estrai solo il nome del piatto
            piatto_selezionato = piatto_selezionato.split(':')[0].strip()

            if piatto_selezionato in self.menu_dict:
                prezzo = self.menu_dict[piatto_selezionato]  # Trova il prezzo del piatto
                quantita = self.quantita_spin.value()  # Ottieni la quantità
                self.comanda_corrente.genera_comanda(piatto_selezionato, prezzo, quantita)
            else:
                message = QMessageBox()
                message.setText("Seleziona un piatto valido.")
                message.exec()

    def visualizza_comanda(self):
        if self.comanda_corrente.totale == 0:
            message = QMessageBox()
            message.setText("Comanda vuota")
            message.exec()
        else:
            descrizione = "Descrizione comanda \n"
            for piatto, quantita in self.comanda_corrente.piatti:
                descrizione += f" - {piatto} x{quantita} \n"
            message = QMessageBox()
            message.setText(descrizione)
            message.exec()

    def conferma_ordine(self):
        if self.comanda_corrente.piatti:
            self.tavolo.ordinazione.aggiorna_ordinazione(self.comanda_corrente)
            self.comanda_corrente = Comanda()  # Resetta la comanda
            
            message = QMessageBox()
            message.setText("Comanda confermata.")
            message.exec()
        else:
            message = QMessageBox()
            message.setText("Nessuna comanda da confermare.")
            message.exec()

# Classe per la finestra (home_amministratore)-----------------------------------------
class HomeAmministratore(QMainWindow):
    def __init__(self):
        super(HomeAmministratore, self).__init__()
        # Carica la finestra home_amministratore
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/home_amministratore.ui")
        uic.loadUi(ui_file, self)

        # Collega il pulsante per aprire prenotazioni
        self.findChild(QPushButton, 'prenotazioni').clicked.connect(self.open_prenotazioni)
        # Collega il pulsante per aprire lista_tavoli
        self.findChild(QPushButton, 'tavoli').clicked.connect(self.open_tavoli)
        # Collega il pulsante stampa_conto
        self.findChild(QPushButton, 'stampa').clicked.connect(self.open_stampa)
        # Collega il pulsante modifica
        self.findChild(QPushButton, 'modifica').clicked.connect(self.open_modifica)
        # Collega il pulsante per tornare indietro
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

    def open_stampa(self):
        self.cliente_window = StampaConto()
        self.cliente_window.show()
        self.close()

    def open_modifica(self):
        self.cliente_window = Modifica()
        self.cliente_window.show()
        self.close()

    def open_indietro(self):
        self.cliente_window = Login()
        self.cliente_window.show()
        self.close()

# Classe per la finestra (visualizza_tavoli)--------------
class VisualizzaTavoli(QMainWindow):
    def __init__(self, previous_window):
        super(VisualizzaTavoli, self).__init__()
        # Carica la finestra visualizza_tavoli
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/visualizza_tavoli.ui")
        uic.loadUi(ui_file, self)

        # Memorizza la finestra precedente
        self.previous_window = previous_window
        # Carica le prenotazioni salvate dal file pickle
        #self.prenotazioni = self.carica_prenotazioni()
        database.carica_dati()
        # Crea un gruppo di pulsanti, aggiunge le checkbox al gruppo e rende il gruppo mutualmente esclusivo
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.pranzo_check)
        self.button_group.addButton(self.cena_check)
        self.button_group.setExclusive(True)

        # Collegamento del pulsante con la finestra popup
        self.findChild(QPushButton, 'calendario_but').clicked.connect(lambda: CalendarPopup.mostra_calendario(self))
        # Collegamento del pulsante conferma passando come argomenti i componenti della finestra
        self.findChild(QPushButton, 'conferma_but').clicked.connect(lambda: GestoreTavoli.visualizza_lista_tavoli(self.lineEdit_giorno.text(), "pranzo" if self.pranzo_check.isChecked() else ("cena" if self.cena_check.isChecked() else ""), self.tavoli_list))
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def open_indietro(self):
        # Mostra la finestra precedente
        self.previous_window.show()
        self.close()

# Classe per la finestra (stampa_conto)------------------
class StampaConto(QMainWindow):
    def __init__(self):
        super(StampaConto, self).__init__()
        # Carica la finestra stampa_conto
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/stampa_conto.ui")
        uic.loadUi(ui_file, self)

        self.focus_spinbox()

        # Collega il pulsante per mostrare il conto
        self.findChild(QPushButton, 'pushButton').clicked.connect(self.open_conto)
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def focus_spinbox(self):
        # Imposta il cursore alla fine del testo
        self.spinBox.lineEdit().setCursorPosition(len(self.spinBox.text()))

    def open_conto(self):
        tavolo_selezionato = self.spinBox.value()
        if OrdinazioneWindow.lista_tavoli is None:
            message = QMessageBox()
            message.setText("Nessuna ordinazione per il tavolo selezionato.")
            message.exec()
        else:
            tavolo = OrdinazioneWindow.lista_tavoli[tavolo_selezionato - 1]
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
        self.cliente_window = HomeAmministratore()
        self.cliente_window.show()
        self.close()

# Classe per la finestra (modifica)------------------------
class Modifica(QMainWindow):
    def __init__(self):
        super(Modifica, self).__init__()
        # Carica la finestra modifica
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/modifica.ui")
        uic.loadUi(ui_file, self)

        # Collega il pulsante per modificare menu
        self.findChild(QPushButton, 'menu').clicked.connect(self.open_modifica_menu)
        # Collega il pulsante per modificare info
        self.findChild(QPushButton, 'info').clicked.connect(self.open_modifica_info)
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def open_modifica_menu(self):
        self.menu_window = ModificaMenu()
        self.menu_window.show()
        self.close()

    def open_modifica_info(self):
        self.info_window = ModificaInfo()
        self.info_window.show()
        self.close()

    def open_indietro(self):
        self.cliente_window = HomeAmministratore()
        self.cliente_window.show()
        self.close()

# Classe per la finestra (modifica_menu)
class ModificaMenu(QMainWindow):
    def __init__(self):
        super(ModificaMenu, self).__init__()
        # Carica la finestra menu
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/menu.ui")
        uic.loadUi(ui_file, self)

        # Creazione del menu leggendo dal file di testo
        menu.leggi_menu_da_file('../Progetto/testo_menu.txt')  # Carica i piatti nel menu
        menu.mostra_menu(self.menu_list)  # Mostra il menu nella lista

        # Rende modificabile il testo e visibile il pulsante salva
        self.menu_list.setEnabled(True)
        self.salva.setGeometry(80, 380, 101, 31)
        # Collega il pulsante indietro e il pulsante salva
        self.findChild(QPushButton, 'salva').clicked.connect(self.salva_modifiche_al_file)
        self.findChild(QPushButton, 'pushButton').clicked.connect(self.indietro)

        # Crea una variabile per il QListWidget
        self.list_widget = self.findChild(QListWidget, 'menu_list')
        # Aggiungi il menu contestuale (clic destro)
        self.list_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.list_widget.customContextMenuRequested.connect(self.show_context_menu)

        self.show()

    # Funzione per il menu contestuale
    def show_context_menu(self, position):
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

        add_action = menu_contestuale.addAction("Aggiungi Elemento")
        edit_action = menu_contestuale.addAction("Modifica Elemento")
        delete_action = menu_contestuale.addAction("Elimina Elemento")

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
        self.cliente_window = Modifica()
        self.cliente_window.show()
        self.close()

# Classe per la finestra (modifica_info)
class ModificaInfo(QMainWindow):
    def __init__(self):
        super(ModificaInfo, self).__init__()
        # Carica la finestra menu
        ui_file = os.path.join(os.path.dirname(__file__), "../Qt/info.ui")
        uic.loadUi(ui_file, self)

        # Rende modificabile il testo e visibile il pulsante salva
        self.textEdit.setEnabled(True)
        self.salva.setGeometry(70, 380, 101, 32)
        # Collega il pulsante indietro e il pulsante salva
        self.findChild(QPushButton, 'pushButton').clicked.connect(self.open_modifica)
        self.findChild(QPushButton, 'salva').clicked.connect(self.salva_modifiche_al_file)

        # Carica il testo da 'testo_info.txt' all'avvio
        self.load_text_from_file('../Progetto/testo_info.txt')

        self.show()

    def open_modifica(self):
        self.cliente_window = Modifica()
        self.cliente_window.show()
        self.close()

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


# Funzione principale
def main():
    app = QApplication([])
    # Avvia la prima finestra (home_page)
    window = HomePage()
    app.exec()

if __name__ == '__main__':
    main()
