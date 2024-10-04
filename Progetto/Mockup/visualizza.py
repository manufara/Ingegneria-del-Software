import os
from PyQt5.QtWidgets import *
from PyQt5 import uic

class HomePage(QMainWindow):
    def __init__(self):
        super(HomePage, self).__init__()

        # Carica la finestra home_page
        ui_file = os.path.join(os.path.dirname(__file__), "home_amministratore.ui")
        uic.loadUi(ui_file, self)

        self.show()

# Funzione principale
def main():
    app = QApplication([])
    # Avvia la prima finestra (home_page)
    window = HomePage()
    app.exec()

if __name__ == '__main__':
    main()
