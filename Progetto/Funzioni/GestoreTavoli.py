import DataBase
import Cameriere
import Ordinazione
import math
import Tavolo
import GestorePrenotazioni


class GestoreTavoli:
    def __init__(self):
        '''
        self.tavoliservizio = {
            ("lunedi", "pranzo"): self.creaTavoli(),
            ("lunedi", "cena"): self.creaTavoli(),
            ("martedi", "pranzo"): self.creaTavoli(),
            ("martedi", "cena"): self.creaTavoli(),
            ("mercoledi", "pranzo"): self.creaTavoli(),
            ("mercoledi", "cena"): self.creaTavoli(),
            ("giovedi", "pranzo"): self.creaTavoli(),
            ("giovedi", "cena"): self.creaTavoli(),
            ("venerdi", "pranzo"): self.creaTavoli(),
            ("venerdi", "cena"): self.creaTavoli(),
            ("sabato", "pranzo"): self.creaTavoli(),
            ("sabato", "cena"): self.creaTavoli(),
            ("domenica", "pranzo"): self.creaTavoli(),
            ("domenica", "cena"): self.creaTavoli()
        }
        '''

    def creaTavoli(self):
        return [Tavolo.Tavolo(i + 1) for i in range(20)]

    def visualizzaListaTavoli(self, giorno, servizio):
        for tavolo in DataBase.tavoliservizio[giorno][servizio]:
            print(f"Tavolo nr {tavolo.nrTavolo}")
            if tavolo.occupato:
                print(f"Occupato - Codice prenotazione: {tavolo.Prenotazione.codPre}")
            else:
                print("Libero")

    def CompattaTavoli(self, giorno, servizio):
        # Ottieni la lista di tavoli per il giorno e il servizio specificati
        tavoli = DataBase.tavoliservizio[giorno][servizio]
        # lista prenotazione per il giorno e il servizio specificati
        prenotazioni = DataBase.prenotazioniservizio[giorno][servizio]
        #libera i tavoli
        self.LiberaTavoli(tavoli)
            #e li riassegna senza lasciare buchi
        for prenotazione in prenotazioni:
            GestorePrenotazioni.GP.assegnaPrenotazione(prenotazione)





#questa funzione non assegna propriamente i tavoli ma ritorna una lista di tavoli, che poi AssegnaPrenotazione utilizzerà
    def assegnaTavolo(self, prenotazione):
        # calcola tavoli necessari
        tavoli_necessari = math.ceil(int(prenotazione.pax) / 4)
        #tavoli=self.tavoliservizio[(giorno,servizio)]
        tavoli_assegnati = []
        tavoli_liberi = [tavolo for tavolo in DataBase.tavoliservizio[prenotazione.giorno][prenotazione.servizio] if not tavolo.occupato]
        # verifica disponibilità
        if len(tavoli_liberi) >= tavoli_necessari:
            #for tavolo in tavoli:
             #   if  not tavolo.occupato:
            for tavolo in tavoli_liberi:
                    tavoli_assegnati.append(tavolo)
                    # occupa tavolo
                    #tavolo.occupato=True
                    if len(tavoli_assegnati) == tavoli_necessari:
                        break
        else :
            print("ERRORE assegna tavolo ")
            return None
        return tavoli_assegnati

    def LiberaTavoli(self, tavoli):
        for tavolo in tavoli:
            tavolo.occupato = False
            tavolo.Prenotazione = None


    def visualizza_disponiblita_settimana(self, servizio, pax):
        giorni_settimana = ["lunedi", "martedi", "mercoledi", "giovedi", "venerdi", "sabato", "domenica"]
        for giorno in giorni_settimana:
            if self.visualizza_disponibilita_giorno(giorno, servizio, pax):
                print(f"{giorno} disponibile")
            else: print(f"{giorno} non disponibile")
    def visualizza_disponibilita_giorno(self, giorno, servizio, pax):
        if self.visualizza_disponibilita_tavoli(giorno, servizio, pax):
            return True
        else : return False
    def visualizza_disponibilita_tavoli(self, giorno, servizio, pax):
        tavoli_liberi = [tavolo for tavolo in DataBase.tavoliservizio[giorno][servizio] if not tavolo.occupato]
      #  print (len(tavoli_liberi))
        tavoli_necessari = math.ceil(int(pax) / 4)
        if len(tavoli_liberi)>=tavoli_necessari:
            return True
        else:
            return False



GT=GestoreTavoli()