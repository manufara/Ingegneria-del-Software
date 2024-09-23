import GestorePrenotazioni
import Cameriere
import Ordinazione
import GestoreTavoli
import Menu

#qui abbiamo le "viste" con le funzioni da associare ai futuri bottoni

def login():

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

def cliente_menu():
    while True:
        print("\n---- MENU CLIENTE ----")
        print("1. Visualizzare il menu")
        print("2. prenotazione")
        print("3. Info")
        print("4. Logout")
        scelta = input("Inserisci il numero corrispondente alla tua scelta: ")

        if scelta == '1':
            Menu.menu.mostraMenu()
        elif scelta == '2':
            GestorePrenotazioni.GP.MenuPrenotazioni()
        elif scelta=='3':
            print ("info")
        elif scelta == '4':
            login()
        else:
            print("Scelta non valida. Riprova.")

def cameriere_menu(cameriere, giorno, servizio):

    while True:
        print("\n---- MENU CAMERIERE ----")

        print("1. Prendere una comanda")
        print("2. Visualizza Lista Prenotazioni")
        print("3. Visualizza Menu")
        print("4. esci")
        scelta = input("Inserisci il numero corrispondente alla tua scelta: ")

        if scelta == '1':
            #creare la relazione cameriere-tavolo
            cameriere.AssegnaCameriere(giorno, servizio)
        elif scelta == '2':
            GestorePrenotazioni.GP.VisualizzaListaPrenotazioni(giorno, servizio)
        elif scelta == '3':
            Menu.menu.mostraMenu()
        elif scelta == '4':
            login()
        else:
            print("Scelta non valida. Riprova.")

def amministratore_menu(giorno, servizio):
    while True:
        print("\n---- MENU AMMINISTRATORE ----")
        print("1. Visualizza Tavoli")
        print("2. Stampa conto")
        print("3. Prenotazione")
        print("4. Modifica Menu")
        print("5. Logout")

        scelta = input("Inserisci il numero corrispondente alla tua scelta: ")

        if scelta == '1':
            g=chiedi_giorno()
            s=chiedi_servizio()
            GestoreTavoli.GT.visualizzaListaTavoli(g, s)

        elif scelta == '2':
            t=int(input("inserire numero del Tavolo : "))
            tavolo = GestoreTavoli.GT.tavoliservizio[(giorno, servizio)][t-1]
            if tavolo.ordinazione:
                tavolo.ordinazione.mostra_ordinazione()
            else:
                print("Non ci sono ordinazioni per questo tavolo.")

        elif scelta == '3':
            while True:
                GestorePrenotazioni.GP.MenuPrenotazioni()

        elif scelta == '4' :
            print("modifica menu")
            Menu.menu.ModificaMenu()

        elif scelta == '5':
            login()
        else:
            print("Scelta non valida. Riprova.")


def chiedi_giorno():
    giorni_settimana = ["lunedi", "martedi", "mercoledi", "giovedi", "venerdi", "sabato", "domenica"]

    while True:
        giorno = input("Inserisci il giorno della settimana: ").lower()
        if giorno in giorni_settimana:
            return giorno
        else:
            print("Giorno non valido. Riprova.")

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