# classe tavolo ---------------------------------
class Tavolo:
    def __init__(self, nrTavolo):
        self.nrTavolo = nrTavolo
        self.occupato = False
        self.capacita = 4
        self.prenotazione = None # Collegamento al codice della prenotazione che occupa il tavolo
        self.ordinazione = None

        #self.cameriere = None # non serve, perché per controllare se un tavolo è già assegnato basta ciclare sull'attributo
                                    # del cameriere


# Funzione per creare tavoli
def crea_tavoli():
    tavoli = []
    numero_tavoli = 20  # Si hanno 20 tavoli disponibili
    for i in range(1, numero_tavoli + 1):
        tavoli.append(Tavolo(nrTavolo=i))  # Crea un nuovo oggetto Tavolo e lo aggiunge alla lista
    return tavoli
