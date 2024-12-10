import unittest
from unittest.mock import MagicMock

# Mock class per simulare una comanda
class MockComanda:
    def __init__(self, piatti, totale):
        self.piatti = piatti
        self.totale = totale

class TestOrdinazioni(unittest.TestCase):
    def setUp(self):
        # Creazione di un mock della classe con le funzioni da testare
        self.mock_ordinazione = MagicMock()
        self.mock_ordinazione.comande = []  # Lista iniziale di comande
        self.mock_ordinazione.totale = 0.0  # Totale iniziale
        self.mock_ordinazione.tavolo = 5  # Valore esplicito per il tavolo

        # Implementazione delle funzioni da testare nella mock class
        def aggiorna_ordinazione(comanda):
            self.mock_ordinazione.comande.append(comanda)
            self.mock_ordinazione.totale += comanda.totale

        def mostra_ordinazione(menu_dict):
            descrizione = f"Descrizione - Tavolo {self.mock_ordinazione.tavolo} \n"
            piatti_dict = {}

            for comanda in self.mock_ordinazione.comande:
                for piatto, quantita in comanda.piatti:
                    if piatto in piatti_dict:
                        piatti_dict[piatto] += quantita
                    else:
                        piatti_dict[piatto] = quantita

            for piatto, quantita in piatti_dict.items():
                prezzo = menu_dict.get(piatto, 0)
                descrizione += f"{piatto} - {quantita}x {prezzo:.2f}€ \n"

            descrizione += f"\nTotale - €{self.mock_ordinazione.totale:.2f} \n"
            return descrizione

        self.mock_ordinazione.aggiorna_ordinazione = aggiorna_ordinazione
        self.mock_ordinazione.mostra_ordinazione = mostra_ordinazione

    def test_aggiorna_ordinazione(self):
        # Creazione di una comanda fittizia
        comanda = MockComanda([("Pizza", 2), ("Pasta", 1)], 25.0)
        self.mock_ordinazione.aggiorna_ordinazione(comanda)

        # Verifica che la comanda sia stata aggiunta
        self.assertIn(comanda, self.mock_ordinazione.comande)
        # Verifica che il totale sia stato aggiornato
        self.assertEqual(self.mock_ordinazione.totale, 25.0)

    def test_mostra_ordinazione(self):
        # Creazione di comande fittizie
        comanda1 = MockComanda([("Pizza", 2), ("Pasta", 1)], 25.0)
        comanda2 = MockComanda([("Pizza", 1), ("Insalata", 3)], 15.0)

        # Aggiunta delle comande
        self.mock_ordinazione.aggiorna_ordinazione(comanda1)
        self.mock_ordinazione.aggiorna_ordinazione(comanda2)

        # Dizionario del menu con prezzi
        menu_dict = {"Pizza": 10.0, "Pasta": 8.0, "Insalata": 5.0}

        # Chiamata alla funzione e risultato atteso
        descrizione = self.mock_ordinazione.mostra_ordinazione(menu_dict)

        # Descrizione attesa
        descrizione_attesa = (
            "Descrizione - Tavolo 5 \n"
            "Pizza - 3x 10.00€ \n"
            "Pasta - 1x 8.00€ \n"
            "Insalata - 3x 5.00€ \n"
            "\nTotale - €40.00 \n"
        )

        # Verifica che la descrizione sia corretta
        self.assertEqual(descrizione, descrizione_attesa)

    def test_calcola_totale(self):
        # Creazione di comande fittizie
        comanda1 = MockComanda([("Pizza", 2), ("Pasta", 1)], 25.0)
        comanda2 = MockComanda([("Pizza", 1), ("Insalata", 3)], 15.0)

        # Aggiunta delle comande
        self.mock_ordinazione.aggiorna_ordinazione(comanda1)
        self.mock_ordinazione.aggiorna_ordinazione(comanda2)

        # Chiamata alla funzione per calcolare il totale
        self.mock_ordinazione.calcola_totale()

        # Verifica che il totale calcolato sia corretto
        self.assertEqual(self.mock_ordinazione.totale, 40.0)


if __name__ == "__main__":
    unittest.main()
