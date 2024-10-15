# classe piatto ----------------------------------
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

"""# classe comanda ----------------------------------
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
            if not aggiunto : print("riprova")"""

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
