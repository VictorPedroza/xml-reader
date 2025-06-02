from config.settings import Config

settings = Config(__file__)

entry = settings.getEntry()
output = settings.getOutput()
backup = settings.getBackup()