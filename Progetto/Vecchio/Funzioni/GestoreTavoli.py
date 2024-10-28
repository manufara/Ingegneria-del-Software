import DataBase
import GestorePrenotazioni
import math

class GestoreTavoli:

    # visualizza i tavoli con relative prenotazione di un dato giorno/servizio
    def visualizza_lista_tavoli(self, giorno, servizio):
        print(f"Tavoli per il {giorno} a {servizio}")
        for tavolo in DataBase.DB.dati_tavoli[giorno][servizio]:
            print(f"Tavolo nr {tavolo.nrTavolo}")
            if tavolo.occupato:
                print(f"Occupato - Codice prenotazione: {tavolo.Prenotazione.codPre}")
            else:
                print("Libero")

    # compatta i tavoli di un dato giorno/servizio per eliminare i buchi
    def compatta_tavoli(self, giorno, servizio):
        # Ottieni la lista di tavoli per il giorno e il servizio specificati
        tavoli = DataBase.DB.dati_tavoli[giorno][servizio]
        # lista prenotazione per il giorno e il servizio specificati
        prenotazioni = DataBase.DB.dati_prenotazioni[giorno][servizio]
        #libera i tavoli
        self.libera_tavoli(tavoli)
        #e li riassegna senza lasciare buchi
        for prenotazione in prenotazioni:
            GestorePrenotazioni.GP.assegna_prenotazione(prenotazione)





        #questa funzione non assegna propriamente i tavoli ma ritorna una lista di tavoli, che poi AssegnaPrenotazione utilizzerà

    #fornisce la lista di tavoli da attribuire alla prenotazione
    def assegna_tavolo(self, prenotazione):
        # calcola tavoli necessari
        tavoli_necessari = math.ceil(int(prenotazione.pax) / 4)
        #tavoli=self.tavoliservizio[(giorno,servizio)]
        tavoli_assegnati = []
        tavoli_liberi = [tavolo for tavolo in DataBase.DB.dati_tavoli[prenotazione.giorno][prenotazione.servizio] if not tavolo.occupato]
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

    # libera i tavoli senza eliminare la prenotazione
    def libera_tavoli(self, tavoli):
        for tavolo in tavoli:
            tavolo.occupato = False
            tavolo.Prenotazione = None

    #visualizzala disponibilità di un tot di giorni
    def visualizza_disponiblita_settimana(self, servizio, pax):
        giorni_settimana = ["lunedi", "martedi", "mercoledi", "giovedi", "venerdi", "sabato", "domenica"]
        for giorno in giorni_settimana:
            if self.visualizza_disponibilita_giorno(giorno, servizio, pax):
                print(f"{giorno} disponibile")
            else: print(f"{giorno} non disponibile")

    # visualizza la disponibilità di tavoli di un giorno/servizio
    def visualizza_disponibilita_giorno(self, giorno, servizio, pax):
        if self.visualizza_disponibilita_tavoli(giorno, servizio, pax):
            return True
        else : return False

    # visualizza la disponibilità dei tavoli, return true se ci sono abbastanza tavoli per pax
    def visualizza_disponibilita_tavoli(self, giorno, servizio, pax):
        tavoli_liberi = [tavolo for tavolo in DataBase.DB.dati_tavoli[giorno][servizio] if not tavolo.occupato]

        #  print (len(tavoli_liberi))
        tavoli_necessari = math.ceil(int(pax) / 4)
        if len(tavoli_liberi)>=tavoli_necessari:
            return True
        else:
            return False



GT=GestoreTavoli()