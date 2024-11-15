from PyQt5.QtWidgets import QMessageBox


# classe comanda -----------------------------------
class Comanda:
    def __init__(self):
        self.piatti = []
        self.prezzi = []
        self.totale = 0

    def genera_comanda(self, piatto, prezzo, quantita):
        self.piatti.append((piatto, quantita))
        self.prezzi.append(prezzo)
        self.totale += prezzo * quantita

    def aggiungi_piatto(self, parent):
        item_selezionato = parent.menu_list.currentItem()  # Ottieni l'elemento selezionato
        if item_selezionato:
            piatto_selezionato = item_selezionato.text()
            piatto_selezionato = piatto_selezionato.split(':')[0].strip() # Estrai solo il nome del piatto

            if piatto_selezionato in parent.menu_dict:
                prezzo = parent.menu_dict[piatto_selezionato]  # Trova il prezzo del piatto
                quantita = parent.quantita_spin.value()  # Ottieni la quantità
                parent.comanda_corrente.genera_comanda(piatto_selezionato, prezzo, quantita)
            else:
                message = QMessageBox()
                message.setText("Seleziona un piatto valido.")
                message.exec()

    def visualizza_comanda(self, parent):
        if parent.comanda_corrente.totale == 0:
            message = QMessageBox()
            message.setText("Comanda vuota")
            message.exec()
        else:
            descrizione = "Descrizione comanda \n"
            for piatto, quantita in parent.comanda_corrente.piatti:
                descrizione += f" - {piatto} x{quantita} \n"
            message = QMessageBox()
            message.setText(descrizione)
            message.exec()
