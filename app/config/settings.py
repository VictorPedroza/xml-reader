import os 
import json

class Config:
    def __init__(self, file):
        self.dir = os.path.dirname(os.path.abspath(file))
        self.fileDir = os.path.abspath(os.path.join(self.dir, "..", "config", "settings.json"))
        
        with open(self.fileDir, "r", encoding="utf-8") as arq:
            self.data = json.load(arq)
            
        self.entry = os.path.abspath(self.data.get("entry"))
        self.output = os.path.abspath(self.data.get("output"))
        self.backup = os.path.join(self.entry, self.data.get("backup"))
        
    def makeDir(self, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)
            
        return dir
    
    def getEntry(self):
        return self.makeDir(self.entry)
    
    def getOutput(self):
        return self.makeDir(self.output) 
    
    def getBackup(self):
        return self.makeDir(self.backup)   