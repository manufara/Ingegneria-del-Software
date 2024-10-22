from prenotazione_class import Tavolo


# classe piatto -----------------------------------
class Piatto():
    def __init__(self, categoria, nome, descrizione, prezzo):
        self.categoria = categoria
        self.nome = nome
        self.descrizione = descrizione
        self.prezzo = prezzo

    def mostraPiatto(self):
        return f"{self.nome}: {self.descrizione} - {self.prezzo}€"


# classe menu -------------------------------------
class MenuClass():
    def __init__(self, piatti):
        self.piatti = piatti


# classe ordinazione ------------------------------
class Ordinazione:
    def __init__(self, tavolo): #, cameriere
        self.tavolo = tavolo # viene passato il tavolo come intero, uguale quindi all'attributo nrTavolo della classe Tavolo
        self.comande = []
        self.totale = 0 #tavolo.prenotazione.numero_persone * 2 # inizialmente c'è il coperto

        #self.cameriere = cameriere

    def aggiorna_ordinazione(self, comanda):
        self.comande.append(comanda)
        self.totale += comanda.totale

    def mostra_ordinazione(self):
        descrizione = f"Descrizione - Tavolo {self.tavolo} \n"
        cont = 0
        for comanda in self.comande:
            for piatto, quantita in comanda.piatti:
                descrizione += f"{quantita}x {piatto} - {comanda.prezzi[cont]} \n"
                cont = cont + 1
        descrizione += f"\nTotale - €{self.totale:.2f} \n"
        return descrizione


# classe comanda -----------------------------------
class Comanda:
    def __init__(self): #, cameriere
        self.piatti = []
        self.totale = 0
        self.prezzi = []

        #self.cameriere = cameriere

    def genera_comanda(self, piatto, prezzo, quantita):
        self.piatti.append((piatto, quantita))
        self.prezzi.append(prezzo)
        self.totale += prezzo * quantita


"""# classe cameriere ----------------------------------
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
                print(f"Errore: Il tavolo selezionato non esiste, riprova o digita 'esci'.")"""


# Funzione per leggere il menu da un file con categorie e piatti e creare oggetti Piatto e MenuClass
def leggi_menu_da_file(file_path):
    piatti = []  # Lista che conterrà oggetti Piatto
    categoria_corrente = None  # Per tenere traccia della categoria attuale
    
    with open(file_path, 'r') as file:
        for linea in file:
            linea = linea.strip()
            
            # Ignora le righe vuote
            if not linea:
                continue
            
            # Se la riga non contiene una virgola, la trattiamo come categoria
            if ',' not in linea:
                categoria_corrente = linea  # Aggiorna la categoria corrente
                continue
            
            # Se la riga contiene una virgola, la trattiamo come piatto
            try:
                nome, descrizione, prezzo = linea.split(',')
                piatto = Piatto(categoria_corrente, nome, descrizione.strip(), prezzo.strip())  # Crea un oggetto Piatto
                piatti.append(piatto)  # Aggiungi l'oggetto Piatto alla lista
            except ValueError:
                print(f"Errore nel formato della riga: {linea}")

    menu = MenuClass(piatti)  # Crea un oggetto MenuClass con i piatti
    return menu
