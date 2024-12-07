import sys
sys.stdout.reconfigure(encoding='utf-8')
import os

def list_files(folder):
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        
        if os.path.isfile(item_path):
            print(item_path) 
        elif os.path.isdir(item_path):
            list_files(item_path) 

searched_folder = 'c:/Users/jessi/Documents/Infnet/4E24/Velocidade/AT'
print(f'Lista de arquivos encontrados no diretório: ')
list_files(searched_folder)