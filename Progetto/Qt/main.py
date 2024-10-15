import os
from menu_class import leggi_menu_da_file
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt

# Classe per la prima finestra (home_page)
class HomePage(QMainWindow):
    def __init__(self):
        super(HomePage, self).__init__()

        # Carica la finestra home_page
        ui_file = os.path.join(os.path.dirname(__file__), "home_page.ui")
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
        ui_file = os.path.join(os.path.dirname(__file__), "home_cliente.ui")
        uic.loadUi(ui_file, self)

        # Collega il pulsante per aprire prenotazioni_cliente
        self.findChild(QPushButton, 'pushButtonToPrenotazioniCliente').clicked.connect(self.open_prenotazioni_cliente)
        # Collega il pulsante per aprire menu
        self.findChild(QPushButton, 'pushButton_2').clicked.connect(self.open_menu)
        # Collega il pulsante per aprire info
        self.findChild(QPushButton, 'pushButton_3').clicked.connect(self.open_info)
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def open_prenotazioni_cliente(self):
        self.pren_cli_window = PrenotazoniCliente(self)
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

# Classe per la finestra (prenotazioni_cliente) -----------------------------------
class PrenotazoniCliente(QMainWindow):
    def __init__(self, previous_window):
        super(PrenotazoniCliente, self).__init__()

        # Carica la finestra prenotazioni_cliente
        ui_file = os.path.join(os.path.dirname(__file__), "prenotazioni_cliente.ui")
        uic.loadUi(ui_file, self)
        
        # Memorizza la finestra precedente
        self.previous_window = previous_window

        # Collega il pulsante per aprire prenota_cli
        self.findChild(QPushButton, 'pushButton').clicked.connect(self.open_prenota_cliente)
        # Collega il pulsante per aprire gest_pren_cli
        self.findChild(QPushButton, 'pushButton_2').clicked.connect(self.open_gest_cli)
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def open_prenota_cliente(self):
        self.prenota_cli = PrenotaCliente(self)
        self.prenota_cli.show()
        self.close()

    def open_gest_cli(self):
        self.gest_pren_cli = GestionePrenotazoniCliente(self)
        self.gest_pren_cli.show()
        self.close()

    def open_indietro(self):
        # Mostra la finestra precedente
        self.previous_window.show()
        self.close()

# Classe per la finestra (prenota) ----------------------
class PrenotaCliente(QMainWindow):
    def __init__(self, previous_window):
        super(PrenotaCliente, self).__init__()

        # Carica la finestra prenota
        ui_file = os.path.join(os.path.dirname(__file__), "prenota.ui")
        uic.loadUi(ui_file, self)
        # Memorizza la finestra precedente
        self.previous_window = previous_window

        # Crea un gruppo di pulsanti, aggiunge le checkbox al gruppo e rende il gruppo mutualmente esclusivo
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.pranzo_check)
        self.button_group.addButton(self.cena_check)
        self.button_group.setExclusive(True)

        # Collega il pulsante di conferma prenotazione
        #self.findChild(QPushButton, 'pushButton').clicked.connect(self.crea_prenotazione)
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def open_indietro(self):
        # Mostra la finestra precedente
        self.previous_window.show()
        self.close()

# Classe per la finestra (gest_pren_cli) -----------------
class GestionePrenotazoniCliente(QMainWindow):
    def __init__(self, previous_window):
        super(GestionePrenotazoniCliente, self).__init__()

        # Carica la finestra prenotazioni_cliente
        ui_file = os.path.join(os.path.dirname(__file__), "gest_pren_cli.ui")
        uic.loadUi(ui_file, self)

        # Memorizza la finestra precedente
        self.previous_window = previous_window

        # Collega il pulsante per aprire gest_pren_cli
        self.findChild(QPushButton, 'but_conferma').clicked.connect(self.but_enable)
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def but_enable(self):
        if self.lineEdit.text() == "MMS39P":
            self.but_visualizza.setEnabled(True)
            self.but_modifica. setEnabled (True)
            self.but_cancella. setEnabled (True)
        else:
            message = QMessageBox()
            message.setText("Prenotazione non trovata")
            message.exec()

    def open_indietro(self):
        # Mostra la finestra precedente
        self.previous_window.show()
        self.close()

# Classe per la finestra (menu) ---------------------------------------------------
class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()

        # Carica la finestra menu
        ui_file = os.path.join(os.path.dirname(__file__), "menu.ui")
        uic.loadUi(ui_file, self)
        # Imposta il QListWidget per non essere modificabile
        self.menu_list.setEditTriggers(QListWidget.NoEditTriggers)

        # Creazione di un menu leggendo dal file di testo
        menu = leggi_menu_da_file('Progetto copia/Qt/testo_menu.txt')

        # Set per tracciare le categorie già visualizzate
        categorie_visualizzate = set()

        # Popola la lista con categorie e piatti
        for piatto in menu.piatti:
            # Se la categoria del piatto non è stata ancora visualizzata, aggiungila
            if piatto.categoria not in categorie_visualizzate:
                # Aggiungi una riga vuota tra le categorie, tranne per la prima
                if categorie_visualizzate:
                    self.menu_list.addItem('')  # Riga vuota per separare le categorie
                
                # Aggiungi la categoria
                self.menu_list.addItem(piatto.categoria)
                categorie_visualizzate.add(piatto.categoria)  # Segna la categoria come visualizzata

            # Aggiungi il piatto sotto la categoria corretta
            self.menu_list.addItem(piatto.mostraPiatto())

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
        ui_file = os.path.join(os.path.dirname(__file__), "info.ui")
        uic.loadUi(ui_file, self)

        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'pushButton').clicked.connect(self.open_home_cliente)

        # Carica il testo da 'testo_info.txt' all'avvio
        self.load_text_from_file('Progetto copia/Qt/testo_info.txt')

        self.show()

    def open_home_cliente(self):
        self.cliente_window = HomeCliente()
        self.cliente_window.show()
        self.close()

    def load_text_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            # Imposta l'allineamento giustificato
            #self.textEdit.setAlignment(Qt.AlignJustify)
            self.textEdit.setPlainText(content)

# Classe per la finestra (login) --------------------------------------------------------------------------------------
class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()

        # Carica la finestra login
        ui_file = os.path.join(os.path.dirname(__file__), "login.ui")
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

        # Carica la finestra home_amministratore
        ui_file = os.path.join(os.path.dirname(__file__), "home_cameriere.ui")
        uic.loadUi(ui_file, self)

        # Collega il pulsante prenotazioni
        #self.findChild(QPushButton, 'prenotazioni').clicked.connect(self.open_prenotazioni)
        # Collega il pulsante nuovo_ordine
        self.findChild(QPushButton, 'nuovo_ordine').clicked.connect(self.open_ricerca)
        # Collega il pulsante aggiorna_ordine
        self.findChild(QPushButton, 'aggiorna_ordine').clicked.connect(self.open_ricerca)
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'logout').clicked.connect(self.open_indietro)

        self.show()

    def open_ricerca(self):
        self.cliente_window = RicercaTavolo()
        self.cliente_window.show()
        self.close()

    def open_indietro(self):
        self.cliente_window = Login()
        self.cliente_window.show()
        self.close()

# Classe per la finestra (cerca_tavolo)------------------
class RicercaTavolo(QMainWindow):
    def __init__(self):
        super(RicercaTavolo, self).__init__()

        # Carica la finestra cerca_tavolo
        ui_file = os.path.join(os.path.dirname(__file__), "cerca_tavolo.ui")
        uic.loadUi(ui_file, self)

        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def open_indietro(self):
        self.cliente_window = HomeCameriere()
        self.cliente_window.show()
        self.close()

# Classe per la finestra (home_amministratore)-----------------------------------------
class HomeAmministratore(QMainWindow):
    def __init__(self):
        super(HomeAmministratore, self).__init__()

        # Carica la finestra home_amministratore
        ui_file = os.path.join(os.path.dirname(__file__), "home_amministratore.ui")
        uic.loadUi(ui_file, self)

        # Collega il pulsante per aprire prenotazioni_cliente
        self.findChild(QPushButton, 'prenotazioni').clicked.connect(self.open_prenotazioni)
        # Collega il pulsante stampa_conto
        self.findChild(QPushButton, 'stampa').clicked.connect(self.open_stampa)
        # Collega il pulsante modifica
        self.findChild(QPushButton, 'modifica').clicked.connect(self.modifica_admin)
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'logout').clicked.connect(self.open_indietro)

        self.show()
        
    def open_prenotazioni(self):
        self.pren_cli_window = PrenotazoniCliente(self)
        self.pren_cli_window.show()
        self.close()

    def open_stampa(self):
        self.cliente_window = StampaConto()
        self.cliente_window.show()
        self.close()

    def modifica_admin(self):
        self.cliente_window = ModificaAdmin()
        self.cliente_window.show()
        self.close()

    def open_indietro(self):
        self.cliente_window = Login()
        self.cliente_window.show()
        self.close()

# Classe per la finestra (stampa_conto)------------------
class StampaConto(QMainWindow):
    def __init__(self):
        super(StampaConto, self).__init__()

        # Carica la finestra stampa_conto
        ui_file = os.path.join(os.path.dirname(__file__), "stampa_conto.ui")
        uic.loadUi(ui_file, self)

        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def open_indietro(self):
        self.cliente_window = HomeAmministratore()
        self.cliente_window.show()
        self.close()

# Classe per la finestra (modifica_admin)----------------
class ModificaAdmin(QMainWindow):
    def __init__(self):
        super(ModificaAdmin, self).__init__()

        # Carica la finestra modifica
        ui_file = os.path.join(os.path.dirname(__file__), "modifica_admin.ui")
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
        ui_file = os.path.join(os.path.dirname(__file__), "menu.ui")
        uic.loadUi(ui_file, self)

        # Creazione di un menu leggendo dal file di testo
        menu = leggi_menu_da_file('testo_menu.txt')

        # Set per tracciare le categorie già visualizzate
        categorie_visualizzate = set()

        # Popola la lista con categorie e piatti
        for piatto in menu.piatti:
            # Se la categoria del piatto non è stata ancora visualizzata, aggiungila
            if piatto.categoria not in categorie_visualizzate:
                # Aggiungi una riga vuota tra le categorie, tranne per la prima
                if categorie_visualizzate:
                    self.menu_list.addItem('')  # Riga vuota per separare le categorie
                
                # Aggiungi la categoria
                self.menu_list.addItem(piatto.categoria)
                categorie_visualizzate.add(piatto.categoria)  # Segna la categoria come visualizzata

            # Aggiungi il piatto sotto la categoria corretta
            self.menu_list.addItem(piatto.mostraPiatto())

        # Rende modificabile il testo e visibile il pulsante salva
        self.menu_list.setEnabled(True)
        self.salva.setGeometry(80, 380, 101, 31)
        # Collega il pulsante indietro e il pulsante salva
        self.findChild(QPushButton, 'salva').clicked.connect(self.salva_modifiche_al_file)
        self.findChild(QPushButton, 'pushButton').clicked.connect(self.modifica_admin)

        # Trova il QListWidget
        self.list_widget = self.findChild(QListWidget, 'menu_list')
        # Imposta i trigger di modifica, in questo caso doppio clic
        self.list_widget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)

        # Aggiungi il menu contestuale (clic destro)
        self.list_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.list_widget.customContextMenuRequested.connect(self.show_context_menu)

        self.show()

    # Funzione per il menu contestuale
    def show_context_menu(self, position):
        menu = QtWidgets.QMenu()

        # Imposta il foglio di stile
        menu.setStyleSheet("""
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

        add_action = menu.addAction("Aggiungi Elemento")
        edit_action = menu.addAction("Modifica Elemento")
        delete_action = menu.addAction("Elimina Elemento")

        action = menu.exec_(self.list_widget.viewport().mapToGlobal(position))

        if action == add_action:
            self.add_item()
        elif action == edit_action:
            self.edit_item()
        elif action == delete_action:
            self.delete_item()

    # Aggiungi un nuovo elemento alla lista
    def add_item(self):
        text, ok = QInputDialog.getText(self, 'Aggiungi Elemento', 'Inserisci il nome del nuovo elemento:')
        if ok and text:
            row = self.list_widget.currentRow()  # Ottieni la riga attualmente selezionata
            self.list_widget.insertItem(row, text)  # Inserisci l'elemento nella posizione selezionata

    # Modifica l'elemento selezionato
    def edit_item(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            dialog = QInputDialog(self)
            dialog.setWindowTitle('Modifica Elemento')
            dialog.setLabelText('Modifica il testo:')
            dialog.setTextValue(selected_item.text())
            
            # Imposta una dimensione maggiore per la finestra
            dialog.resize(400, 100)  # Modifica la dimensione del dialogo qui (larghezza, altezza)
            
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                new_text = dialog.textValue()
                if new_text:
                    selected_item.setText(new_text)

    # Elimina l'elemento selezionato
    def delete_item(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            self.list_widget.takeItem(self.list_widget.row(selected_item))

    def salva_modifiche_al_file(self):
        with open('testo_menu.txt', 'w') as file:
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

    def modifica_admin(self):
        self.cliente_window = ModificaAdmin()
        self.cliente_window.show()
        self.close()

# Classe per la finestra (modifica_info)
class ModificaInfo(QMainWindow):
    def __init__(self):
        super(ModificaInfo, self).__init__()

        # Carica la finestra menu
        ui_file = os.path.join(os.path.dirname(__file__), "info.ui")
        uic.loadUi(ui_file, self)

        # Rende modificabile il testo e visibile il pulsante salva
        self.textEdit.setEnabled(True)
        self.salva.setGeometry(70, 380, 101, 32)
        # Collega il pulsante indietro e il pulsante salva
        self.findChild(QPushButton, 'pushButton').clicked.connect(self.modifica_admin)
        self.findChild(QPushButton, 'salva').clicked.connect(self.salva_modifiche_al_file)

        # Carica il testo da 'testo_info.txt' all'avvio
        self.load_text_from_file('testo_info.txt')

        self.show()

    def modifica_admin(self):
        self.cliente_window = ModificaAdmin()
        self.cliente_window.show()
        self.close()

    def salva_modifiche_al_file(self):
        contenuto = self.textEdit.toPlainText()  # Ottiene il testo dal QTextEdit
        with open('testo_info.txt', 'w', encoding='utf-8') as file:
            file.write(contenuto)

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
