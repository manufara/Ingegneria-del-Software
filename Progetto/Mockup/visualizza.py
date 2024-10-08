import os
from PyQt5.QtWidgets import *
from PyQt5 import uic

class HomePage(QMainWindow):
    def __init__(self):
        super(HomePage, self).__init__()

        ui_file = os.path.join(os.path.dirname(__file__), "crea_ordinazione.ui")
        uic.loadUi(ui_file, self)

        self.findChild(QPushButton, 'but_conferma').clicked.connect(self.autenticazione)

        self.show()

    def autenticazione(self):
        if False:
            return
        else:
            message = QMessageBox()
            message.setText("Tavolo 1 \n\nAntipasto di mare misto \nTagliatelle allo scoglio \nGnocchi ai frutti di mare \n\nConfermi?")
            message.exec()

# Funzione principale
def main():
    app = QApplication([])
    # Avvia la prima finestra (home_page)
    window = HomePage()
    app.exec()

if __name__ == '__main__':
    main()
