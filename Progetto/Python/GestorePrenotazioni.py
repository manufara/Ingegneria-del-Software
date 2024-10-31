from Database import database
from Prenotazione import Prenotazione
from GestoreTavoli import GestoreTavoli
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime


class GestorePrenotazioni:

    def crea_prenotazione(parent, messaggio):
        dati_prenotazioni = database.dati_prenotazioni
        dati_tavoli = database.dati_tavoli
        nome = parent.nome_line.text().strip()
        giorno = parent.lineEdit_giorno.text()
        servizio = "pranzo" if parent.pranzo_check.isChecked() else ("cena" if parent.cena_check.isChecked() else "")
        numero_persone = parent.persone_spin.value()

        # Controlla che tutti i campi siano riempiti
        if not nome or not giorno or not servizio:
            message = QMessageBox()
            message.setText("Assicurati di specificare nome, giorno e servizio.")
            message.exec()
            return

        # Converte la stringa 'giorno' in oggetto datetime.date
        giorno_selezionato = datetime.strptime(giorno, "%d/%m/%Y").date()
        # Genera un codice univoco di 6 caratteri, composto da lettere maiuscole e cifre
        if hasattr(parent, 'codice_inserito') and parent.codice_inserito:
            codice = parent.codice_inserito
        else:
            codice = Prenotazione.genera_codice_univoco(dati_prenotazioni)
        
        # Verifica che il giorno selezionato esista nel dizionario
        # (controllo non necessario perché il calendario permette di selezionare solo date valide)
        try:
            tavoli_disponibili = dati_tavoli[giorno_selezionato][servizio]
        except KeyError:
            message = QMessageBox()
            message.setText("Assicurati di selezionare un giorno valido.")
            message.exec()
            return

        persone_da_sistemare = numero_persone

        # Verifica la disponibilità dei tavoli
        if not GestoreTavoli.verifica_disponibilita_tavoli(tavoli_disponibili, persone_da_sistemare):
            return
        
        # Assegna i tavoli disponibili
        tavoli_assegnati = GestoreTavoli.assegna_tavoli(tavoli_disponibili, persone_da_sistemare, codice)
        
        # Crea l'oggetto prenotazione e assegna i tavoli
        prenotazione = Prenotazione(nome, giorno_selezionato, servizio, numero_persone, codice)
        GestorePrenotazioni.assegna_prenotazione(prenotazione, tavoli_assegnati)

        dati_prenotazioni[giorno_selezionato][servizio].append(prenotazione)
        database.salva_dati()
        
        if messaggio is True:
            message = QMessageBox()
            data_formattata = prenotazione.giorno.strftime("%d/%m/%Y")
            message.setText(f"Modifica avvenuta con successo. \nPrenotazione confermata a nome {prenotazione.nome} per {prenotazione.numero_persone} il {data_formattata} a {prenotazione.servizio}. \nCodice: {prenotazione.codice}")
            message.exec()
        else:
            # Conferma della prenotazione
            message = QMessageBox()
            message.setText(f"Prenotazione confermata a nome {nome} per {numero_persone} il {giorno} a {servizio}. \nCodice: {prenotazione.codice}")
            message.exec()

    def modifica_prenotazione(parent):
        nome = parent.nome_line.text().strip()
        giorno = parent.lineEdit_giorno.text()
        servizio_selezionato = "pranzo" if parent.pranzo_check.isChecked() else ("cena" if parent.cena_check.isChecked() else "")
        numero_persone = parent.persone_spin.value()
        codice_inserito = parent.codice_inserito

        # Controlla che tutti i campi siano riempiti
        if not nome or not giorno or not servizio_selezionato:
            message = QMessageBox()
            message.setText("Assicurati di specificare nome, giorno e servizio.")
            message.exec()
            return

        # Converte la stringa 'giorno' in oggetto datetime.date
        giorno_selezionato = datetime.strptime(giorno, "%d/%m/%Y").date()
        persone_da_sistemare = numero_persone
        tavoli_disponibili = database.dati_tavoli[giorno_selezionato][servizio_selezionato]

    # Nel caso sia stato cambiato solo il numero di persone e i tavoli assegnati siano sufficienti
        for giorno, servizi in database.dati_prenotazioni.items():  # Itera per ogni data
            for servizio, prenotazioni in servizi.items():  # Itera per ogni servizio
                for prenotazione in prenotazioni:  # Itera sulle prenotazioni
                    if prenotazione.codice == codice_inserito: # Trova la vecchia prenotazione
                        if prenotazione.giorno == giorno_selezionato and prenotazione.servizio == servizio_selezionato:
                            if len(prenotazione.tavoli_assegnati) * 4 >= numero_persone:
                                # Viene cambiato solamente il numero di persone
                                prenotazione.numero_persone = numero_persone
                                GestoreTavoli.compatta_tavoli(giorno, servizio)
                                database.salva_dati()

                                message = QMessageBox()
                                data_formattata = prenotazione.giorno.strftime("%d/%m/%Y")
                                message.setText(f"Modifica avvenuta con successo. \nPrenotazione confermata a nome {prenotazione.nome} per {prenotazione.numero_persone} il {data_formattata} a {prenotazione.servizio}. \nCodice: {prenotazione.codice}")
                                message.exec()
                                return
                            else:
                                break
                        else:
                            break 

    # Nel caso vengano cambiati il giorno o il servizio, oppure i tavoli assegnati non siano sufficienti al numero
        # di persone. Se c'è disponibilità viene cancellata la vecchia prenotazione e se ne crea una nuova
        if not GestoreTavoli.verifica_disponibilita_tavoli(tavoli_disponibili, persone_da_sistemare):
            return
        
        GestorePrenotazioni.elimina_prenotazione(parent, True)
        GestorePrenotazioni.crea_prenotazione(parent, True)

    def elimina_prenotazione(parent, messaggio):
        codice_inserito = parent.codice_inserito

        # Trova e rimuovi la prenotazione corrispondente al codice
        for giorno, servizi in database.dati_prenotazioni.items():
            for servizio, prenotazioni in servizi.items():
                for prenotazione in prenotazioni:
                    if prenotazione.codice == codice_inserito:
                        prenotazioni.remove(prenotazione)  # Rimuove la prenotazione dalla lista

                        # Compatta i tavoli di un dato giorno e servizio per eliminare i buchi
                        GestoreTavoli.compatta_tavoli(giorno, servizio)
                        # Salva le prenotazioni aggiornate nel file pickle
                        database.salva_dati()

                        if messaggio is False:
                            message = QMessageBox()
                            message.setText(f"Prenotazione con codice {codice_inserito} eliminata con successo.")
                            message.exec()
                            return  # Esci dalla funzione dopo la cancellazione

    def assegna_prenotazione(prenotazione, tavoli_assegnati):
        prenotazione.tavoli_assegnati = tavoli_assegnati
