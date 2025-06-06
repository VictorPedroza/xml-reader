#Importação de Bibibliotecas
import os 
import json

# Classe de Configuração
class Config:
    def __init__(self, file):
        # Diretório principal 
        self.dir = os.path.dirname(os.path.abspath(file))
        # Diretório de Configurações
        self.file_dir = os.path.abspath(os.path.join(self.dir, "..", "config", "settings.json"))
        
        # Lendo arquivo ".json"
        try:
            with open(self.file_dir, "r", encoding="utf-8") as arq:
                self.data = json.load(arq)
        except FileNotFoundError:
            raise FileNotFoundError(f'Erro ao buscar "settings.json"')
        # Pasta de Entrada 
        self.entry_dir = os.path.abspath(self.data.get("entry"))
        # Pasta de Saída
        self.output_dir = os.path.abspath(self.data.get("output"))
        # Pasta de Backup
        self.backup_dir = os.path.join(self.entry_dir, self.data.get("backup"))
     
     # Função de Verificar se existe a pasta   
    def _make_dir(self, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)
        return dir
    
    @property
    def get_entry(self): # Função de retorno da pasta de Entrada
        return self._make_dir(self.entry_dir)
    
    @property
    def get_output(self): # Função de retorno da pasta de Saída
        return self._make_dir(self.output_dir) 
    
    @property
    def get_backup(self): # Função de retorno da pasta de Backup
        return self._make_dir(self.backup_dir)   
    
    def listDir(self, dir):
        return os.listdir(dir)