import math
import Prenotazione
import copy
import Login
import GestoreTavoli
import DataBase
from datetime import datetime

class GestorePrenotazioni:

    def __init__(self):
        '''
        self.prenotazioniservizio={
            ("lunedi", "pranzo"): [],
            ("lunedi", "cena"): [],
            ("martedi", "pranzo"): [],
            ("martedi", "cena"): [],
            ("mercoledi", "pranzo"): [],
            ("mercoledi", "pranzo"): [],
            ("giovedi", "pranzo"): [],
            ("giovedi", "cena"): [],
            ("venerdi", "pranzo"): [],
            ("venerdi", "cena"): [],
            ("sabato", "pranzo"): [],
            ("sabato", "cena"): [],
            ("domenica", "pranzo"): [],
            ("domenica", "cena"): []
        }
        '''

    def VisualizzaListaPrenotazioni(self):

        for data, servizi in DataBase.prenotazioniservizio.items():
            for servizio, prenotazioni in servizi.items():
                print(f"Prenotazioni per il {data.strftime('%d/%m/%Y')} ({servizio}):")
                if prenotazioni:
                    for prenotazione in prenotazioni:
                        print(prenotazione.mostraPrenotazione)
                else:
                    print("  Nessuna prenotazione.")

    '''
    def ModificaPrenotazione(self, p):


        print(f"\n--- Modifica Prenotazione: {p.codPre} ---")
        while True:
            print("Cosa vuoi modificare?")
            print("1. Nome")
            print("2. Numero di persone")
            print("3. Data e ora")
            print("4. Conferma e salva modifiche")
            print("5. Annulla modifiche")
            scelta = input("Inserisci il numero corrispondente alla tua scelta: ")

            if scelta == '1':
                #chiedi dati
                nuovo_nome = input("Inserisci il nuovo nome: ")
                p.nome = nuovo_nome
            elif scelta == '2':
                #chiedi dati
                nuovo_pax = int(input("Inserisci il nuovo numero di persone: "))
                tavoliNec = math.ceil(nuovo_pax / 4)
                #casisitiche
                if tavoliNec > len(p.tavoli):  # Aumenta il numero di tavoli
                    tavoli_disponibili = [tavolo for tavolo in GestoreTavoli.GT.tavoliservizio[(p.giorno, p.servizio)] if not tavolo.occupato]
                    if tavoliNec>int(len(tavoli_disponibili)+len(p.tavoli)):#verifica possibilità di cambio
                        print("errore modificaprenotazione : tavoli non sufficienti")
                        return
                    # Libera i tavoli precedenti e compatta

                    self.EliminaPrenotazione(p)

                    p.pax=nuovo_pax
                    self.assegnaPrenotazione(p)

                elif tavoliNec < len(p.tavoli):  # Diminuisce il numero di tavoli
                    # Libera i tavoli in eccesso
                    GestoreTavoli.GT.LiberaTavoli(p.tavoli[tavoliNec:])
                    p.pax = nuovo_pax
                    p.tavoli = GestoreTavoli.GT.assegnaTavolo(p)
                    GestoreTavoli.GT.CompattaTavoli(p.giorno, p.servizio)



                    #ridimensiona la lista dei tavoli associati alla prenotazione
                    #sistema la sala
                    GestoreTavoli.GT.CompattaTavoli(p.giorno, p.servizio)

                # Se il numero di tavoli necessari rimane invariato, aggiorna solo il numero di persone
                p.pax = nuovo_pax

            elif scelta == '3':
                #chiedi dati

                nuovo_giorno = input("Inserisci la nuova data della prenotazione : ")
                nuovo_servizio = input("inserisci pranzo/cena: ")
                # nuova prenotazione np con data diversa
                np = copy.deepcopy(p)
                np.giorno=nuovo_giorno
                np.servizio=nuovo_servizio
                print(p.giorno)
                print(np.giorno)
                if self.assegnaPrenotazione(np):#modifica possibile
                    print("ok")
                    #libera
                    GestoreTavoli.GT.LiberaTavoli(p.tavoli)
                    self.prenotazioniservizio[(p.giorno, p.servizio)].remove(p)
                    #GestoreTavoli.CompattaTavoli(p.giorno, p.servizio)
                    #aggiorna
                    p = np


            elif scelta == '4':
                # aggiorna codpre
                p.codPre=p.genera_codice_prenotazione()
                print("Modifiche salvate con successo.")
                break
            elif scelta == '5':
                print("Modifiche annullate.")
                break
            else:
                print("Scelta non valida. Riprova.")
    '''
    def modificaPrenotazione(self, p):
        print (f"modifica della prenotazione : {p.codPre}, inserirei nuovi dati della prenotazione : ")
        # rimuovi momentaneamente la vecchia p
        GestoreTavoli.GT.LiberaTavoli(p.tavoli)
        # con i tavoli libera ricrea la prenotazione
        newP = self.CreaPrenotazione()
        # se è stata creata correttamente -> Elimina la vecchia
        if newP :
            self.EliminaPrenotazione(p)
            newP.mostraPrenotazione()
        # se non è stata creata -> Riassegna la vecchia
        else :
            self.assegnaPrenotazione(p)
            p.mostraPrenotazione()







    def CreaPrenotazione(self):
        # raccolta dati
        servizio=self.chiedi_servizio()
        pax=self.chiedi_pax()
        #visualizza i giorni della settimana e relativa disp
        #GestoreTavoli.GT.visualizza_disponiblita_settimana(servizio, pax)
        while True:
            # scelta giorno disponibile alla prenotazione
            giorno=self.chiedi_giorno()
            if not GestoreTavoli.GT.visualizza_disponibilita_giorno(giorno, servizio, pax):
                print(f"siamo pieni per il {giorno} a {servizio}, seleziona un altro giorno")
            else :
                break
                #conferma la prenotazione
        nome=input("inserisci nome della prenotazione")
        prenotazione=Prenotazione.Prenotazione(nome, pax, giorno, servizio)
        # compatta i tavoli di questo gs per evitare di assegnare tavoli separati
        GestoreTavoli.GT.CompattaTavoli(giorno, servizio)
        # assegna la prenotazione
        if self.assegnaPrenotazione(prenotazione):
            # conferma
            prenotazione.mostraPrenotazione()
            print("creata correttamente")
            return prenotazione
        # la prenotazione viene creata ma è inutilizzata e verra persa
        else:
            print("errore")
            return None

    def EliminaPrenotazione(self, p):
        if p in DataBase.prenotazioniservizio[p.giorno][p.servizio]:
            DataBase.prenotazioniservizio[p.giorno][p.servizio].remove(p)
            print(f"Prenotazione {p.codPre} rimossa correttamente")
            GestoreTavoli.GT.LiberaTavoli(p.tavoli)
            GestoreTavoli.GT.CompattaTavoli(p.giorno, p.servizio)
        else:
            print(f"Errore: la prenotazione {p.codPre} non è presente nella lista.")


    def assegnaPrenotazione(self, prenotazione):
        # tavoli che verranno assegnati alla prenotazione
        tavoliAss=GestoreTavoli.GT.assegnaTavolo(prenotazione)
        if tavoliAss:# se ci sono tavoli disponibili per la prenotazione
            # assegna i tavoli alla prenotazione
            prenotazione.tavoli=tavoliAss
            # assegna la prenotazione ai tavoli
            for t in tavoliAss:
                t.Prenotazione=prenotazione
                t.occupato=True

            # salva nel DB prenotazioni, se non gia presente
            if not self.VerificaEsistenzaPrenotazione(prenotazione):
                DataBase.prenotazioniservizio[prenotazione.giorno][prenotazione.servizio].append(prenotazione)
            return True
        else :
            print("errore assegna prenotazione : non ci sono tavoli da assegnare alla prenotazione")
            return False

    def VerificaEsistenzaPrenotazione(self, prenotazione):
        for p in DataBase.prenotazioniservizio[prenotazione.giorno][prenotazione.servizio]:
            if prenotazione.codPre == p.codPre:
                return True
        return False

    def cercaPrenotazione(self,codpre):
        # Chiede il codice prenotazione all'utente
        #codPre = input("Inserisci il codice prenotazione: ")

        for data, servizi in DataBase.prenotazioniservizio.items():
            for servizio, prenotazioni in servizi.items():
                print(f"Prenotazioni per il {data.strftime('%d/%m/%Y')} ({servizio}): ")
                if prenotazioni:
                    for prenotazione in prenotazioni:
                        if prenotazione.codPre==codpre :
                            print("prenotazione trovata")
                            return prenotazione
                else:
                    print("  Nessuna prenotazione.")
        # Scorre tutte le prenotazioni salvate in prenotazioniservizio

        # Se non viene trovata nessuna prenotazione
        print("Nessuna prenotazione trovata con il codice fornito.")
        return None



    def MenuPrenotazioni(self):
        while True:
            print("1. per creare una prenotazione")
            print("2. per gestire una prenotazione")
            print ("3. Per uscire")
            scelta =input()

            if scelta == '1':
                self.CreaPrenotazione()

            elif scelta =='2':
                while True:

                    cp=input("inserire codice prenotazione : ")
                    pr=self.cercaPrenotazione(cp)
                    if pr:

                        print ("1. Modifica Prenotazione")
                        print("2. Elimina Prenotazione")
                        print("3. Visualizza Prenotazione")
                        print("4. esci")
                        while True:
                            scelta2=input()
                            if scelta2 == '1':
                                self.modificaPrenotazione(pr)
                            elif scelta2 == '2':
                                self.EliminaPrenotazione(pr)
                            elif scelta2 == '3':
                                pr.mostraPrenotazione()
                            elif scelta2 == '4':
                                break
                    else: print("prenotazione non trovata, riprova")

            elif scelta == '3':
                break

            else :
                print ("scelta non valida, riprova")

            break


    def chiedi_servizio(self):
        servizi = ["pranzo", "cena"]

        while True:
            servizio = input("Inserisci il servizio (pranzo o cena): ").lower()
            if servizio in servizi:
                return servizio
            else:
                print("Servizio non valido. Riprova.")
    def chiedi_pax(self):
        while True:
            pax=int(input("inserisci il numero di persone: "))
            if pax <= 12 :
                return pax
            else : print("errore : max 12 persone")
    def chiedi_giorno(self):
        data_inizio = datetime(2024, 6, 1)
        data_fine = datetime(2024, 9, 30)
        while True:
            # Chiedi all'utente di inserire una data nel formato corretto
            data_input = input("Inserisci una data (formato DD/MM/YYYY): ")

            try:
                # Prova a convertire l'input in un oggetto datetime.date
                data_formattata = datetime.strptime(data_input, "%d/%m/%Y").date()
                print(data_formattata)

                # Controlla se la data è nell'intervallo consentito
                if data_inizio.date() <= data_formattata <= data_fine.date():
                    print(f"Data inserita correttamente: {data_formattata.strftime('%d/%m/%Y')}")
                    return data_formattata
                else:
                    print(f"La data deve essere compresa tra {data_inizio.strftime('%d/%m/%Y')} e {data_fine.strftime('%d/%m/%Y')}.")

            except ValueError:
                # In caso di errore nella conversione, stampa un messaggio e richiedi l'input
                print("Formato della data non valido. Riprova usando il formato DD/MM/YYYY.")




GP=GestorePrenotazioni()







