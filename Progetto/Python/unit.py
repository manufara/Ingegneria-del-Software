import unittest
from datetime import date
from Database import database
from GestorePrenotazioni import GestorePrenotazioni
from GestoreTavoli import GestoreTavoli
from Prenotazione import Prenotazione

class TestGestionePrenotazioni(unittest.TestCase):

    def setUp(self):
        """
        Prepara i dati iniziali per i test, inclusi un database temporaneo e istanze dei gestori.
        """
        self.gestore_prenotazioni = GestorePrenotazioni()
        self.gestore_tavoli = GestoreTavoli()
        database.crea_database()  # Ricrea il database per ogni test

    def test_crea_prenotazione(self):
        """
        Testa la creazione di una prenotazione e verifica che sia correttamente registrata.
        """
        nome = "Mario Rossi"
        giorno = date(2024, 6, 15)
        servizio = "pranzo"
        numero_persone = 4
        codice = "abcd"

        # Crea una prenotazione
        prenotazione = Prenotazione(nome, numero_persone, giorno, servizio, codice)
        risultato = self.gestore_prenotazioni.assegna_prenotazione(prenotazione)

        self.assertTrue(risultato)
        self.assertIn(prenotazione, database.dati_prenotazioni[giorno][servizio])
        self.assertEqual(len(prenotazione.tavoli_assegnati), 1)  # Una prenotazione di 4 persone richiede 1 tavolo

    def test_modifica_prenotazione(self):
        """
        Testa la modifica di una prenotazione esistente.
        """
        nome = "Mario Rossi"
        giorno = date(2024, 6, 15)
        servizio = "pranzo"
        numero_persone = 4
        codice = "abcd"

        # Crea una prenotazione iniziale
        prenotazione = Prenotazione(nome, numero_persone, giorno, servizio, codice)
        self.gestore_prenotazioni.assegna_prenotazione(prenotazione)

        # Modifica la prenotazione: cambia numero di persone
        nuovo_numero_persone = 8
        prenotazione.numero_persone = nuovo_numero_persone
        self.gestore_prenotazioni.modifica_prenotazione()

        # Verifica la modifica
        self.assertEqual(prenotazione.numero_persone, nuovo_numero_persone)
        self.assertEqual(len(prenotazione.tavoli_assegnati), 2)  # 8 persone richiedono 2 tavoli

    def test_elimina_prenotazione(self):
        """
        Testa l'eliminazione di una prenotazione esistente.
        """
        nome = "Mario Rossi"
        giorno = date(2024, 6, 15)
        servizio = "pranzo"
        numero_persone = 4
        codice = "abcd"
        # Crea una prenotazione
        prenotazione = Prenotazione(nome, numero_persone, giorno, servizio, codice)
        self.gestore_prenotazioni.assegna_prenotazione(prenotazione)

        # Elimina la prenotazione
        self.gestore_prenotazioni.elimina_prenotazione(prenotazione)

        # Verifica che la prenotazione non esista più
        self.assertNotIn(prenotazione, database.dati_prenotazioni[giorno][servizio])
        for tavolo in prenotazione.tavoli_assegnati:
            self.assertFalse(tavolo.occupato)  # I tavoli dovrebbero essere liberati

if __name__ == '__main__':
    unittest.main()
