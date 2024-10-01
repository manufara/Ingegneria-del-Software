import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget
from Qt.menu_class import MenuClass, Piatto

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
                piatto = Piatto(categoria_corrente, nome, descrizione.strip(), prezzo.strip())  # Crea un oggetto Piatto
                piatti.append(piatto)  # Aggiungi l'oggetto Piatto alla lista
            except ValueError:
                print(f"Errore nel formato della riga: {linea}")

    menu = MenuClass(piatti)  # Crea un oggetto MenuClass con i piatti
    return menu

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
        # Imposta il layout
        self.setLayout(layout)


        # Set per tracciare le categorie già visualizzate
        categorie_visualizzate = set()

        # Popola la lista con categorie e piatti
        for piatto in menu.piatti:
            # Se la categoria del piatto non è stata ancora visualizzata, aggiungila
            if piatto.categoria not in categorie_visualizzate:
                # Aggiungi una riga vuota tra le categorie, tranne per la prima
                if categorie_visualizzate:
                    self.menu_list.addItem('')  # Riga vuota per separare le categorie
                
                # Aggiungi la categoria
                self.menu_list.addItem(piatto.categoria)
                categorie_visualizzate.add(piatto.categoria)  # Segna la categoria come visualizzata

            # Aggiungi il piatto sotto la categoria corretta
            self.menu_list.addItem(piatto.mostraPiatto())

# Creazione di un menu leggendo dal file di testo
menu = leggi_menu_da_file('Progetto copia/Qt/testo_menu.txt')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuWindow(menu)
    window.show()
    sys.exit(app.exec_())
