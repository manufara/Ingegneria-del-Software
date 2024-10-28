from Tavolo import crea_tavoli
from Database import database
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime


class GestoreTavoli:

    def visualizza_lista_tavoli(giorno_selezionato, servizio_selezionato, tavoli_list):
            # Pulire la lista prima di popolarla
            tavoli_list.clear()

            # Controlla che tutti i campi siano riempiti
            if not giorno_selezionato or not servizio_selezionato:
                message = QMessageBox()
                message.setText("Assicurati di specificare giorno e servizio.")
                message.exec()
                return
            
            # Converti il giorno in oggetto datetime    
            giorno_selezionato = datetime.strptime(giorno_selezionato, "%d/%m/%Y").date()

            # Crea una lista di tutti i tavoli disponibili (20 tavoli)
            tavoli = crea_tavoli()

            for giorno, servizi in database.dati_prenotazioni.items():
                for servizio, prenotazioni in servizi.items():
                    for prenotazione in prenotazioni:
                        if prenotazione.giorno == giorno_selezionato and prenotazione.servizio == servizio_selezionato:
                            for tavolo_assegnato in prenotazione.tavoli_assegnati:
                                # Cerca il tavolo nella lista dei tavoli creati da creaTavoli
                                for tavolo in tavoli:
                                    if tavolo.nrTavolo == tavolo_assegnato.nrTavolo:
                                        tavolo.occupato = True
                                        tavolo.prenotazione = prenotazione.codice

            # Popola il listWidget con i tavoli e il loro stato
            for tavolo in tavoli:
                if tavolo.occupato is True:
                    # Mostra il tavolo come occupato e il codice della prenotazione
                    item_text = f"Tavolo {tavolo.nrTavolo} - Occupato (Codice: {tavolo.prenotazione})"
                    # Aggiungi l'elemento al listWidget
                    tavoli_list.addItem(item_text)
                else:
                    # Mostra il tavolo come libero
                    item_text = f"Tavolo {tavolo.nrTavolo} - Libero"
                    tavoli_list.addItem(item_text)

    def compatta_tavoli(giorno, servizio):
        # Ottieni le prenotazioni e la lista di tavoli per il giorno e il servizio specificati
        prenotazioni = database.dati_prenotazioni[giorno][servizio]
        tavoli = database.dati_tavoli[giorno][servizio]

        # Salva tutte le prenotazioni esistenti in una variabile temporanea
        prenotazioni_da_riscrivere = prenotazioni.copy()

        # Cancella tutte le prenotazioni esistenti e libera i tavoli
        prenotazioni.clear()
        GestoreTavoli.libera_tavoli(tavoli)

        # Ad ogni prenotazione salvata riassegna i tavoli
        for prenotazione in prenotazioni_da_riscrivere:
            tavoli_assegnati = []
            persone_da_sistemare = prenotazione.numero_persone
            for tavolo in tavoli:
                if not tavolo.occupato:
                    tavolo.occupato = True
                    tavolo.prenotazione = prenotazione.codice
                    tavoli_assegnati.append(tavolo)
                    persone_da_sistemare -= tavolo.capacita
                    if persone_da_sistemare <= 0:
                        break
            
            # Cambia i tavoli assegnati alla prenotazione e la aggiunge alla lista
            prenotazione.tavoli_assegnati = tavoli_assegnati
            database.dati_prenotazioni[giorno][servizio].append(prenotazione)

    def libera_tavoli(tavoli):
        for tavolo in tavoli:
            tavolo.occupato = False
            tavolo.prenotazione = None

    #questa funzione non assegna propriamente i tavoli ma ritorna una lista di tavoli, che poi AssegnaPrenotazione utilizzerà
    #fornisce la lista di tavoli da attribuire alla prenotazione
    # def assegna_tavolo(self, prenotazione)
