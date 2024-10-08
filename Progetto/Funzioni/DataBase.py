from datetime import date, timedelta
import Tavolo
import pickle
def creaTavoli():
    return [Tavolo.Tavolo(i + 1) for i in range(20)]

# Data di inizio e fine del periodo di apertura
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

def salva_dati(file_path):
    with open(file_path, 'wb') as file:
        # Salva i dati dei dizionari su file
        pickle.dump((prenotazioniservizio, tavoliservizio), file)
    print(f"Dati salvati correttamente su {file_path}")

def carica_dati(file_path):
    global prenotazioniservizio, tavoliservizio
    try:
        with open(file_path, 'rb') as file:
            # Carica i dati dal file
            prenotazioniservizio, tavoliservizio = pickle.load(file)
        print(f"Dati caricati correttamente da {file_path}")
    except FileNotFoundError:
        print(f"File {file_path} non trovato. Creazione di nuovi dati.")
        # Se il file non esiste, continua con i dati di default

