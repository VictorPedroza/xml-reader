from config.settings import Config
from folder.main import Folder

settings = Config(__file__)

entry = settings.get_entry
output = settings.get_output
backup = settings.get_backup

folder = Folder(entry, output, backup)

for arq in settings.listDir(entry):
    print(folder.save(arq))