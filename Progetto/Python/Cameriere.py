from PyQt5.QtWidgets import QMessageBox


# classe cameriere ----------------------------------
class Cameriere:
    def __init__(self, id):
        self.id = id
        self.password = "Emilia"
        self.tavoli = []

    # Assegna il cameriere al tavolo e viceversa, e crea l'ordine relativo al tavolo
    def assegna_cameriere(self, tavolo_selezionato):
        from Database import database
        from Ordinazione import Ordinazione

        self.tavolo = tavolo_selezionato

        # Se ci sono clienti al tavolo
        if self.tavolo.occupato is True:
            # Se il tavolo non è assegnato a nessun cameriere
            assegnato = False
            for cameriere in database.lista_camerieri: # Cicla su tutti i camerieri per vedere se qualcuno ha il tavolo come assegnato
                for tavolo in cameriere.tavoli:
                    if tavolo.nrTavolo == self.tavolo.nrTavolo:
                        assegnato = True

            if assegnato == False:
                msg_box = QMessageBox()
                msg_box.setText(f"Confermi di volerti assegnare al tavolo {self.tavolo.nrTavolo}?")

                # Crea i pulsanti personalizzati
                conferma_button = msg_box.addButton("Conferma", QMessageBox.YesRole)
                annulla_button = msg_box.addButton("Annulla", QMessageBox.NoRole)
                msg_box.setDefaultButton(conferma_button) # Imposta "Conferma" come pulsante predefinito
                msg_box.exec_() # Mostra il messaggio e attendi la risposta

                # Controlla quale pulsante è stato premuto
                if msg_box.clickedButton() == conferma_button:
                    self.tavoli.append(self.tavolo)
                    # Crea ordinazione vuota
                    if self.tavolo.ordinazione is None:
                        self.tavolo.ordinazione = Ordinazione(self.tavolo.nrTavolo)
                        return
                    
                elif msg_box.clickedButton() == annulla_button:
                    return

            # Se il tavolo ha gia un cameriere
            else:
                cameriere_assegnato = None
                for cameriere in database.lista_camerieri:
                    for tavolo in cameriere.tavoli:
                        if tavolo.nrTavolo == self.tavolo.nrTavolo:
                            cameriere_assegnato = cameriere.id

                # Assegnato allo stesso
                if cameriere_assegnato == self.id:
                    msg_box = QMessageBox()
                    msg_box.setText(f"Il tavolo {self.tavolo.nrTavolo} è gia assegnato a te.")
                    msg_box.exec_()
                    return
                # Assegnato ad un altro
                else:
                    msg_box = QMessageBox()
                    msg_box.setText(f"Il tavolo {self.tavolo.nrTavolo} è già assegnato al cameriere {cameriere_assegnato}.")
                    msg_box.exec_()
                    return
                
        # Se il tavolo non è occupato, mostra un messaggio di errore
        else:
            msg_box = QMessageBox()
            msg_box.setText(f"Il tavolo {self.tavolo.nrTavolo} non è occupato da nessun cliente.")
            msg_box.exec_()
