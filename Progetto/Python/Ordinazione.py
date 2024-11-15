from Comanda import Comanda
from PyQt5.QtWidgets import QMessageBox


# classe ordinazione ------------------------------
class Ordinazione:
    def __init__(self, tavolo):
        self.tavolo = tavolo # Viene passato un intero che corrisponde all'attributo nrTavolo della classe Tavolo
        self.comande = []
        self.totale = 0

    def aggiorna_ordinazione(self, comanda):
        self.comande.append(comanda)
        self.totale += comanda.totale

    def mostra_ordinazione(self):
        descrizione = f"Descrizione - Tavolo {self.tavolo} \n"
        piatti_dict = {} # Crea un dizionario per accumulare i piatti e le quantità
        
        for comanda in self.comande: # Itera sulle comande
            for piatto, quantita in comanda.piatti:
                if piatto in piatti_dict:
                    # Se il piatto è già nel dizionario, incrementa la quantità
                    piatti_dict[piatto] += quantita
                else:
                    # Se il piatto non è nel dizionario, lo aggiunge con la quantità
                    piatti_dict[piatto] = quantita
    
        for piatto, quantita in piatti_dict.items():
            for comanda in self.comande:
                if piatto in [p[0] for p in comanda.piatti]:  # Verifica se il piatto è presente in questa comanda
                    index = [p[0] for p in comanda.piatti].index(piatto) # Trova il piatto nella lista della comanda
                    prezzo = comanda.prezzi[index]  # Prezzo del piatto
                    descrizione += f"{piatto} - {quantita}x {prezzo}€ \n"
                    break
        
        descrizione += f"\nTotale - €{self.totale:.2f} \n"
        return descrizione

    def conferma_ordinazione(self, tavolo, comanda_corrente):
        if comanda_corrente.piatti:
            tavolo.ordinazione.aggiorna_ordinazione(comanda_corrente)
            comanda_corrente = Comanda()  # Resetta la comanda
            
            message = QMessageBox()
            message.setText("Comanda confermata.")
            message.exec()
        else:
            message = QMessageBox()
            message.setText("Nessuna comanda da confermare.")
            message.exec()
