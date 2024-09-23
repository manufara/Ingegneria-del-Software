import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from cliente_window import ClienteWindow  # Import della finestra Cliente
from dipendente_window import DipendenteWindow  # Import della finestra Dipendente

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Creazione layout
        layout = QVBoxLayout()

        # Creazione pulsanti
        self.button_cliente = QPushButton('Cliente')
        self.button_cliente.clicked.connect(self.open_cliente_window)  # Collegamento pulsante Cliente

        self.button_dipendente = QPushButton('Dipendente')
        self.button_dipendente.clicked.connect(self.open_dipendente_window)  # Collegamento pulsante Dipendente

        # Aggiunta pulsanti al layout
        layout.addWidget(self.button_cliente)
        layout.addWidget(self.button_dipendente)

        # Impostazione layout della finestra principale
        self.setLayout(layout)
        self.setWindowTitle('Esempio Cliente e Dipendente')
        self.setGeometry(100, 100, 200, 150)

    # Metodo per aprire la finestra Cliente
    def open_cliente_window(self):
        self.cliente_window = ClienteWindow()
        self.cliente_window.show()

    # Metodo per aprire la finestra Dipendente
    def open_dipendente_window(self):
        self.dipendente_window = DipendenteWindow()
        self.dipendente_window.show()

# Punto di ingresso dell'applicazione
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Creazione dell'istanza QApplication
    window = MainWindow()  # Creazione della finestra principale
    window.show()  # Visualizza la finestra principale
    sys.exit(app.exec_())  # Esecuzione del ciclo dell'applicazione
