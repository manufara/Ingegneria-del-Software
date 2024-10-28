
class Prenotazione:
    def __init__(self, nome, pax, giorno, servizio):
        self.nome = nome
        self.pax = pax
        self.giorno = giorno
        self.servizio = servizio

        self.codPre=self.genera_codice_prenotazione()
        self.tavoli = []
        self.note = None

    # genera il codice prenotazione dai dati dell aprenotazione
    def genera_codice_prenotazione(self):
        prima_lettera_nome = self.nome[0].upper()
        numero_persone = str(self.pax)
        DDMM = self.giorno.strftime("%d%m")
        prima_lettera_servizio = self.servizio[0].upper()
        codice_prenotazione = f"{prima_lettera_nome}{numero_persone}{DDMM}{prima_lettera_servizio}"
        return codice_prenotazione

    # mostra i principali dati della prenotazione
    def mostra_prenotazione(self):
        print(f"prenotazione a nome {self.nome} per {self.pax} persone il giorno {self.giorno} a {self.servizio} ")
        print(f"codice prenotazione = {self.codPre}")
