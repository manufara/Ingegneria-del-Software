import random, string
from PyQt5.QtWidgets import QMessageBox


# classe prenotazione ----------------------------
class Prenotazione:
    def __init__(self, nome, giorno, servizio, numero_persone, codice):
        self.nome = nome
        self.giorno = giorno
        self.servizio = servizio
        self.numero_persone = numero_persone
        self.codice = codice
        self.tavoli_assegnati = []

    def genera_codice_univoco(prenotazioni_salvate):
        codici_esistenti = set()
        
        # Estrarre i codici dalle prenotazioni salvate
        for data, servizi in prenotazioni_salvate.items():
            for servizio, lista_prenotazioni in servizi.items():
                for prenotazione in lista_prenotazioni:
                    codici_esistenti.add(prenotazione.codice)
        
        # Genera un codice finché non è univoco
        while True:
            nuovo_codice = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            if nuovo_codice not in codici_esistenti:
                return nuovo_codice

    def mostra_prenotazione(codice_inserito, prenotazioniservizio):
        for giorno, servizi in prenotazioniservizio.items():  # Itera per ogni data
            for servizio, prenotazioni in servizi.items():  # Itera per ogni servizio
                for prenotazione in prenotazioni:  # Itera sulle prenotazioni
                    if prenotazione.codice == codice_inserito:
                        # Crea il messaggio con i dati della prenotazione
                        data_formattata = giorno.strftime("%d/%m/%Y")
                        message = QMessageBox()
                        message.setText(f"Dati relativi alla prenotazione {codice_inserito} \nNome - {prenotazione.nome} \nGiorno - {data_formattata} \nServizio - {prenotazione.servizio.capitalize()} \nNumero persone - {prenotazione.numero_persone}")
                        message.exec()
                        return
