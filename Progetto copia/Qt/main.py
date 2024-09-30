import os
#from menu_class import Piatto, MenuClass, Comanda
from PyQt5.QtWidgets import *
from PyQt5 import uic


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
        self.pren_cli_window = PrenotazoniCliente()
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
    def __init__(self):
        super(PrenotazoniCliente, self).__init__()

        # Carica la finestra prenotazioni_cliente
        ui_file = os.path.join(os.path.dirname(__file__), "prenotazioni_cliente.ui")
        uic.loadUi(ui_file, self)

        # Collega il pulsante per aprire prenota_cli
        self.findChild(QPushButton, 'pushButton').clicked.connect(self.open_prenota_cliente)
        # Collega il pulsante per aprire gest_pren_cli
        self.findChild(QPushButton, 'pushButton_2').clicked.connect(self.open_gest_cli)
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_home_cliente)

        self.show()

    def open_gest_cli(self):
        self.gest_pren_cli = GestionePrenotazoniCliente()
        self.gest_pren_cli.show()
        self.close()

    def open_prenota_cliente(self):
        self.prenota_cli = PrenotaCliente()
        self.prenota_cli.show()
        self.close()

    def open_home_cliente(self):
        self.cliente_window = HomeCliente()
        self.cliente_window.show()
        self.close()

# Classe per la finestra (prenota) ----------------------
class PrenotaCliente(QMainWindow):
    def __init__(self):
        super(PrenotaCliente, self).__init__()

        # Carica la finestra prenota
        ui_file = os.path.join(os.path.dirname(__file__), "prenota.ui")
        uic.loadUi(ui_file, self)

        # Crea un gruppo di pulsanti, aggiunge le checkbox al gruppo e rende il gruppo mutualmente esclusivo
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.checkBox)
        self.button_group.addButton(self.checkBox_2)
        self.button_group.setExclusive(True)

        # Collega il pulsante di conferma prenotazione
        #self.findChild(QPushButton, 'pushButton').clicked.connect(self.----------)
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def open_indietro(self):
        self.cliente_window = PrenotazoniCliente()
        self.cliente_window.show()
        self.close()

# Classe per la finestra (gest_pren_cli) -----------------
class GestionePrenotazoniCliente(QMainWindow):
    def __init__(self):
        super(GestionePrenotazoniCliente, self).__init__()

        # Carica la finestra prenotazioni_cliente
        ui_file = os.path.join(os.path.dirname(__file__), "gest_pren_cli.ui")
        uic.loadUi(ui_file, self)

        # Collega il pulsante per aprire gest_pren_cli
        self.findChild(QPushButton, 'but_conferma').clicked.connect(self.but_enable)
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'indietro').clicked.connect(self.open_indietro)

        self.show()

    def but_enable(self):
        if self.lineEdit.text() == "aaa":
            self.but_visualizza.setEnabled(True)
            self.but_modifica. setEnabled (True)
            self.but_cancella. setEnabled (True)
        else:
            message = QMessageBox()
            message.setText("Prenotazione non trovata")
            message.exec()

    def open_indietro(self):
        self.cliente_window = PrenotazoniCliente()
        self.cliente_window.show()
        self.close()

# Classe per la finestra (menu) ---------------------------------------------------
class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()

        # Carica la finestra menu
        ui_file = os.path.join(os.path.dirname(__file__), "menu.ui")
        uic.loadUi(ui_file, self)

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

        self.show()

# Classe per la finestra (home_amministratore)-----------------------------------------
class HomeAmministratore(QMainWindow):
    def __init__(self):
        super(HomeAmministratore, self).__init__()

        # Carica la finestra home_amministratore
        ui_file = os.path.join(os.path.dirname(__file__), "home_amministratore.ui")
        uic.loadUi(ui_file, self)

        # Collega il pulsante modifica
        self.findChild(QPushButton, 'modifica').clicked.connect(self.modifica_admin)
        # Collega il pulsante per tornare indietro
        self.findChild(QPushButton, 'logout').clicked.connect(self.open_indietro)

        self.show()

    def modifica_admin(self):
        self.cliente_window = ModificaAdmin()
        self.cliente_window.show()
        self.close()

    def open_indietro(self):
        self.cliente_window = Login()
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

        # Rende modificabile il testo e visibile il pulsante salva
        self.textEdit.setEnabled(True)
        self.salva.setGeometry(80, 380, 101, 31)
        # Collega il pulsante indietro
        self.findChild(QPushButton, 'pushButton').clicked.connect(self.modifica_admin)

        self.show()

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
        self.load_text_from_file('Progetto copia/Qt/testo_info.txt')

        self.show()

    def modifica_admin(self):
        self.cliente_window = ModificaAdmin()
        self.cliente_window.show()
        self.close()

    # Aggiungi questo metodo nella tua classe MainWindow
    def salva_modifiche_al_file(self):
        contenuto = self.textEdit.toPlainText()  # Ottiene il testo dal QTextEdit
        with open('Progetto copia/Qt/testo_info.txt', 'w', encoding='utf-8') as file:
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
