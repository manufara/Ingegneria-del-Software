import GestoreTavoli
import Ordinazione
import DataBase

class Cameriere:
    def __init__(self, id):
        self.id = id
        self.password = "Emilia"
        self.tavoli = []

    # assegna il cameriere al tavolo e viceversa, e crea l'ordine relativo al tavolo
    def assegna_cameriere(self, giorno, servizio):
        while True:
            input_utente = input("selezionare il tavolo da servire (digita 'esci' per uscire): ")

            # Controllo se l'utente vuole uscire
            if input_utente.lower() == "esci":
                break
            try:
                # Prova a convertire l'input in un numero
                i = int(input_utente)
                # Selezione del tavolo dal DB
                tavolo = DataBase.DB.dati_tavoli[giorno][servizio][i - 1]
                # Se ci sono clienti al tavolo
                if tavolo.occupato:
                    print(tavolo.Prenotazione.codPre)
                    # se il tavolo non è assegnato a nessun cameriere
                    if not tavolo.cameriere:
                        self.tavoli.append(tavolo)
                        tavolo.cameriere = self
                        print("assegnamento completato")
                        # crea ordinazione
                        if not tavolo.ordinazione:
                            tavolo.ordinazione = Ordinazione.Ordinazione(tavolo, self)
                            print("Ordinazione aperta")
                            return
                    # se il tavolo ha gia un cameriere
                    else :
                        # a te
                        if tavolo.cameriere == self :
                            print ("Il Tavolo è gia assegnato a te")
                            return
                        # ad altri
                        else :
                            print (f"IL Tavolo è gia assegnato al cameriere {tavolo.cameriere}")
                            return

                # Se il tavolo non è occupato, mostra un messaggio di errore
                else:
                    print(f"Il tavolo nr {i} non è occupato da nessun cliente, riprova o esci.")

            except ValueError:
                # Gestisce il caso in cui l'input non è un numero
                print("Errore: Inserisci un numero valido o digita 'esci' per uscire.")

            except IndexError:
                # Gestisce il caso in cui il numero inserito è fuori dall'intervallo di tavoli disponibili
                print(f"Errore: Il tavolo selezionato non esiste, riprova o digita 'esci'.")

def LoginCameriere(id, pasw):
    for cam in DataBase.DB.lista_camerieri:
        if (id == cam.id) and (pasw == cam.password):
            return cam

