import os
from PyQt5.QtWidgets import *
from PyQt5 import uic

class HomePage(QMainWindow):
    def __init__(self):
        super(HomePage, self).__init__()

        # Carica la finestra home_page
        ui_file = os.path.join(os.path.dirname(__file__), "stampa_conto.ui")
        uic.loadUi(ui_file, self)

        self.findChild(QPushButton, 'pushButton').clicked.connect(self.autenticazione)

        self.show()

    def autenticazione(self):
        if False:
            return
        else:
            message = QMessageBox()
            message.setText("Descrizione \nAntipasto di mare misto - 16 \nTagliatelle allo scoglio - 12 \nGnocchi ai frutti di mare - 13 \nSorbetto al limone - 5 \nTiramisu - 6 \n\nTotale - 52€")
            message.exec()

# Funzione principale
def main():
    app = QApplication([])
    # Avvia la prima finestra (home_page)
    window = HomePage()
    app.exec()

if __name__ == '__main__':
    main()
