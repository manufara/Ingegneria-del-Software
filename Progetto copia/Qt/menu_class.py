# classe piatto ----------------------------------
class Piatto():
    def __init__(self, nome, descrizione, prezzo):
        self.nome = nome
        self.descrizione = descrizione
        self.prezzo = prezzo

    def mostraPiatto(self):
        return "{self.nome} {self.descrizione} {self.prezzo}"


# classe menu -------------------------------------
class MenuClass():
    def __init__(self, piatti):
        self.piatti = piatti

    def mostraMenu(self):
        for piatto in self.piatti:
            piatto.mostraPiatto()

    def ModificaMenu(self):
        while True:
            print("\n--- Modifica Menu ---")
            print("1. Aggiungi piatto")
            print("2. Elimina piatto")
            print("3. Modifica piatto")
            print("4. Esci")
            scelta = input("Inserisci il numero corrispondente alla tua scelta: ")

            if scelta == '1':
                # Aggiungi un piatto
                numero = len(self.piatti)+1
                nome = input("inserisci nome del piatto: ")
                descrizione = input("inserisci descrizione del piatto: ")
                prezzo = input("inserisci il prezzo del piatto: ")
                new_piatto = Piatto.Piatto(numero, nome, descrizione, prezzo)
                self.piatti.append(new_piatto)

            elif scelta == '2':
                # Elimina un piatto
                self.mostraMenu()
                while True:
                    piatto_da_eliminare = int(input("'esci' o Inserisci il numero del piatto da eliminare: "))
                    if piatto_da_eliminare == "esci":
                        return
                    for piatto in self.piatti:
                        if piatto.numero == piatto_da_eliminare:
                            del self.piatti[piatto_da_eliminare-1]
                            print("piatto eliminato correttamente dal menu")
                            return

                    print("piatto non trovato, riprova")

            elif scelta == '3':
                # Modifica un piatto
                piatto_da_modificare = int(input("'esci' o Inserisci il numero del piatto da modificare: "))
                if piatto_da_modificare == "esci":
                    return
                for piatto in self.piatti:
                    if piatto.numero == piatto_da_modificare:

                        print("Cosa vuoi modificare?")
                        print("1. Prezzo")
                        print("2. Descrizione")
                        print()
                        modifica = input("Inserisci il numero della tua scelta: ")

                        if modifica == '1':
                            nuovo_prezzo = float(input(f"Inserisci il nuovo prezzo per '{piatto_da_modificare}': "))
                            piatto.prezzo = nuovo_prezzo
                            print(f"Prezzo di '{piatto}' modificato con successo.")

                        elif modifica == '2':
                            nuova_descrizione = input(f"Inserisci la nuova descrizione per '{piatto_da_modificare}': ")
                            piatto = nuova_descrizione
                            print(f"Descrizione di '{piatto}' modificata con successo.")
                        else:
                            print("Scelta non valida.")
                    else:
                        print(f"Il piatto indicato non è presente nel menu.")

            elif scelta == '4':
                print("Uscita dal menu di modifica.")
                break
            else:
                print("Scelta non valida, riprova.")


# classe comanda ----------------------------------
class Comanda:
    def __init__(self, cameriere):
        self.cameriere = cameriere
        self.piatti = []
        self.totale = 0

    def generaComanda(self):

        print("Inserire i piatti, digita 'conferma' per inviare:")
        MenuClass.menu.mostraMenu()
        while True:
            np=input("inserire il numero del piatto da aggiungere alla comanda : ")
            if np.lower()=="conferma":
                break
            np=int(np)
            aggiunto=False
            for piatto in MenuClass.menu.piatti:
                if np==piatto.numero:
                    self.piatti.append(piatto)
                    self.totale=+piatto.prezzo
                    print ("piatto aggiunto alla comanda")
                    aggiunto=True
            if not aggiunto : print("riprova")


# inizializzazione ---------------------------------
piatto1=Piatto("Moscioli", "Antipasto", 5)
piatto2=Piatto("Gnocchi", "Primo", 10)
piatto3=Piatto("Frittura","secondo",15)
piatto4=Piatto("tiramisu","Dolce",4)
piatti=[piatto1,piatto2,piatto3,piatto4]

menu=MenuClass(piatti)
