import GestorePrenotazioni
import Piatto
import Cameriere
import Ordinazione
import GestoreTavoli
import Menu
import Prenotazione
import Login
import DataBase


'''
giorno = Login.chiedi_giorno()

p1=Prenotazione.Prenotazione("matteo", 3, giorno, "pranzo")
GestorePrenotazioni.GP.assegnaPrenotazione(p1)
p2=Prenotazione.Prenotazione("andre", 5, giorno, "pranzo")
GestorePrenotazioni.GP.assegnaPrenotazione(p2)
p3=Prenotazione.Prenotazione("emanuele", 2, giorno, "pranzo")
GestorePrenotazioni.GP.assegnaPrenotazione(p3)
p4=Prenotazione.Prenotazione("filippo", 8, giorno, "pranzo")
GestorePrenotazioni.GP.assegnaPrenotazione(p4)
p5=Prenotazione.Prenotazione("giulio", 10, giorno, "cena")
GestorePrenotazioni.GP.assegnaPrenotazione(p5)
'''
#servizio = GestorePrenotazioni.chiedi_servizio()
file_path = 'dati_prenotazioni.pkl'

DataBase.carica_dati(file_path)

Login.login()

