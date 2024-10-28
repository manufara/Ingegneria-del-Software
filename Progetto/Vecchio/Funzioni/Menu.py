import Piatto

class Menu():

    def __init__(self, piatti ):
        self.piatti = piatti

        self.Piatto_del_giorno = None

    # mostra ogni piatto del menu
    def mostra_menu(self):
        for piatto in self.piatti:
            piatto.mostra_piatto()

    # aggiungi, elimina o modifica un piatto al menu
    def modifica_menu(self):

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
                prezzo = float(input("inserisci il prezzo del piatto: "))
                new_piatto = Piatto.Piatto(numero, nome, descrizione, prezzo)
                self.piatti.append(new_piatto)

            elif scelta == '2':
                # Elimina un piatto
                self.mostra_menu()
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


# creazione del menu
piatto1=Piatto.Piatto(1,"Moscioli", "Antipasto", 5)
piatto2=Piatto.Piatto(2,"Gnocchi", "Primo", 10)
piatto3=Piatto.Piatto(3,"Frittura","secondo",15)
piatto4=Piatto.Piatto(4,"tiramisu","Dolce",4)
piatti=[piatto1,piatto2,piatto3,piatto4]
# istanza
menu=Menu(piatti)



