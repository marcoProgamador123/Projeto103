import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/MARCO ANTONIO/Downloads"

# criando a classe gerenciador de evento
class FileEventHandler(FileSystemEventHandler):
    
    def on_created(self, event):
        print(f"Olá,{event.src_path} foi criado")
    
    def on_deleted(self,event):
        print(f"Opa! Alguem excluiu {event.src_path}!")
    
    def on_modified(self, event):
        print(f"Oi! Alguem modificou {event.src_path}!")
    
    def on_moved(self,event):
        print(f"Olá o arquivo {event.src_path} foi movido") 

#Inicializando a classe gerenciador de eventos
event_handler = FileEventHandler()

#inicializar o observador
observer = Observer()

#agendar o observador
observer.schedule(event_handler,from_dir,recursive = True)

#startando o observador
observer.start()

try:
    while True:
        time.sleep(2)
        print("Executando...")
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()        
                
                   