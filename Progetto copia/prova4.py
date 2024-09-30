import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget
from prova import MenuClass, Piatto

# Funzione per leggere il menu da un file con categorie e piatti e creare oggetti Piatto e MenuClass
def leggi_menu_da_file(file_path):
    piatti = []  # Lista che conterrà oggetti Piatto
    categoria_corrente = None  # Per tenere traccia della categoria attuale
    
    with open(file_path, 'r') as file:
        for linea in file:
            linea = linea.strip()
            
            # Ignora le righe vuote
            if not linea:
                continue
            
            # Se la riga non contiene una virgola, la trattiamo come categoria
            if ',' not in linea:
                categoria_corrente = linea  # Aggiorna la categoria corrente
                continue
            
            # Se la riga contiene una virgola, la trattiamo come piatto
            try:
                nome, descrizione, prezzo = linea.split(',')
                nome = f"{categoria_corrente}: {nome.strip()}"  # Aggiungi la categoria al nome del piatto
                piatto = Piatto(nome, descrizione.strip(), float(prezzo.strip()))  # Crea un oggetto Piatto
                print(f"Piatto creato: {piatto.mostraPiatto()}")
                piatti.append(piatto)  # Aggiungi l'oggetto Piatto alla lista
            except ValueError:
                print(f"Errore nel formato della riga: {linea}")
    
    return MenuClass(piatti)  # Crea un oggetto MenuClass con i piatti

class MenuWindow(QWidget):
    def __init__(self, menu):
        super().__init__()

        # Configura la finestra
        self.setWindowTitle("Menu")
        self.setGeometry(100, 100, 300, 400)

        # Layout
        layout = QVBoxLayout()

        # Etichetta "Menu"
        title = QLabel("Menu")
        layout.addWidget(title)

        # Lista per mostrare le categorie e i piatti
        self.menu_list = QListWidget()
        layout.addWidget(self.menu_list)

        # Popola la lista con categorie e piatti
        for piatto in menu.piatti:
            self.menu_list.addItem(piatto.mostraPiatto())

        self.setLayout(layout)

# Creazione di un menu leggendo dal file di testo
file_menu = 'Progetto copia/m.txt'
menu = leggi_menu_da_file(file_menu)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuWindow(menu)
    window.show()
    sys.exit(app.exec_())
