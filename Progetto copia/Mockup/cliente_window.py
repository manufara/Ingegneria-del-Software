from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

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
