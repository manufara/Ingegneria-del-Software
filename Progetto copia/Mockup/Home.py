import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

# Finestra Cliente
class ClienteWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Finestra Cliente')
        self.setGeometry(100, 100, 200, 100)

        # Layout e contenuto della finestra Cliente
        layout = QVBoxLayout()
        label = QLabel('Sei nella finestra Cliente')
        layout.addWidget(label)
        self.setLayout(layout)

# Finestra Dipendente
class DipendenteWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Finestra Dipendente')
        self.setGeometry(100, 100, 200, 100)

        # Layout e contenuto della finestra Dipendente
        layout = QVBoxLayout()
        label = QLabel('Sei nella finestra Dipendente')
        layout.addWidget(label)
        self.setLayout(layout)

# Finestra principale
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

# Avvio dell'applicazione PyQt5
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
