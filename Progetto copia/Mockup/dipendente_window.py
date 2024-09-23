from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

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
