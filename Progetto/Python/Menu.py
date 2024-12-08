from Piatto import Piatto
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets, QtCore


# classe menu -------------------------------------
class MenuClass():
    def __init__(self, piatti):
        self.piatti = piatti

    def mostra_menu(self, menu_list):
        categorie_visualizzate = set() # Set per tracciare le categorie già visualizzate
        
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

            menu_list.addItem(piatto.mostraPiatto()) # Aggiungi il piatto sotto la categoria corretta

    def modifica_menu(self, list_widget, action):
        if action == 'aggiungi' or action == 'modifica':
            # Seleziona il piatto da modificare (se action è 'modifica')
            nome, descrizione, prezzo = "", "", ""
            if action == 'modifica':
                selected_item = list_widget.currentItem()
                if selected_item:
                    testo_corrente = selected_item.text()

                    # Se la riga è vuota o è una categoria, esci dalla funzione
                    if ':' not in testo_corrente:
                        message = QMessageBox()
                        message.setText("Seleziona un piatto.")
                        message.exec()
                        return

                    try:
                        # Estrai nome, descrizione e prezzo dal testo corrente
                        nome, resto = testo_corrente.split(": ")
                        descrizione, prezzo = resto.rsplit(" - ", 1)
                        prezzo = prezzo.replace("€", "")
                    except ValueError:
                        pass  # Se il parsing fallisce, lascia i campi vuoti

            # Crea un dialog con tre campi di input
            dialog = QtWidgets.QDialog()
            dialog.setWindowTitle('Aggiungi Piatto' if action == 'aggiungi' else 'Modifica Piatto')
            dialog.resize(320, 170) # Imposta le dimensioni del dialog
            
            # LineEdit per nome, descrizione e prezzo
            nome_edit = QtWidgets.QLineEdit(nome)
            descrizione_edit = QtWidgets.QLineEdit(descrizione)
            prezzo_edit = QtWidgets.QLineEdit(prezzo)

            # Imposta la larghezza dei lineEdit in base alla larghezza del dialog
            fixed_width = dialog.width() * 0.8
            nome_edit.setFixedWidth(fixed_width)
            descrizione_edit.setFixedWidth(fixed_width)
            prezzo_edit.setFixedWidth(fixed_width)
            
            layout = QtWidgets.QFormLayout(dialog)
            layout.addRow("Nome:", nome_edit)
            layout.addRow("Descrizione:", descrizione_edit)
            layout.addRow("Prezzo:", prezzo_edit)
            
            # Pulsanti conferma e annulla
            buttons = QtWidgets.QDialogButtonBox(
                QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
                QtCore.Qt.Horizontal,
                dialog
            )
            buttons.accepted.connect(dialog.accept)
            buttons.rejected.connect(dialog.reject)
            layout.addRow(buttons)
            
            # Mostra il dialogo e recupera i dati se l'utente preme OK
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                nuovo_nome = nome_edit.text()
                nuova_descrizione = descrizione_edit.text()
                nuovo_prezzo = prezzo_edit.text()
                if nuovo_nome and nuova_descrizione and nuova_descrizione:
                    nuovo_testo = f"{nuovo_nome}: {nuova_descrizione} - {nuovo_prezzo}€"
                    
                    if action == 'aggiungi':
                        row = list_widget.currentRow()
                        list_widget.insertItem(row, nuovo_testo)
                    elif action == 'modifica' and selected_item:
                        selected_item.setText(nuovo_testo)

        elif action == 'elimina':
            selected_item = list_widget.currentItem()
            if selected_item:
                testo_corrente = selected_item.text()

                # Se la riga è vuota o è una categoria, esci dalla funzione
                if ':' not in testo_corrente:
                    message = QMessageBox()
                    message.setText("Seleziona un piatto.")
                    message.exec()
                    return

                list_widget.takeItem(list_widget.row(selected_item)) # Altrimenti procedi con l'eliminazione

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

        self.piatti = piatti # Assegna i piatti letti all'attributo dell'istanza


menu = MenuClass([])
