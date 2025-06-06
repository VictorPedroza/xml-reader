import os
import shutil
from datetime import date

class Folder:
    def __init__(self, entry, output, backup):
        self.entryDir = entry
        self.outputDir = output
        self.bakcupDir = backup
    
    def dataFolder(self, dest):
        today = date.today().strftime("%Y-%m-%d")
        path = os.path.join(dest, today)
        os.makedirs(path, exist_ok=True)
        
        return path
        
    def save(self, file):
        if file.endswith('.xml'):
            dirFile = os.path.join(self.entryDir, file)
            destBackup = self.dataFolder(self.bakcupDir)
            destOutput = self.dataFolder(self.outputDir)
            shutil.copy2(dirFile, destBackup)
            shutil.move(dirFile, destOutput)
            