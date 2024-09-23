import GestoreTavoli
import Ordinazione

class Cameriere:
    def __init__(self, id):
        self.id = id
        self.password = "Emilia"
        self.tavoli = []


    def AssegnaCameriere(self, giorno, servizio):
        i=int(input("selezionare il tavolo da servire : "))#
        tavolo=GestoreTavoli.GT.tavoliservizio[(giorno, servizio)][i-1]
        while True:
            if tavolo.occupato:
                print (tavolo.Prenotazione.codPre)
                #relazione cameriere-tavolo
                if not (tavolo in self.tavoli):
                    self.tavoli.append(tavolo)
                    tavolo.cameriere=self

                #se il tavolo non ha un conto aperto, crealo
                if not tavolo.ordinazione:
                    tavolo.ordinazione=Ordinazione.Ordinazione(tavolo, self)
                #aggiorna ordinazione
                tavolo.ordinazione.aggiornaOrdinazione()
                break


            else : print("tavolo non occupato, riprova")


c1 = Cameriere("c1")
c2 = Cameriere("c2")
c3 = Cameriere("c3")
c4 = Cameriere("c4")
c5 = Cameriere("c5")

ListaCamerieri = [c1, c1, c3, c4, c5]
#vista cameriere


def LoginCameriere(id, pasw):
    for cam in ListaCamerieri:
        if (id == cam.id) and (pasw == cam.password):
            return cam

