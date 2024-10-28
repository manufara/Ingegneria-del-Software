import DataBase
import GestoreTavoli
import Prenotazione
from datetime import datetime
import math

class Gestore_Prenotazioni:

    # visualizza la lista di tutte le prenotazioni esistenti
    def visualizza_lista_prenotazioni(self):

        for data, servizi in DataBase.DB.dati_prenotazioni.items():
            for servizio, prenotazioni in servizi.items():
                if prenotazioni:
                    print(f"Prenotazioni per il {data.strftime('%d/%m/%Y')} ({servizio}):")
                    for prenotazione in prenotazioni:
                        print(prenotazione.mostra_prenotazione())
        return

    # modifica prenotazione
    def modifica_prenotazione (self, p):
        print (f"modifica della prenotazione {p.codPre}")
        while True :
            x = int(input("Cosa vuoi modificare? \n 1) Data/Ora \n 2) Numero di Persone\n 3) Per uscire"))
            # modifica data/ora
            if x == 1:
                while True:
                    np = Prenotazione.Prenotazione(p.nome, p.pax, self.chiedi_giorno(), self.chiedi_servizio())
                    # se c'è disponibilità
                    if GestoreTavoli.GT.visualizza_disponibilita_giorno(np.giorno, np.servizio, np.pax):
                        self.elimina_prenotazione(p)
                        self.assegna_prenotazione(np)
                        print("modifica effettuata")
                        break
                    # se non cè disponibilità
                    else :
                        print(f"purtroppo siamo pieni per il {np.giorno} a {np.servizio}, prova con un altro giorno")
                        if input("se vuoi annullare la modifica digita 'esci' altrimenti premi invio") == "esci":
                            self.modifica_prenotazione(p)
                break

            # modifica pax
            if x == 2:
                while True:
                    np = Prenotazione.Prenotazione(p.nome, self.chiedi_pax(), p.giorno, p.servizio)
                    tn = math.ceil(int(np.pax) / 4) # tn = TavoliNecessari per la NuovaPrenotazione
                    # se aumentano i tavoli
                    if tn > math.ceil(int(p.pax) / 4):
                        # calcolo nr di tavoli liberi + p.tavoli -> verifico disp -> creo
                        tavoli_liberi = [tavolo for tavolo in DataBase.DB.dati_tavoli[p.giorno][p.servizio] if not tavolo.occupato]
                        t_disp = len(tavoli_liberi) + len(p.tavoli)
                        # se cè disponibilità per la modifica richiesta
                        if t_disp >= tn:
                            self.elimina_prenotazione(p)
                            self.assegna_prenotazione(np)
                            np.mostra_prenotazione()
                            break
                        else :
                            print(f"purtroppo siamo pieni per il {np.giorno} a {np.servizio}, prova con un altro giorno")
                            if input("se vuoi annullare la modifica digita 'esci' altrimenti premi invio") == "esci":
                                self.modifica_prenotazione(p)

                    # se diminuiscono i tavoli
                    if math.ceil(int(np.pax) / 4) < math.ceil(int(p.pax) / 4):
                        # libera i tavoli in eccesso
                        GestoreTavoli.GT.libera_tavoli(p.tavoli[math.ceil(int(np.pax) / 4):])
                        # aggiorna la prenotazione e assegna solo il numero di tavoli necessari
                        p.pax = np.pax
                        p.codPre = p.genera_codice_prenotazione()
                        p.tavoli = p.tavoli[:math.ceil(int(np.pax) / 4)]
                        GestoreTavoli.GT.compatta_tavoli(p.giorno, p.servizio)
                        p.mostra_prenotazione()
                        break
                    # se i tavoli rimangono invariati
                    else :
                        p.pax = self.chiedi_pax()
                        p.codPre = p.genera_codice_prenotazione()
                        p.mostra_prenotazione()
                        break

                if x == 3:
                    print("esci dal menu di modifica...")
                    self.menu_prenotazioni()

                else :
                    print("inserimento errato, riprova")
            break

    # inserisci dati new P, questa viene assegnata
    def crea_prenotazione(self):
        # raccolta dati
        servizio = self.chiedi_servizio()
        pax = self.chiedi_pax()
        while True:
            # scelta giorno disponibile alla prenotazione
            giorno = self.chiedi_giorno()
            if not GestoreTavoli.GT.visualizza_disponibilita_giorno(giorno, servizio, pax):
                print(f"siamo pieni per il {giorno} a {servizio}, seleziona un altro giorno")
            else :
                break
                #conferma la prenotazione
        nome = input("inserisci nome della prenotazione")
        prenotazione = Prenotazione.Prenotazione(nome, pax, giorno, servizio)
        # compatta i tavoli di questo gs per evitare di assegnare tavoli separati
        # GestoreTavoli.GT.compatta_tavoli(giorno, servizio)
        # assegna la prenotazione
        if self.assegna_prenotazione(prenotazione):
            # conferma
            prenotazione.mostra_prenotazione()
            print("creata correttamente")
            return prenotazione
        # la prenotazione viene creata ma è inutilizzata e verra persa
        else:
            print("errore")
            return None

    # assegna una prenotazione a un tavolo e la salva nel DB
    def assegna_prenotazione(self, prenotazione):
        # tavoli che verranno assegnati alla prenotazione
        tavoliAss=GestoreTavoli.GT.assegna_tavolo(prenotazione)
        if tavoliAss:# se ci sono tavoli disponibili per la prenotazione
            # assegna i tavoli alla prenotazione
            prenotazione.tavoli=tavoliAss
            # assegna la prenotazione ai tavoli
            for t in tavoliAss:
                t.Prenotazione=prenotazione
                t.occupato=True

            # salva nel DB prenotazioni, se non gia presente
            if not self.verifica_esistenza_prenotazione(prenotazione):
                DataBase.DB.dati_prenotazioni[prenotazione.giorno][prenotazione.servizio].append(prenotazione)
            return True
        else :
            print("errore assegna prenotazione : non ci sono tavoli da assegnare alla prenotazione")
            return False

    # elimina una prenotazione: la rimuove dal DB, libera i tavoli e li compatta
    def elimina_prenotazione(self, p):
        #se esiste la cancella
        if self.verifica_esistenza_prenotazione(p):
            DataBase.DB.dati_prenotazioni[p.giorno][p.servizio].remove(p)
            GestoreTavoli.GT.libera_tavoli(p.tavoli)
            GestoreTavoli.GT.compatta_tavoli(p.giorno, p.servizio)
            print(f"Prenotazione {p.codPre} rimossa correttamente")

        # altrimenti errore
        else:
            print(f"Errore: la prenotazione {p.codPre} non è presente nella lista.")

        return

    # verifica che una prenotazione esista nel DB
    def verifica_esistenza_prenotazione(self, prenotazione):
        for p in DataBase.DB.dati_prenotazioni[prenotazione.giorno][prenotazione.servizio]:
            if prenotazione.codPre == p.codPre:
                return True
        return False

    #trova una prenotazione nel DB attraverso il codice di prenotazione, se la trova viene mostrata altrimenti erroe
    def cerca_prenotazione(self):
        print ("cerca prenotazione")
        codpre = input("inserire il codice prenotazione : ")
        # breakpoint
        if codpre == "esci":
            print("ao")
            return

        for data, servizi in DataBase.DB.dati_prenotazioni.items():
            for servizio, prenotazioni in servizi.items():
                if prenotazioni:
                    for prenotazione in prenotazioni:
                        if prenotazione.codPre==codpre :
                            print("prenotazione trovata : ")
                            prenotazione.mostra_prenotazione()
                            return prenotazione
        print("Prenotazione non trovata")


        # Scorre tutte le prenotazioni salvate in prenotazioniservizio



    #Menu di navigazione per le funzioni del GestorePrenotazioni
    def menu_prenotazioni(self):
        while True:
            print("1. per creare una prenotazione")
            print("2. per gestire una prenotazione")
            print("3. per uscire")
            scelta = input()

            # crea
            if scelta == '1':
                self.crea_prenotazione()

            # modifica
            elif scelta == '2':
                pr = self.cerca_prenotazione()
                if pr:
                    while True:
                        print("1. Modifica Prenotazione")
                        print("2. Elimina Prenotazione")
                        print("3. Visualizza Prenotazione")
                        print("4. esci")
                        scelta2 = input()
                        if scelta2 == '1':
                            self.modifica_prenotazione(pr)
                        elif scelta2 == '2':
                            self.elimina_prenotazione(pr)
                        elif scelta2 == '3':
                            pr.mostra_prenotazione()
                        elif scelta2 == '4':
                            break  # Torna al menu principale delle prenotazioni
                else:
                    print("prenotazione non trovata, riprova")

            # esci
            elif scelta == '3':
                # print("Uscita dal menu prenotazioni.")
                break  # Esci dal menu delle prenotazioni

            else:
                print("scelta non valida, riprova")




    # chiede il tipo di servizio (pranzo/cena)
    def chiedi_servizio(self):
        servizi = ["pranzo", "cena"]

        while True:
            servizio = input("Inserisci il servizio (pranzo o cena): ").lower()
            if servizio in servizi:
                return servizio
            else:
                print("Servizio non valido. Riprova.")

    #  chiede il numero di persone
    def chiedi_pax(self):
        while True:
            try:
                pax=int(input("inserisci il numero di persone: "))
                if pax <= 12 :
                    return pax
                else : print("errore : max 12 persone")
            except ValueError :
                print ("errore d inserimento, riprova")

    # chiede la data e la converte nel formato utilizzato dal sistema
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



GP=Gestore_Prenotazioni()








