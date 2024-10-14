import Login
import DataBase
import threading
from _datetime import datetime
d = datetime.strptime("23/06/2024", "%d/%m/%Y").date()
s = "pranzo"


DataBase.DB.crea_database()
file_path = 'dati_prenotazioni.pkl'
DataBase.DB.carica_dati(file_path)
# back up automatico ogni 1 min
thread_backup = threading.Thread(target=DataBase.DB.esegui_backup_automatico, args=(file_path, 60))
thread_backup.daemon = True  # Rende il thread secondario
thread_backup.start()
Login.amministratore_menu(d,s)

