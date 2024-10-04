from datetime import date, timedelta
import Tavolo
def creaTavoli():
    return [Tavolo.Tavolo(i + 1) for i in range(20)]

# Data di inizio e fine del periodo
data_inizio = date(2024, 6, 1)
data_fine = date(2024, 9, 30)

# Dizionario per memorizzare prenotazioni dal 01/06 al 30/09
prenotazioniservizio = {}
tavoliservizio = {}
# Ciclo su tutte le date dal 01/06 al 30/09
data_corrente = data_inizio
while data_corrente <= data_fine:
    # Aggiungi una nuova chiave per la data corrente con "pranzo" e "cena"
    prenotazioniservizio[data_corrente] = {
        "pranzo": [],  # Lista per le prenotazioni di pranzo
        "cena": []     # Lista per le prenotazioni di cena
    }
    tavoliservizio[data_corrente] = {
        "pranzo" : creaTavoli(),
        "cena" : creaTavoli()
    }
    # Incrementa la data di un giorno
    data_corrente += timedelta(days=1)

# Visualizza la struttura per verificare
print(prenotazioniservizio)
