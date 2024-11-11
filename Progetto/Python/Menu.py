from Piatto import Piatto
from PyQt5.QtWidgets import QInputDialog
from PyQt5 import QtWidgets


# classe menu -------------------------------------
class MenuClass():
    def __init__(self, piatti):
        self.piatti = piatti

    def mostra_menu(self, menu_list):

        # Set per tracciare le categorie già visualizzate
        categorie_visualizzate = set()
        
        # Popola la lista con categorie e piatti
        for piatto in menu.piatti:
            # Se la categoria del piatto non è stata ancora visualizzata, aggiungila
            if piatto.categoria not in categorie_visualizzate:
                # Aggiungi una riga vuota tra le categorie, tranne per la prima
                if categorie_visualizzate:
                    menu_list.addItem('')  # Riga vuota per separare le categorie
                
                # Aggiungi la categoria
                menu_list.addItem(piatto.categoria)
                categorie_visualizzate.add(piatto.categoria)  # Segna la categoria come visualizzata

            # Aggiungi il piatto sotto la categoria corretta
            menu_list.addItem(piatto.mostraPiatto())

    def modifica_menu(self, list_widget, action):
        if action == 'aggiungi':
            text, ok = QInputDialog.getText(None, 'Aggiungi Elemento', 'Inserisci i dati del nuovo piatto:')
            if ok and text:
                row = list_widget.currentRow()  # Ottieni la riga attualmente selezionata
                list_widget.insertItem(row, text)  # Inserisci l'elemento nella posizione selezionata
        
        elif action == 'modifica':
            selected_item = list_widget.currentItem()
            if selected_item:
                dialog = QInputDialog()
                dialog.setWindowTitle('Modifica Elemento')
                dialog.setLabelText('Modifica i dati del piatto:')
                dialog.setTextValue(selected_item.text())
                
                # Imposta una dimensione maggiore per la finestra
                dialog.resize(400, 100)  # Modifica la dimensione del dialogo qui (larghezza, altezza)
                
                if dialog.exec_() == QtWidgets.QDialog.Accepted:
                    new_text = dialog.textValue()
                    if new_text:
                        selected_item.setText(new_text)

        elif action == 'elimina':
            selected_item = list_widget.currentItem()
            if selected_item:
                list_widget.takeItem(list_widget.row(selected_item))

    # Funzione per leggere il menu da un file con categorie e piatti
    def leggi_menu_da_file(self, file_path):
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

        # Assegna i piatti letti all'attributo dell'istanza
        self.piatti = piatti

menu = MenuClass([])
