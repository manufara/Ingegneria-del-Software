import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# Crea una classe per la finestra principale
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Imposta il layout verticale
        layout = QVBoxLayout()

        # Crea una QLabel per visualizzare del testo
        label = QLabel('Benvenuto in PyQt5!', self)

        # Aggiungi la QLabel al layout
        layout.addWidget(label)

        # Imposta il layout per la finestra
        self.setLayout(layout)

        # Imposta il titolo della finestra
        self.setWindowTitle('PyQt5 con Testo')
        self.setGeometry(100, 100, 300, 200)  # Posizione e dimensione della finestra

# Avvio dell'applicazione PyQt5
app = QApplication(sys.argv)

# Crea un'istanza della finestra
window = MyWindow()
window.show()

# Avvia il ciclo di eventi
sys.exit(app.exec_())
