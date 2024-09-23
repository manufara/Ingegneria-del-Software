import GestorePrenotazioni


class Prenotazione:
    def __init__(self, nome, pax, giorno, servizio,):
        self.nome = nome
        self.pax = pax
        self.giorno = giorno
        self.servizio=servizio
        self.codPre=self.genera_codice_prenotazione()

        self.tavoli = []
        self.note = None

    def genera_codice_prenotazione(self):
        prima_lettera_nome = self.nome[0].upper()
        numero_persone = str(self.pax)
        prime_due_lettere_giorno = self.giorno[:2].upper()
        prima_lettera_servizio = self.servizio[0].upper()
        codice_prenotazione = f"{prima_lettera_nome}{numero_persone}{prime_due_lettere_giorno}{prima_lettera_servizio}"
        return codice_prenotazione

    def mostraPrenotazione(self):
        print(f"prenotazione a nome {self.nome} per {self.pax} persone il giorno {self.giorno} a {self.servizio} ")
        print(f"codice prenotazione = {self.codPre}")
