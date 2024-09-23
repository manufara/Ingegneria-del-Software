import GestorePrenotazioni
import Piatto
import Cameriere
import Ordinazione
import GestoreTavoli
import Menu
import Prenotazione
import Login








#giorno = GestorePrenotazioni.chiedi_giorno()
#servizio = GestorePrenotazioni.chiedi_servizio()

#script iniziale per simulazioni

giorno = "giovedi"
servizio = "pranzo"

pr1=Prenotazione.Prenotazione("matteo",3,"giovedi","pranzo")
GestorePrenotazioni.GP.assegnaPrenotazione(pr1)
pr2=Prenotazione.Prenotazione("flaia",5,"giovedi","pranzo")
GestorePrenotazioni.GP.assegnaPrenotazione(pr2)
pr3=Prenotazione.Prenotazione("giacomo",2,"giovedi","pranzo")
GestorePrenotazioni.GP.assegnaPrenotazione(pr3)
pr4=Prenotazione.Prenotazione("raffaele",6,"venerdi","pranzo")
GestorePrenotazioni.GP.assegnaPrenotazione(pr4)
pr5=Prenotazione.Prenotazione("luigi", 60, "giovedi", "pranzo" )
GestorePrenotazioni.GP.assegnaPrenotazione(pr5)

Login.login()
