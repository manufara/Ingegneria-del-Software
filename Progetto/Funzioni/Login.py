import GestorePrenotazioni
import Cameriere
import GestoreTavoli
import Menu
import DataBase
# questo file non è utile all imple,entazione del software
# è un sostituto del software in se per verificarne la funzionalità da terminale python

# qui abbiamo le "viste" con le funzioni da associare ai futuri bottoni

# accesso ai vari menu
def menu_principale():

    while True:
        print("---- LOGIN ----")
        print("Seleziona il tipo di utente:")
        print("1. Cliente")
        print("2. Dipendente")

        scelta = input("Inserisci il numero corrispondente alla tua scelta: ")

        if scelta == '1':
            cliente_menu()

        elif scelta == '2':
            LoginDipedente()

        else:
            print("Scelta non valida. Riprova.")
# vista cliente
def cliente_menu():
    while True:
        print("\n---- MENU CLIENTE ----")
        print("1. Visualizzare il menu")
        print("2. prenotazione")
        print("3. Info")
        print("4. Logout")
        scelta = input("Inserisci il numero corrispondente alla tua scelta: ")

        # visualizza menu
        if scelta == '1':
            Menu.menu.mostra_menu()
        # prenotazioni
        elif scelta == '2':
            GestorePrenotazioni.GP.menu_prenotazioni()
        # info sito
        elif scelta == '3':
            print ("info")
        # logout
        elif scelta == '4':
            menu_principale()

        else:
            print("Scelta non valida. Riprova.")
# vista cameriere
def cameriere_menu(cameriere, giorno, servizio):

    while True:
        print("\n---- MENU CAMERIERE ----")

        print("1. Prendere una comanda")
        print("2. Servi nuovo Tavolo")
        print("3. Visualizza Lista Tavoli")
        print("4. Visualizza Menu")
        print("5. esci")

        scelta = input("Inserisci il numero corrispondente alla tua scelta: ")

        #creare la relazione cameriere-tavolo e crea nuova ordinazione
        if scelta =='1':
            while True:
                i = input("inserisci il numero del tavolo")
                # breakpoint
                if i == "esci":
                    break
                i = int(i)
                tavolo = DataBase.DB.dati_tavoli[giorno][servizio][i-1]
                if tavolo:
                    if tavolo.ordinazione:
                        tavolo.ordinazione.aggiorna_ordinazione()
                        break
                else :
                    print("tavolo non trovato, riprova")

        elif scelta == '2':
            # assegna e torna al menu cameriere
            cameriere.assegna_cameriere(giorno, servizio)
            cameriere_menu(cameriere, giorno, servizio)

        # visualizza i tavoli in sala
        elif scelta == '3':
            GestoreTavoli.GT.visualizza_lista_tavoli(giorno, servizio)

        # visualizza il menu
        elif scelta == '4':
            Menu.menu.mostra_menu()

        # logout
        elif scelta == '5':
            menu_principale()

        else:
            print("Scelta non valida. Riprova.")
#vista admin
def amministratore_menu(giorno, servizio):
    while True:
        print("\n---- MENU AMMINISTRATORE ----")
        print("1. Visualizza Tavoli")
        print("2. Stampa conto")
        print("3. Prenotazione")
        print("4. Modifica Menu")
        print ("5. Visualizza Lista Prenotazioni")
        print("6. Logout")

        scelta = input("Inserisci il numero corrispondente alla tua scelta: ")

        if scelta == '1':
            GestoreTavoli.GT.visualizza_lista_tavoli(giorno, servizio)

        elif scelta == '2':
            t=int(input("inserire numero del Tavolo : "))
            tavolo = DataBase.DB.dati_tavoli[giorno][servizio]
            if tavolo.ordinazione:
                tavolo.ordinazione.mostra_ordinazione()
            else:
                print("Non ci sono ordinazioni per questo tavolo.")

        elif scelta == '3':
            GestorePrenotazioni.GP.menu_prenotazioni()

        elif scelta == '4' :
            print("modifica menu")
            Menu.menu.modifica_menu()
        elif scelta == '5' :
            GestorePrenotazioni.GP.visualizza_lista_prenotazioni()
        elif scelta == '6':
            menu_principale()
        else:
            print("Scelta non valida. Riprova.")



def chiedi_giorno():
    from datetime import datetime
    while True:
        # Chiedi all'utente d' inserire una data nel formato corretto
        data_input = input("Inserisci una data (formato DD/MM/YYYY): ")

        try:
            # Prova a convertire l input in un oggetto datetime.date
            data_formattata = datetime.strptime(data_input, "%d/%m/%Y").date()
            print(f"Data inserita correttamente: {data_formattata.strftime('%d/%m/%Y')}")
            return data_formattata

        except ValueError:
            # In caso di errore nella conversione, stampa un messaggio e richiedi l'input
            print("Formato della data non valido. Riprova usando il formato DD/MM/YYYY.")

def chiedi_servizio():
    servizi = ["pranzo", "cena"]

    while True:
        servizio = input("Inserisci il servizio (pranzo o cena): ").lower()
        if servizio in servizi:
            return servizio
        else:
            print("Servizio non valido. Riprova.")

def LoginDipedente():

    giorno=chiedi_giorno()
    servizio=chiedi_servizio()
    while True:
        id = input("inserire username : ")
        password = input("inserire Password : ")
        #cameriere
        if Cameriere.LoginCameriere(id, password):
            cam=Cameriere.LoginCameriere(id, password)
            cameriere_menu(cam, giorno, servizio)
        #admin
        elif id == "Admin":
            if password == "Emiliadmin":
                amministratore_menu(giorno, servizio)
        #errore
        print("utente non trovato, riprova : ")