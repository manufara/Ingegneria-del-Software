import Menu

class Comanda:
    def __init__(self, cameriere):
        self.cameriere = cameriere
        self.piatti = []
        self.totale = 0

    # popola la nuova comanda creata che sara poi aggiunta all'ordinazione totale
    def genera_comanda(self):
        print("Inserire i piatti, digita 'conferma' per inviare:")
        Menu.menu.mostra_menu()
        while True:
            np=input("inserire il numero del piatto da aggiungere alla comanda : ")
            if np.lower()=="conferma":
                break
            np=int(np)
            aggiunto=False
            for piatto in Menu.menu.piatti:
                if np==piatto.numero:
                    self.piatti.append(piatto)
                    self.totale=+piatto.prezzo
                    print ("piatto aggiunto alla comanda")
                    aggiunto=True
            if not aggiunto : print("riprova")